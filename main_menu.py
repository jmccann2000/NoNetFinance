import PySimpleGUI as Gui
import numpy as np


def print_category_value(pct, all_vals):
    absolute = int(np.round(pct / 100. * np.sum(all_vals)))
    return "{:.1f}% (${:d})".format(pct, absolute)


def category_sums(panda):
    categories = set(panda["Category"])
    rem_categories = set()
    cat_sums = []
    for cat in categories:
        cat_total = panda.loc[panda["Category"] == cat, "Cost"].sum()
        if cat_total != 0:
            cat_sums.append(cat_total)
        else:
            rem_categories.add(cat)

    for cat in rem_categories:
        categories.remove(cat)

    cat_to_sum = {}
    for key in categories:
        for value in cat_sums:
            cat_to_sum[key] = value
            cat_sums.remove(value)
            break

    return cat_to_sum


def create(panda):
    headers = panda.columns.values.tolist()
    data_table = [
        [Gui.Table(values=panda.values.tolist(), headings=headers, auto_size_columns=True, key="-DATATABLE-")],
        [Gui.Button("Exit")]
    ]
    total_spent = panda.loc[:, "Cost"].sum()
    stat_menu = [
        [Gui.Text("Total Spent:"), Gui.Text("$" + str(total_spent))]
    ]
    layout = [
        [Gui.Column(data_table), Gui.VerticalSeparator(), Gui.Column(stat_menu)]
    ]
    window = Gui.Window("Spending Overview",
                        layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == Gui.WIN_CLOSED:
            break

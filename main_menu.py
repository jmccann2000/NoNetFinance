import PySimpleGUI as Gui
import numpy as np

import rules_menu


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

    ]
    total_spent = panda.loc[:, "Cost"].sum()
    header = [
        [Gui.Text("Total Spent: $"+str(total_spent))]
    ]
    categories_pane = [
        [Gui.Text("Categories:")],
        [Gui.Column([
            [Gui.Button("Auto/Gas"),
             Gui.Text("$123.12")],
            [Gui.Button("Grocery"),
             Gui.Text("$500.12")]
        ])],
        [Gui.Button("Edit Categories")]
    ]
    footer = [
        [Gui.Button("Exit"), Gui.Button("Rules")]
    ]
    layout = [
        [header],
        [Gui.Column(data_table), Gui.VerticalSeparator(), Gui.Column(categories_pane)],
        [footer]
    ]
    window = Gui.Window("Spending Overview",
                        layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == Gui.WIN_CLOSED:
            break
        if event == "Rules":
            rules_menu.create(["category1", "cat2"])

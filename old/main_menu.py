import PySimpleGUI as Gui
import numpy as np

import rules_menu
import category_ui
import edit_category_ui


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
        [
            Gui.Text("Total Spent: $"+str(total_spent), font=("Helvetica", 15, "bold")),
            Gui.Push(),
            Gui.Text("11/16/22 - 12/16/22", font=("Helvetica", 13))
         ]
    ]
    category_to_cost  = sorted(category_sums(panda).items(), key=lambda x:x[1])
    sortdict = dict(category_to_cost)
    categories_column = []
    for key in sortdict:
        key_as_ui = [Gui.Button(key), Gui.Push(), Gui.Text("$" + str(sortdict[key]))]
        categories_column.append(key_as_ui)

    categories_column.reverse()
    categories_pane = [
        [Gui.Text("Categories:", font=("Helvetica", 12))],
        [Gui.Column(categories_column)],
        [Gui.Button("Edit Categories")]
    ]
    footer = [
        [Gui.Button("Exit"), Gui.Push(), Gui.Button("Rules")]
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
        if event in set(panda["Category"]):
            category_ui.create(panda, event)
            window.bring_to_front()
        if event == "Edit Categories":
            edit_category_ui.build(panda)

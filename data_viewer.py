import PySimpleGUI as Gui
import main_menu


def regulate_data(panda, header, desc_col_label, date_col_label, category_col_label, cost_col_label):
    header.remove(desc_col_label)
    header.remove(date_col_label)
    header.remove(category_col_label)
    header.remove(cost_col_label)
    panda.drop(header, inplace=True, axis=1)
    name_mapping = {desc_col_label: "Description", date_col_label: "Date", category_col_label: "Category",
                    cost_col_label: "Cost"}
    return panda.rename(columns=name_mapping)


def create(filename, panda):
    headers = panda.columns.values.tolist()
    data_table = [
        [Gui.Table(values=panda.values.tolist(), headings=headers, auto_size_columns=True, key="-DATATABLE-")],
        [Gui.Text("Select description column:"), Gui.DropDown(values=headers, key="-DESC-")],
        [Gui.Text("Select date column:"), Gui.DropDown(values=headers, key="-DATE-")],
        [Gui.Text("Select category column:"), Gui.DropDown(values=headers, key="-CATEGORY-")],
        [Gui.Text("Select cost column:"), Gui.DropDown(values=headers, key="-COST-")],
        [Gui.Button("Exit"), Gui.Button("Continue")]
    ]
    window = Gui.Window(filename, data_table)
    while True:
        event, values = window.read()
        if event == "Exit" or event == Gui.WIN_CLOSED:
            break
        if event == "Continue":
            required_data_filled = values["-DESC-"] and values["-DATE-"] and values["-CATEGORY-"] and values["-COST-"]
            if required_data_filled:
                panda = regulate_data(panda, headers, values["-DESC-"], values["-DATE-"],
                                      values["-CATEGORY-"], values["-COST-"])
                window.close()
                main_menu.create(panda)
    window.close()

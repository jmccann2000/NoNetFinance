import PySimpleGUI as Gui


def create(panda, category_name):
    category_panda = panda.query("Category == '%s'" % category_name)
    headers = panda.columns.values.tolist()
    data_table = [
        [Gui.Table(values=category_panda.values.tolist(), headings=headers, auto_size_columns=True, key="-DATATABLE-")],
    ]
    layout = [data_table]
    window = Gui.Window(category_name + " Overview", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == Gui.WIN_CLOSED:
            break
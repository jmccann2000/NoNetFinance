import PySimpleGUI as Gui


def create(panda, category_name):
    category_panda = panda.query("Category == '%s'" % category_name)
    headers = panda.columns.values.tolist()

    total_spent = category_panda.loc[:, "Cost"].sum()
    header = [
        [
            Gui.Text("Total Spent: $"+str(total_spent), font=("Helvetica", 15, "bold")),
            Gui.Push(),
            Gui.Text("11/16/22 - 12/16/22", font=("Helvetica", 13))
         ]
    ]
    
    data_table = [
        [Gui.Table(values=category_panda.values.tolist(), headings=headers, auto_size_columns=True, key="-DATATABLE-")],
    ]

    footer = [
        [Gui.Button("Exit")]
    ]
    
    layout = [
        header,
        data_table,
        footer
    ]
    window = Gui.Window(category_name + " Overview", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == Gui.WIN_CLOSED:
            break
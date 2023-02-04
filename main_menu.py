import PySimpleGUI as Gui


def create(panda):
    headers = panda.columns.values.tolist()
    data_table = [
        [Gui.Table(values=panda.values.tolist(), headings=headers, auto_size_columns=True, key="-DATATABLE-")]
    ]
    total_spent = panda.loc[:, "Cost"].sum()
    right_menu = [
        [Gui.Text("Total Spent:"), Gui.Text("$" + str(total_spent))]
    ]
    layout = [
        [Gui.Column(data_table), Gui.Column(right_menu)],
        [Gui.Button("Exit")]
    ]
    window = Gui.Window("Spending Overview",
                        layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == Gui.WIN_CLOSED:
            break

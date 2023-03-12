import PySimpleGUI as Gui

class CategoryView:
    def __init__(self, controller):
        self.controller = controller
        self.window = None

    def show(self, category):
        panda = self.controller.model.data_table
        category_name = category
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
        self.window = Gui.Window(category_name + " Overview", layout)
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == Gui.WIN_CLOSED:
                break

    def close(self):
        if self.window is not None:
            self.window.close()
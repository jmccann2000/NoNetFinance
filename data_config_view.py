import PySimpleGUI as Gui

class DataConfigView:
    def __init__(self, controller):
        self.controller = controller
        self.window = None
        

    def show(self):
        headers = self.controller.model.data_table.columns.values.tolist()
        data_table = [
            [Gui.Table(values=self.controller.model.data_table.values.tolist(), headings=headers, auto_size_columns=True, key="-DATATABLE-")],
            [Gui.Text("Select description column:"), Gui.DropDown(values=headers, key="-DESC-")],
            [Gui.Text("Select date column:"), Gui.DropDown(values=headers, key="-DATE-")],
            [Gui.Text("Select category column:"), Gui.DropDown(values=headers, key="-CATEGORY-")],
            [Gui.Text("Select cost column:"), Gui.DropDown(values=headers, key="-COST-")],
            [Gui.Button("Exit"), Gui.Button("Continue")]
        ]
        self.window = Gui.Window(self.controller.model.file_location, data_table)
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == Gui.WIN_CLOSED:
                break
            if event == "Continue":
                self.controller.normalize_data_table(values["-DESC-"], values["-DATE-"],
                                      values["-CATEGORY-"], values["-COST-"])
                break
        self.window.close()

    def close(self):
        if self.window is not None:
            self.window.close()
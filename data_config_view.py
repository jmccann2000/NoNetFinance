import PySimpleGUI as Gui

class DataConfigView:
    def init(self):
        self.window = None

    def create(self, panda, filename):
        headers = panda.columns.values.tolist()
        data_table = [
            [Gui.Table(values=panda.values.tolist(), headings=headers, auto_size_columns=True, key="-DATATABLE-")],
            [Gui.Text("Select description column:"), Gui.DropDown(values=headers, key="-DESC-")],
            [Gui.Text("Select date column:"), Gui.DropDown(values=headers, key="-DATE-")],
            [Gui.Text("Select category column:"), Gui.DropDown(values=headers, key="-CATEGORY-")],
            [Gui.Text("Select cost column:"), Gui.DropDown(values=headers, key="-COST-")],
            [Gui.Button("Exit"), Gui.Button("Continue")]
        ]
        self.window = Gui.Window(filename, data_table)

    def close(self):
        if self.window is not None:
            self.window.close()
import PySimpleGUI as Gui

class EditCategoryView:
    def __init__(self, controller):
        self.controller = controller
        self.window = None

    def show(self):
        header =   [
            Gui.Text("Categories", font=("Helvetica", 15, "bold"))
         ]
        categories = [
                
            ]
        footer = [
            [Gui.Button("Exit"), Gui.Push(), Gui.Button("Add Category")]
        ]
        layout = [header,footer]
        self.window = Gui.Window("Edit Categories", layout)
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == Gui.WIN_CLOSED:
                break
        self.window.Close()
    
    def close(self):
        if self.window is not None:
            self.window.close()
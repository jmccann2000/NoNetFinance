import PySimpleGUI as Gui

class RulesView:
    def __init__(self, controller):
        self.controller = controller
        self.window = None

    def show(self):
        header = [
            Gui.Titlebar("Rules")
        ]
        rules_pane = [
            [
                Gui.Text("If contains 'ball', move to "),
                Gui.DropDown(["Auto/Gas", "Grocery"]),
                Gui.Button("-")
            ]
        ]
        footer = [
            [Gui.Button("Back/Apply"), Gui.Push(), Gui.Button("Add Rule"), Gui.Push(), Gui.Button("Back")]
        ]
        layout = [
            header,
            [Gui.VPush()],
            rules_pane,
            [Gui.VPush()],
            footer
        ]
        window = Gui.Window("Rules",
                            layout)
        while True:
            event, values = window.read()
            if event == "Back" or event == Gui.WIN_CLOSED:
                break
            if event == "Back/Apply":
                break

        window.close()

    def close(self):
        if self.window is not None:
            self.window.close()
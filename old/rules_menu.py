import PySimpleGUI as Gui


def create(categories):
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
            # Apply rules, may need panda passed in here
            break

    window.close()

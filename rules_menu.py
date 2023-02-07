import PySimpleGUI as Gui


def create(categories):
    header = [
        Gui.Text("Rules")
    ]
    rules_pane = [
        [
            Gui.Text("If contains 'ball', move to "),
            Gui.DropDown(["Auto/Gas", "Grocery"])
        ]
    ]
    footer = [
        Gui.Button("Back/Apply"),
        Gui.Button("Back")
    ]
    layout = [
        header,
        rules_pane,
        footer
    ]
    window = Gui.Window("Spending Overview",
                        layout)
    while True:
        event, values = window.read()
        if event == "Back" or event == Gui.WIN_CLOSED:
            break
        if event == "Back/Apply":
            # Apply rules, may need panda passed in here
            break

    window.close()

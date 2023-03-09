import PySimpleGUI as Gui

def build(panda):
    header =   [
            Gui.Text("Categories", font=("Helvetica", 15, "bold"))
         ]
    categories = [
            
        ]
    footer = [
        [Gui.Button("Exit"), Gui.Push(), Gui.Button("Add Category")]
    ]
    layout = [header,footer]
    window = Gui.Window("Edit Categories", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == Gui.WIN_CLOSED:
            break
    window.Close()
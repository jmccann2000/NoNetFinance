import PySimpleGUI as Gui
import os.path
import data_viewer
import pandas as pd

# First the window layout in 2 columns
file_list_column = [
    [
        Gui.Text("Current Folder"),
        Gui.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        Gui.FolderBrowse(),
    ],
    [
        Gui.Listbox(
            values=[], enable_events=True, size=(50, 20), key="-FILE LIST-"
        )
    ],
    [Gui.Button("Exit"), Gui.Button("Import")]
]

layout = [
    [
        Gui.Column(file_list_column)
    ]
]

window = Gui.Window("Import Transactions", layout)


def import_file(window, values):
    filename = values["-FILE LIST-"][0]
    full_filename = os.path.join(
        values["-FOLDER-"], filename
    )
    data_panda = pd.read_csv(full_filename)
    window.close()
    data_viewer.create(filename, data_panda)


def fetch_directory_content(window, values):
    folder = values["-FOLDER-"]
    if os.path.exists(folder):
        file_list = os.listdir(folder)
    else:
        file_list = []

    file_names = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith(".csv")
    ]
    window["-FILE LIST-"].update(file_names)


while True:
    event, values = window.read()
    if event == "Exit" or event == Gui.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        fetch_directory_content(window, values)
    elif event == "Import":
        import_file(window, values)

window.close()

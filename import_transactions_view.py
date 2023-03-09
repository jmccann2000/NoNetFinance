import PySimpleGUI as Gui
import os.path
import pandas as pd

class ImportTransactionsView:
    def __init__(self, controller):
        self.controller = controller
        self.folder_path = ""
        self.file_list = []
        self.window = None
        self.layout = [
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
        
    def show(self):
        self.window = Gui.Window("Import Transactions", self.layout)
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == Gui.WIN_CLOSED:
                break
            elif event == "-FOLDER-":
                self.folder_path = values["-FOLDER-"]
                self.controller.fetch_directory_content(self.folder_path)
            elif event == "-FILE LIST-":
                selected_file = values["-FILE LIST-"][0]
                self.controller.import_file(selected_file)
            elif event == "Import":
                if self.file_list:
                    selected_file = self.file_list[0]
                    self.controller.import_file(selected_file)
            self.window.refresh()
        self.window.close()
        
    def update_file_list(self, file_names):
        self.file_list = file_names
        self.window["-FILE LIST-"].update(self.file_list)

    def close(self):
        self.window.close()
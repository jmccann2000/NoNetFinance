import PySimpleGUI as Gui
import os.path
import pandas as pd
import sys
sys.path.append("..")
from import_transactions_view import ImportTransactionsView


class ImportTransactionsController:
    def __init__(self):
        self.view = ImportTransactionsView(self)
        
    def import_file(self, filename):
        full_filename = os.path.join(self.view.folder_path, filename)
        data_panda = pd.read_csv(full_filename)
        self.view.close()
        self.model.set_file_location(full_filename)
        self.model.set_data_table(data_panda)
        
    def fetch_directory_content(self, folder):
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
        self.view.update_file_list(file_names)
        
    def run(self, model):
        self.model = model
        self.view.show()
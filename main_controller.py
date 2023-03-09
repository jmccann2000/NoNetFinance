import PySimpleGUI as Gui
from import_transactions_controller import ImportTransactionsController
from data_config_controller import DataConfigController
from model import Model

class MainController:
    def __init__(self):
        self.import_controller = ImportTransactionsController()
        self.data_config_controller = DataConfigController()
        self.window = Gui.Window("Main Menu", [[Gui.Button("Import Data")]])
        self.model = Model()

    def start(self):
        self.import_controller.run(self.model)
        self.data_config_controller

        
main_controller = MainController()
main_controller.start()
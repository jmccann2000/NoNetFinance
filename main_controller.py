import PySimpleGUI as Gui
from import_transactions_controller import ImportTransactionsController
from data_config_controller import DataConfigController
from dashboard_controller import DashboardController
from transaction_factory import TransactionFactory
from model import Model

class MainController:
    def __init__(self):
        self.import_controller = ImportTransactionsController()
        self.data_config_controller = DataConfigController()
        self.dashboard_controller = DashboardController()

    def start(self):
        self.model = Model()
        self.model.set_data_table(TransactionFactory.get_transaction_model())
        self.dashboard_controller.run(self.model)


        
main_controller = MainController()
main_controller.start()
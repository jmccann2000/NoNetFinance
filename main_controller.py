import PySimpleGUI as Gui
from dashboard_controller import DashboardController
from transaction_factory import TransactionFactory
from model import Model

class MainController:
    def __init__(self):
        self.dashboard_controller = DashboardController()

    def start(self):
        self.model = Model()
        self.model.set_data_table(TransactionFactory.get_transaction_model())
        self.dashboard_controller.run(self.model)


        
main_controller = MainController()
main_controller.start()
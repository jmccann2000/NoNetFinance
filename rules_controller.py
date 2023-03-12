from rules_view import RulesView

class RulesController:
    def __init__(self):
        self.view = RulesView(self)

    def run(self, model):
        self.model = model
        self.view.show()
        self.view.close()
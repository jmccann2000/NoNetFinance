from category_view import CategoryView

class CategoryController:
    def __init__(self):
        self.view = CategoryView(self)

    def run(self, model, category):
        self.model = model
        self.view.show(category)
        self.view.close()
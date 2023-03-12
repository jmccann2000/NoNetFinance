from edit_category_view import EditCategoryView

class EditCategoryController:
    def __init__(self):
        self.view = EditCategoryView(self)

    def run(self, model):
        self.model = model
        self.view.show()
        self.view.close()
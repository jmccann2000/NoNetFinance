from dashboard_view import DashboardView

class DashboardController:
    def __init__(self):
        self.view = DashboardView(self)

    def category_sums(self):
        panda = self.model.data_table
        categories = set(panda["Category"])
        rem_categories = set()
        cat_sums = []
        for cat in categories:
            cat_total = panda.loc[panda["Category"] == cat, "Cost"].sum()
            if cat_total != 0:
                cat_sums.append(cat_total)
            else:
                rem_categories.add(cat)

        for cat in rem_categories:
            categories.remove(cat)

        cat_to_sum = {}
        for key in categories:
            for value in cat_sums:
                cat_to_sum[key] = value
                cat_sums.remove(value)
                break

        return cat_to_sum

    def run(self, model):
         self.model = model
         self.view.show() 
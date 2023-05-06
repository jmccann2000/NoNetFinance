from data_config_view import DataConfigView

class DataConfigController:
     def __init__(self):
          self.view = DataConfigView(self)

     def normalize_data_table(self, desc_col_label, date_col_label, category_col_label, cost_col_label):
          header = self.model.data_table.columns.values.tolist()
          header.remove(date_col_label)
          header.remove(category_col_label)
          header.remove(cost_col_label)
          header.remove(desc_col_label)
          self.model.data_table.drop(header, inplace=True, axis=1)
          name_mapping = {desc_col_label: "Description", date_col_label: "Date", category_col_label: "Category",
                              cost_col_label: "Cost"}
          norm_table = self.model.data_table.rename(columns=name_mapping)
          self.model.set_data_table(norm_table)

     def run(self, model):
          self.model = model
          self.model.show
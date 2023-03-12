class Model:
    def __init__(self):
        self.file_location = None
        self.data_table = None
        self.categories = None

    def set_data_table(self, table):
        self.data_table = table

    def set_file_location(self, file_name):
       self.file_location = file_name
        
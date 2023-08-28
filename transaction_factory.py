import pandas as pd
import os.path

class TransactionFactory:

    @staticmethod
    def get_transaction_model():
         transactions = TransactionFactory.import_transactions()
         return TransactionFactory.normalize_data_table(transactions, "Description","Transaction Date","Category", "Debit")

    @staticmethod
    def normalize_data_table(transactions, desc_col_label, date_col_label, category_col_label, cost_col_label):
          header = transactions.columns.values.tolist()
          header.remove(date_col_label)
          header.remove(category_col_label)
          header.remove(cost_col_label)
          header.remove(desc_col_label)
          transactions.drop(header, inplace=True, axis=1)
          name_mapping = {desc_col_label: "Description", date_col_label: "Date", category_col_label: "Category",
                              cost_col_label: "Cost"}
          norm_table = transactions.rename(columns=name_mapping)
          return norm_table

    @staticmethod
    def import_transactions():
        folder_path = os.getcwd() + "\\transactions"
        print(folder_path)
        all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
        combined_data = pd.DataFrame()

        for file in all_files:
            file_path = os.path.join(folder_path, file)
            data = pd.read_csv(file_path)
            combined_data = pd.concat([combined_data, data])  
            
        return combined_data
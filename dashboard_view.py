import tkinter as tk
from tkinter import ttk
import pandas as pd

class DashboardView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Spending Overview")

    def show(self):
        panda = self.controller.model.data_table
        headers = panda.columns.values.tolist()

        # Header
        total_spent = panda.loc[:, "Cost"].sum()
        header_frame = tk.Frame(self.window)
        header_frame.pack(fill=tk.X, pady=(0, 10))

        total_spent_label = tk.Label(header_frame, text="Total Spent: $" + str(total_spent), font=("Helvetica", 15, "bold"))
        total_spent_label.pack(side=tk.LEFT)

        date_label = tk.Label(header_frame, text="11/16/22 - 12/16/22", font=("Helvetica", 13))
        date_label.pack(side=tk.RIGHT)

        # Data table
        table_frame = tk.Frame(self.window)
        table_frame.pack(side=tk.LEFT, padx=(0, 10))

        tree = ttk.Treeview(table_frame, columns=headers, show="headings")
        for column in headers:
            tree.heading(column, text=column)
            tree.column(column, stretch=True)

        for index, row in panda.iterrows():
            tree.insert("", "end", values=row.tolist())

        tree.pack(fill=tk.BOTH, expand=True)

        # Categories pane
        categories_frame = tk.Frame(self.window)
        categories_frame.pack(side=tk.LEFT)

        categories_label = tk.Label(categories_frame, text="Categories:", font=("Helvetica", 12))
        categories_label.pack(anchor=tk.NW, pady=(0, 5))

        category_to_cost = sorted(self.controller.category_sums().items(), key=lambda x: x[1])
        sortdict = dict(category_to_cost)

        for key in sortdict:
            key_frame = tk.Frame(categories_frame)
            key_frame.pack(fill=tk.X, pady=(0, 5))

            category_button = tk.Button(key_frame, text=key, command=lambda key=key: self.controller.open_category(key))
            category_button.pack(side=tk.LEFT)

            cost_label = tk.Label(key_frame, text="$" + str(sortdict[key]))
            cost_label.pack(side=tk.RIGHT)

        edit_categories_button = tk.Button(categories_frame, text="Edit Categories", command=self.controller.open_edit_categories)
        edit_categories_button.pack(pady=(10, 0))

        # Footer
        footer_frame = tk.Frame(self.window)
        footer_frame.pack(fill=tk.X, pady=(10, 0), anchor='s')

        exit_button = tk.Button(footer_frame, text="Exit", command=self.window.destroy)
        exit_button.pack(side=tk.LEFT, anchor='sw')

        rules_button = tk.Button(footer_frame, text="Rules", command=self.controller.open_rules)
        rules_button.pack(side=tk.RIGHT, anchor='se')

        self.window.mainloop()
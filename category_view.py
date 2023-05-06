import tkinter as tk
from tkinter import ttk

class CategoryView:
    def __init__(self, controller):
        self.controller = controller
        self.window = None

    def show(self, category):
        self.window = tk.Tk()
        self.window.title(category + " Overview")

        panda = self.controller.model.data_table
        category_name = category
        category_panda = panda.query("Category == '%s'" % category_name)
        headers = panda.columns.values.tolist()

        total_spent = category_panda.loc[:, "Cost"].sum()

        header = tk.Frame(self.window)
        header.pack(fill=tk.X, pady=(0, 10))

        total_spent_label = tk.Label(header, text="Total Spent: $" + str(total_spent), font=("Helvetica", 15, "bold"))
        total_spent_label.pack(side=tk.LEFT)

        date_label = tk.Label(header, text="11/16/22 - 12/16/22", font=("Helvetica", 13))
        date_label.pack(side=tk.RIGHT)

        # Data table
        table_frame = tk.Frame(self.window)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        tree = ttk.Treeview(table_frame, columns=headers, show='headings')
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)

        for col in headers:
            tree.heading(col, text=col)
            tree.column(col, anchor='center')

        for index, row in category_panda.iterrows():
            tree.insert('', 'end', values=row.tolist())

        tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')

        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        footer = tk.Frame(self.window)
        footer.pack(fill=tk.X, pady=(10, 0))

        exit_button = tk.Button(footer, text="Exit", command=self.window.destroy)
        exit_button.pack(side=tk.LEFT)

        self.window.mainloop()

    def close(self):
        if self.window is not None:
            self.window.destroy()
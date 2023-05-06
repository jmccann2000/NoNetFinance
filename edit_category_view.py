import tkinter as tk

class EditCategoryView:
    def __init__(self, controller):
        self.controller = controller
        self.window = None

    def show(self):
        self.window = tk.Tk()
        self.window.title("Edit Categories")

        header = tk.Label(self.window, text="Categories", font=("Helvetica", 15, "bold"))
        header.pack(pady=(0, 10))

        footer = tk.Frame(self.window)
        footer.pack(fill=tk.X, pady=(10, 0))

        exit_button = tk.Button(footer, text="Exit", command=self.window.destroy)
        exit_button.pack(side=tk.LEFT)

        add_category_button = tk.Button(footer, text="Add Category")
        add_category_button.pack(side=tk.RIGHT)

        self.window.mainloop()

    def close(self):
        if self.window is not None:
            self.window.destroy()
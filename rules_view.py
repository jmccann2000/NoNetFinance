import tkinter as tk

class RulesView:
    def __init__(self, controller):
        self.controller = controller
        self.window = None

    def show(self):
        self.window = tk.Tk()
        self.window.title("Rules")

        header = tk.Label(self.window, text="Rules", font=("Helvetica", 15, "bold"))
        header.pack(pady=(0, 10))

        rules_pane = tk.Frame(self.window)
        rules_pane.pack(pady=(10, 10))

        text = tk.Label(rules_pane, text="If contains 'ball', move to ")
        text.pack(side=tk.LEFT)

        options = ["Auto/Gas", "Grocery"]
        dropdown = tk.OptionMenu(rules_pane, tk.StringVar(value=options[0]), *options)
        dropdown.pack(side=tk.LEFT)

        remove_button = tk.Button(rules_pane, text="-")
        remove_button.pack(side=tk.LEFT)

        footer = tk.Frame(self.window)
        footer.pack(fill=tk.X, pady=(10, 0))

        back_apply_button = tk.Button(footer, text="Back/Apply")
        back_apply_button.pack(side=tk.LEFT)

        add_rule_button = tk.Button(footer, text="Add Rule")
        add_rule_button.pack(side=tk.RIGHT, padx=(0, 10))

        back_button = tk.Button(footer, text="Back")
        back_button.pack(side=tk.RIGHT)

        self.window.mainloop()

    def close(self):
        if self.window is not None:
            self.window.destroy()
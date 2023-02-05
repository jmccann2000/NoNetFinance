import PySimpleGUI as Gui
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def print_category_value(pct, all_vals):
    absolute = int(np.round(pct / 100. * np.sum(all_vals)))
    return "{:.1f}% (${:d})".format(pct, absolute)


def create_pie(panda):
    categories = set(panda["Category"])
    rem_categories = set()
    data = []
    for cat in categories:
        cat_total = panda.loc[panda["Category"] == cat, "Cost"].sum()
        if cat_total != 0:
            data.append(cat_total)
        else:
            rem_categories.add(cat)

    for cat in rem_categories:
        categories.remove(cat)

    explode_vals = np.full(
                      shape=len(data),
                      fill_value=0.2,
                      dtype=np.float
                    )
    figure = plt.figure()
    plt.pie(data, labels=categories, autopct=lambda pct: print_category_value(pct, data), explode=explode_vals)
    return figure


def create(panda):
    headers = panda.columns.values.tolist()
    data_table = [
        [Gui.Table(values=panda.values.tolist(), headings=headers, auto_size_columns=True, key="-DATATABLE-")],
        [Gui.Button("Exit")]
    ]
    total_spent = panda.loc[:, "Cost"].sum()
    stat_menu = [
        [Gui.Text("Total Spent:"), Gui.Text("$" + str(total_spent))],
        [Gui.Canvas(key='-PIE-')]
    ]
    layout = [
        [Gui.Column(data_table), Gui.VerticalSeparator(), Gui.Column(stat_menu)]
    ]
    window = Gui.Window("Spending Overview",
                        layout,
                        finalize=True)
    pie_chart = create_pie(panda)
    draw_figure(window['-PIE-'].TKCanvas, pie_chart)

    while True:
        event, values = window.read()
        if event == "Exit" or event == Gui.WIN_CLOSED:
            break

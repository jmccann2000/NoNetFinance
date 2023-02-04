import PySimpleGUI as sg
import main_splash
import pandas as pd

def regulate_data(data, header, desc_col_label, date_col_label, category_col_label, cost_col_label):
    desc_col = data[header.index(desc_col_label)]
    date_col = data[header.index( date_col_label)]
    category_col = data[header.index(category_col_label)]
    print(header.index(category_col_label))
    cost_col = data[:]
    print(cost_col)

def create(filename, header, data):
    data_table = [
        [sg.Table(values=data, headings=header, auto_size_columns=True, key = "-DATATABLE-")],
        [sg.Text("Select description column:"), sg.DropDown(values=header, key="-DESC-")],
        [sg.Text("Select date column:"), sg.DropDown(values=header, key="-DATE-")],
        [sg.Text("Select category column:"), sg.DropDown(values=header, key="-CATEGORY-")],
        [sg.Text("Select cost column:"), sg.DropDown(values=header, key="-COST-")],
        [sg.Button("Exit"), sg.Button("Continue")]
    ]
    window = sg.Window(filename, data_table)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Continue":
            required_data_filled = values["-DESC-"] and values["-DATE-"] and values["-CATEGORY-"] and values["-COST-"]
            if required_data_filled:
                normal_data = regulate_data(data, header, values["-DESC-"], values["-DATE-"], values["-CATEGORY-"], values["-COST-"])
                main_splash.create(normal_data)
    window.close()
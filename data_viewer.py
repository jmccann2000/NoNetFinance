import PySimpleGUI as sg

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
                break
    window.close()
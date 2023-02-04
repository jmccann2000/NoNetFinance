import PySimpleGUI as sg

def create(filename, header, data):
    data_table = [
        [sg.Table(values=data, headings=header, auto_size_columns=True, key = "-DATATABLE-")],
        [sg.Button("Exit")]
    ]
    window = sg.Window(filename, data_table)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
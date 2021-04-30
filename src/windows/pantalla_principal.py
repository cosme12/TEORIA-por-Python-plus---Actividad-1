import PySimpleGUI as sg


def build():
    """
    Construye la ventana del menú del juego
    """
    padding = ((5,5),(10,30))
    size_boton = (30,3)
    fuente = ("Arial", 20)
    fuente2 = ("Arial", 12)

    texto1 = "El primer dataset corresponde a todos los aterrizajes y despegues del 2021"
    texto2 = "El segundo dataset contiene una lista de todos los aeropuertos habilitados del pais"

    layout = [
        [sg.Text("¿Qué datos analizamos?", pad=padding, font=fuente)],
        [sg.Text(texto1)],
        [sg.Text(texto2, pad=padding)],
        [sg.Button("Aterrizajes y despegues 2021", key="-B_ATERRIZAJE-", size=size_boton, font=fuente2)],
        [sg.Button("Aeropuetos 2021", key="-B_AEROPUERTOS-", size=size_boton, pad=padding, font=fuente2)],
        [sg.Button("Salir", key="-SALIR-", size=size_boton, pad=padding)]
    ]


    board = sg.Window('Actividad 1 x Python Plus - TEORIA',
        element_justification = "center", no_titlebar=True, grab_anywhere=True).Layout(layout)

    return board

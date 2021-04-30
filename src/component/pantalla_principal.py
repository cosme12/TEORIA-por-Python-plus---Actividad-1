import PySimpleGUI as sg
from src.windows import pantalla_principal
from src.handlers import aeropuertos
from src.handlers import aterrizajes


def start():
    """
    Lanza la ejecución de la ventana del menú
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    mensaje1 = "Se guardaron en un json todos los aterrizajes de aeronaves privadas entre aeropuertos distintos a ezeiza y que sean vuelos de cabotaje realizados a la 1am con aeronaves distintas a BEECHCRAFT"
    mensaje2 = "Se guardaron en un json todos los aeropuertos donde el trafico es nacional, pertenecen al estado y se encuentran a una elevacion de entre 500 y 700 metros"

    window = pantalla_principal.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit") or event in ["-exit-", "-SALIR-"]:
            break

        elif event == "-B_ATERRIZAJE-":
            aterrizajes.procesar()
            sg.popup(mensaje1, title="Exito")
        elif event == "-B_AEROPUERTOS-":
            aeropuertos.procesar()
            sg.popup(mensaje2, title="Exito")

    return window

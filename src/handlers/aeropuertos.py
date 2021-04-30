import csv
import json


def procesar():
    """
    Guarda en un json todos los aeropuertos donde trafico=Nacional y condicion=PUBLICO 
    y 500<elev<700
    """
    archivo = open("src/recursos/aeropuertos_detalle.csv", "r", encoding="utf8")
    csvreader = csv.reader(archivo, delimiter=';')

    encabezado, datos = next(csvreader), list(csvreader) 
    archivo.close()

    encabezado[0] = encabezado[0][1:]  # Elimina caracter de inicio de linea

    # Devuelve todos los aeropuertos donde trafico=Nacional y condicion=PUBLICO y 500<elev<700
    aeropuertos_nacionales = list(filter(lambda x: x[18]=="Nacional" and x[13]=='PUBLICO' and 500<float(x[8])<700, datos))

    datos_json = []
    for a in aeropuertos_nacionales:
        datos_dict = {}
        for i in range(len(encabezado)):
            datos_dict[encabezado[i]] = a[i]
        datos_json.append(datos_dict)

    aeropuetos_JSON = json.dumps(datos_json)

    with open("aeropuertos.json", "w", encoding="utf8") as archivoJSON:
        archivoJSON.write(aeropuetos_JSON)


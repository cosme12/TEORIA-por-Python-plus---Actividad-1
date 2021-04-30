import csv
import json



def procesar():
    """
    Guarda en un json todos los aterrizajes de aeronaves privadas entre aeropuertos distintos a ezeiza 
    y que sean vuelos de cabotaje realizados a la 1am con aeronaves distintas a BEECHCRAFT
    Informacion adicional de la cabecera:

    https://es.wikipedia.org/wiki/C%C3%B3digo_de_aeropuertos_de_OACI

    """   
    archivo = open("src/recursos/aterrizajes-y-despegues-2021.csv", "r", encoding="utf8")
    csvreader = csv.reader(archivo, delimiter=',')

    encabezado, datos = next(csvreader), list(csvreader) 
    archivo.close()
    
    # Devuelve todos los aterrizajes de aeronaves privadas entre aeropuertos distintos a ezeiza y que
    # sean vuelos de cabotaje realizados a la 1am con aeronaves distintas a BEECHCRAFT
    aterrizaje = list(filter(lambda x: x[1]=="1" and x[2]=="Vuelo Privado con Matrícula Nacional" 
        and x[3]=="Cabotaje" and x[4]=="Aterrizaje" and x[5]!="SAEZ" and x[6]!="SAEZ"
        and x[7]=="N/A" and "BEECHCRAFT" not in x[8], datos))

    datos_json = []
    for a in aterrizaje:
        datos_dict = {}
        for i in range(len(encabezado)):
            datos_dict[encabezado[i]] = a[i]
        datos_json.append(datos_dict)

    aterrizajes_JSON = json.dumps(datos_json)

    with open("aterrizajes-y-despegues-2021.json", "w", encoding="utf8") as archivoJSON:
        archivoJSON.write(aterrizajes_JSON)


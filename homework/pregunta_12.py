"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    df = open("files/input/data.csv", "r").readlines()
    df = [z.replace('\n', '')for z in df]
    df = [z.split("\t")for z in df]
    data = []
    for i in df:
        col_1 = i[0]
        contador=0
        for j in i[4].split(","):
            col_5 = int(j.split(":")[1])
            contador += col_5
        data.append((col_1, contador))

    tuple_data = sorted(data , key=lambda x: x[0])

    diccionario = {}
    for key, value in tuple_data:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value
  
    return diccionario

if __name__ == "__main__":
    print(pregunta_12())

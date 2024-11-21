"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    df = open("files/input/data.csv", "r").readlines()
    df = [z.replace('\n', '')for z in df]
    df = [z.split("\t")for z in df]
    data = []
    for row in df:
        col_2 = int(row[1])
        for i in row[3].split(","):
            data.append((i, col_2))
    tuple_data = sorted(data , key=lambda x: x[0])

    diccionario = {}
    for key, value in tuple_data:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value
  
    return diccionario


if __name__ == "__main__":
    print(pregunta_11())
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    df = open("files/input/data.csv", "r").readlines()
    df = [z.replace('\n', '')for z in df]
    df = [z.split("\t")for z in df]
    data=[]
    for i in range(len(df)):
        data.append(df[i][0])
    tuple_data = [(i, item) for i, item in enumerate(data)]
    tuple_data = [(word, 1) for _, text_line in tuple_data  for word in text_line.split()]
    tuple_data = sorted(tuple_data , key=lambda x: x[0])
    diccionario = {}
    for key, value in tuple_data:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value
    return list(diccionario.items())

if __name__ == "__main__":
    print(pregunta_02())


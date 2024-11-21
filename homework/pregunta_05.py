"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    df = open("files/input/data.csv", "r").readlines()
    df = [z.replace('\n', '')for z in df]
    df = [z.split("\t")for z in df]
    data = []
    for i in range(len(df)):
        tuple = (df[i][0], df[i][1])
        data.append(tuple)
    tuple_data = sorted(data , key=lambda x: x[0])
    diccionario = {}
    for key, value in tuple_data:
        if key not in diccionario:
            diccionario[key] = []
            diccionario[key].append(int(value))
        else:
            diccionario[key].append(int(value))
    for key, value in diccionario.items():
        diccionario[key] = (max(value), min(value))

    tuple_final = []
    for key, value in diccionario.items():
        tuple_final.append((key, value[0], value[1])) 
    return tuple_final 



if __name__ == "__main__":
    print(pregunta_05())


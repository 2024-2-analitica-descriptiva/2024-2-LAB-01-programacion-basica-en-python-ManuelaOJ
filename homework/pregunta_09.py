"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    df = open("files/input/data.csv", "r").readlines()
    df = [z.replace('\n', '')for z in df]
    df = [z.split("\t")for z in df]
    data = []
    for row in df:
        list_items = row[4].split(",")  
        for item in list_items:
            data.append(item.split(":")[0])  
    tuple_data = [(i, item) for i, item in enumerate(data)]
    tuple_data = [(word, 1) for _, text_line in tuple_data for word in text_line.split()]
    tuple_data = sorted(tuple_data , key=lambda x: x[0])

    diccionario = {}
    for key, value in tuple_data:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value
  
    return diccionario


if __name__ == "__main__":
    print(pregunta_09())
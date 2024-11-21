"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    df = open("files/input/data.csv", "r").readlines()
    df = [z.replace('\n', '')for z in df]
    df = [z.split("\t")for z in df]
    data = []
    for i in range(len(df)):
        list = df[i][4].split(",")
        for j in list :
            data.append((j.split(":")[0], j.split(":")[1]))
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
        tuple_final.append((key, value[1], value[0])) 
    return tuple_final 



if __name__ == "__main__":
    print(pregunta_06())


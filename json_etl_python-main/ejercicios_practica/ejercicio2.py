# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    repuesta = requests.get(url)
    datos = repuesta.json()

    numeros_repetidos = []
    x = []
    for d in datos:
        if d["userId"] in numeros_repetidos:
            continue
        else:
            x.append(str(d["userId"]))
            numeros_repetidos.append(d["userId"])
    
    y = []
    dic_y = {"cont_1": 0, "cont_2": 0, "cont_3": 0, "cont_4": 0, "cont_5": 0,
            "cont_6": 0, "cont_7": 0, "cont_8": 0, "cont_9": 0, "cont_10": 0}
    for d in datos:
        if d["userId"] == 1:
            if d["completed"] == True:
                dic_y["cont_1"] += 1
        elif d["userId"] == 2:
            if d["completed"] == True:
                dic_y["cont_2"] += 1
        elif d["userId"] == 3:
            if d["completed"] == True:
                dic_y["cont_3"] += 1
        elif d["userId"] == 4:
            if d["completed"] == True:
                dic_y["cont_4"] += 1
        elif d["userId"] == 5:
            if d["completed"] == True:
                dic_y["cont_5"] += 1
        elif d["userId"] == 6:
            if d["completed"] == True:
                dic_y["cont_6"] += 1
        elif d["userId"] == 7:
            if d["completed"] == True:
                dic_y["cont_7"] += 1
        elif d["userId"] == 8:
            if d["completed"] == True:
                dic_y["cont_8"] += 1
        elif d["userId"] == 9:
            if d["completed"] == True:
                dic_y["cont_9"] += 1
        elif d["userId"] == 10:
            if d["completed"] == True:
                dic_y["cont_10"] += 1

    for v in dic_y.values():
        y.append(v)
    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.bar(x, y, label = "titulos completados",)
    ax.legend()
    plt.show()
    print("terminamos")
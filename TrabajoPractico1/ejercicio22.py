# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.
def usar_la_fuerza(mochila, objetos_sacados=0):

    if len(mochila) == 0: #Caso base: No hay objetos en la mochila.
        return -1

    objeto = mochila.pop(0)  #Elimino el primer objeto de la mochila.
    if objeto == "sable de luz":
        return objetos_sacados

    return usar_la_fuerza(mochila, objetos_sacados + 1)

mochila = ["comida","agua","mapa", "pistola laser", "sable de luz", "ropa"]
objetos_sacados = usar_la_fuerza(mochila)
if objetos_sacados == -1:
    print("No se encontró el sable de luz en la mochila.")
else:
    print(f"Se encontró el sable de luz luego de sacar {objetos_sacados} objetos.")
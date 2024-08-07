# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:

# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.

def usar_la_fuerza(mochila, indice = 0, objetos_sacados = 0, ):
    if indice >= len(mochila):
        print("No se encontro el sable de luz en la mochila.")
        return False, objetos_sacados
    
    if mochila[indice] == "sable de luz":
        print(f"Se encontro el sable de luz en la mochila luego de sacar {objetos_sacados + 1} objetos")
        return True, objetos_sacados + 1
    
    print(f"Sacando objeto: {mochila[indice]}")
    return usar_la_fuerza(mochila, indice + 1, objetos_sacados + 1)

mochila = ["botella de agua", "comida en lata", "brujula", "sable de luz", "kit de primeros auxilios"]
print(usar_la_fuerza(mochila))
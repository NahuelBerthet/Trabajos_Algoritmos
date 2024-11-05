# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;
# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;
# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
# f) Determina cuantos pokemons hay de tipo electrico y acero

from arbol_avl import BinaryTree

arbol_por_nombre= BinaryTree()
arbol_por_numero = BinaryTree()
arbol_por_tipo = BinaryTree()

pokemons = [
    {'numero': 1, 'nombre': 'Bulbasaur', 'tipos': ['Planta', 'Veneno']},
    {'numero': 4, 'nombre': 'Charmander', 'tipos': ['Fuego']},
    {'numero': 7, 'nombre': 'Squirtle', 'tipos': ['Agua']},
    {'numero': 25, 'nombre': 'Pikachu', 'tipos': ['Electrico']},
    {'numero': 39, 'nombre': 'Jigglypuff', 'tipos': ['Normal', 'Hada']},
    {'numero': 52, 'nombre': 'Meowth', 'tipos': ['Normal']},
    {'numero': 63, 'nombre': 'Abra', 'tipos': ['Psiquico']},
    {'numero': 81, 'nombre': 'Magnemite', 'tipos': ['Electrico', 'Acero']},
    {'numero': 104, 'nombre': 'Cubone', 'tipos': ['Tierra']},
    {'numero': 133, 'nombre': 'Eevee', 'tipos': ['Normal']},
    {'numero': 22,'nombre':'Jolteon','tipos':['Electrico']},
    {'numero': 100,'nombre':'Lycanroc','tipos':['Roca']},
    {'numero': 125,'nombre':'Tyrantrum','tipos':['Roca','Dragon']}
]
#Punto a
for pokemon in pokemons:
    arbol_por_nombre.insert_node(pokemon['nombre'],pokemon)
    arbol_por_numero.insert_node(pokemon['numero'],pokemon)
    arbol_por_tipo.insert_node(pokemon['tipos'],pokemon)


#Punto b: Busqueda por nombre y por numero
print('Busqueda por nombre')
arbol_por_nombre.proximity_search('Bul')
print('\n Busqueda por numero')
arbol_por_numero.search(52)

#Punto c:mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
print('\n Nombres de los pokemon segun su tipo')
arbol_por_tipo.proximity_search_tipo('Agua')
arbol_por_tipo.proximity_search_tipo('Fuego')
arbol_por_tipo.proximity_search_tipo('Planta')
arbol_por_tipo.proximity_search_tipo('Electrico')

#Punto d: Mostrar listados
print('\nOrden por numero:')
arbol_por_numero.inorden()
print('\nOrden por nombre:')
arbol_por_nombre.inorden()

# Punto e: Mostrar datos de los pokemones Jolteon, Lycanroc y Tyrantrum
print('\nDatos de los pokemons: Jolteon, Lycanroc y Tyrantrum')
arbol_por_nombre.proximity_search('Jolteon')
arbol_por_nombre.proximity_search('Lycanroc')
arbol_por_nombre.proximity_search('Tyrantrum')


#Punto f: pokemones electrico y acero
print('\nPokemones tipo electrico, acero')
arbol_por_tipo.proximity_search_tipo('Electrico')
arbol_por_tipo.proximity_search_tipo('Acero')
# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer(MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
from arbol_avl import BinaryTree

personajes=[
    {'nombre':'Captain America', 'villano':False},
    {'nombre': 'Factor Strange','villano': False},
    {'nombre': 'Iron Man','villano': False},
    {'nombre': 'Thanos','villano': True},
    {'nombre': 'Black Panther', 'villano':False},
    {'nombre': 'Electro', 'villano':True},
    {'nombre': 'Superman', 'villano':False},
    {'nombre': 'Spider Man' , 'villano':False},
    {'nombre': 'Ant Man', 'villano':False},
    {'nombre': 'Black Adam', 'villano':True},
    {'nombre': 'Trigon', 'villano':True},
    {'nombre': 'Batman', 'villano':False},
    {'nombre': 'Paralax', 'villano':True},
    {'nombre': 'Ares', 'villano':True},
]

tree = BinaryTree()

#Cargar con True o false si son villanos o heroes
for personaje in personajes:
    tree.insert_node(personaje['nombre'], personaje)

#Punto b
print('\nListado Villanos:')
tree.inorden_villanos()

# Punto c
print('\nComienzan con C:')
tree.proximity_search('C')

# Punto d

print('\nCantidad de superheroes: ',tree.contar_super_heroes())

#Punto e
pos = tree.search('Factor Strange')
pos.value = 'Doctor Strange'

#Punto f
print('\nListado orden descendente')
tree.postorden()

#Punto g
arbol_heroes=BinaryTree()
arbol_villanos=BinaryTree()


tree.transferir_nodos(arbol_heroes,arbol_villanos)

print('\nListado orden villanos:')
arbol_villanos.inorden()

print('\nListado orden superheroes')
arbol_heroes.inorden()






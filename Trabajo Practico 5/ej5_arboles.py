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
from arbol import BinaryTree
personajes = [
    {'nombre': "Iron man", 'tipo': True},
    {'nombre': "Carnage", 'tipo': False},
    {'nombre': "Dr Strange", 'tipo': True},
    {'nombre': "Captain America", 'tipo': True},
    {'nombre': "Loki", 'tipo': False},
    {'nombre': "Captain Marvel", 'tipo': True},
    {'nombre': "Thanos", 'tipo': False},
]
tree = BinaryTree()
for personaje in personajes:
    is_hero = False if 'tipo' in personaje else True
    personaje['is_hero'] = is_hero
    tree.insert_node(personaje['nombre'], personaje)


print(tree)

     
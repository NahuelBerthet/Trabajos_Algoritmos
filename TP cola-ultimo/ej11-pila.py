# Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks
from heap import HeapMax

personajes = [
    ("Luke Skywalker", "Tatooine"),
    ("Leia Organa", "Alderaan"),
    ("Han Solo", "Corellia"),
    ("Yoda", "Dagobah"),
    ("Jar Jar Binks", "Naboo"),
    ("Chewbacca", "Kashyyyk"),
    ("Ewok", "Endor"),
]

heap = HeapMax()

# #! Agregar personajes al heap

for personaje in personajes:
    heap.add(personaje)

# #! Buscar los planetas especificos
def personajes_planetas(heap, planetas):
    personajes_en_planetas = []
    for personaje in heap.elements:
        if personaje[1] in planetas:
            personajes_en_planetas.append(personaje)
    return personajes_en_planetas

# #! Buscar Planeta natal
def planeta_natal(heap, nombre):
    for personaje in heap.elements:
        if personaje[0] == nombre:
            return personaje[1]
    return None

# #! Insertar personaje

def insertar_personaje(heap, nuevo_personaje,referente_insertar):
    index = next((i for i, p in enumerate(heap.elements) if p[0] == referente_insertar), None)
    if index is not None:
        heap.elements.insert(index, nuevo_personaje)
        heap.float(index)  
    return heap


# #! Eliminar personaje
def eliminar_despues_de(heap, referente_eliminar):
    index = next((i for i, p in enumerate(heap.elements) if p[0] == referente_eliminar), None)
    if index is not None and index + 1 < len(heap.elements):
        heap.elements.pop(index + 1)
    return heap


# #* Ejecucion Funciones

#Punto A
planetas_buscados = ["Alderaan", "Endor", "Tatooine"]
resultado = personajes_planetas(heap, planetas_buscados)
print("Personajes de Alderaan, Endor y Tatooine:", resultado)

print("-----------------------------------------------------")

#Punto B
luke_planeta = planeta_natal(heap, "Luke Skywalker")
han_planeta = planeta_natal(heap, "Han Solo")
print("Planeta natal de Luke Skywalker:", luke_planeta)
print("Planeta natal de Han Solo:", han_planeta)

print("-----------------------------------------------------")
# Vista previa
print("Personajes antes de insertar: ", heap.elements)

print("-----------------------------------------------------")

# Punto C
nuevo_personaje = ("Darth Vader", "Tatooine")
heap_actualizado = insertar_personaje(heap, nuevo_personaje, "Yoda")
print("Personajes después de insertar:", heap_actualizado.elements)

print("-----------------------------------------------------")

#Punto D

heap_final = eliminar_despues_de(heap_actualizado, "Jar Jar Binks")
print("Personajes después de eliminar:", heap_final.elements)

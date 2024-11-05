from grafo import Graph

personajes = [
    "Yoda",
    "Luke Skywalker",
    "Darth Vader",
    "Boba Fett",
    "C-3PO",
    "Leia Organa",
    "Rey",
    "Kylo Ren",
    "Chewbacca",
    "Han Solo",
    "R2-D2",
    "BB-8",
    "Emperor Palpatine",
    "Obi-Wan Kenobi",
    "Lando Calrissian"
]
grafo=Graph(dirigido=False)
for personaje in personajes:
    grafo.insert_vertice(personaje)
    

aristas = [
    ('Luke Skywalker', 'Darth Vader', 4),
    ('Luke Skywalker', 'Yoda', 3),
    ('Luke Skywalker', 'Leia', 5),
    ('Luke Skywalker', 'Han Solo', 5),
    ('Leia', 'Han Solo', 5),
    ('Leia', 'C-3PO', 5),
    ('Han Solo', 'Chewbacca', 5),
    ('R2-D2', 'C-3PO', 7),
    ('Rey', 'Kylo Ren', 3),
    ('Rey', 'Leia', 2),
    ('Rey', 'BB-8', 3),
    ('Darth Vader', 'Yoda', 9),
    ('Yoda', 'R2-D2', 3),
    ('BB-8', 'R2-D2', 1),
]

for origen,destino,peso in aristas:
    grafo.insert_arista(origen,destino,peso)


# Punto b
arbol_expansion_minima = grafo.kruskal(personajes[0]) 
print("Árbol de expansión mínima:")
print(arbol_expansion_minima)

yoda_en_arbol = any("Yoda" in arista for arista in arbol_expansion_minima)

if yoda_en_arbol:
    print('\nSe encuentra Yoda')
else:
    print('\nNo se encuentra Yoda')

# Punto c
episodios_compartidos = 0
nombre_personajes = ()

for nodo in grafo.elements:
    for arista in nodo['aristas']:
        peso = arista['peso']
        origen = nodo['value']
        destino = arista['value']
        
        if peso > episodios_compartidos:
            episodios_compartidos = peso
            nombre_personajes = (origen, destino)

print("\nNumero maximo de episodios compartidos:", episodios_compartidos)
print("Los personajes son:", nombre_personajes)
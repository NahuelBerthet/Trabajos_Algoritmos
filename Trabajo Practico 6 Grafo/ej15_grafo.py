# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectonicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectonica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectonicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.
from grafo import Graph

maravillas = [
    {"nombre": "Gran Muralla China", "pais": ["China"], "tipo": "arquitectonica"},
    {"nombre": "Petra", "pais": ["Jordania"], "tipo": "arquitectonica"},
    {"nombre": "Cristo Redentor", "pais": ["Brasil"], "tipo": "arquitectonica"},
    {"nombre": "Machu Picchu", "pais": ["Peru"], "tipo": "arquitectonica"},
    {"nombre": "Chichen Itza", "pais": ["México"], "tipo": "arquitectonica"},
    {"nombre": "Coliseo de Roma", "pais": ["Italia"], "tipo": "arquitectonica"},
    {"nombre": "Taj Mahal", "pais": ["India"], "tipo": "arquitectonica"},
    {"nombre": "Amazonas", "pais": ["Brasil", "Colombia", "Peru", "Venezuela"], "tipo": "natural"},
    {"nombre": "Bahía de Ha-Long", "pais": ["Vietnam"], "tipo": "natural"},
    {"nombre": "Cataratas del Iguazú", "pais": ["Argentina", "Brasil"], "tipo": "natural"},
    {"nombre": "Isla Jeju", "pais": ["Corea del Sur"], "tipo": "natural"},
    {"nombre": "Montaña de la Mesa", "pais": ["Sudáfrica"], "tipo": "natural"},
    {"nombre": "Parque Nacional de Komodo", "pais": ["Indonesia"], "tipo": "natural"},
    {"nombre": "Río subterráneo de Puerto Princesa", "pais": ["Filipinas"], "tipo": "natural"}
]

grafo = Graph(dirigido=False)

for maravilla in maravillas:
    grafo.insert_vertice(maravilla['nombre'],maravilla)


distancias = [
    ["Gran Muralla China", "Petra", 5000],
    ["Gran Muralla China", "Cristo Redentor", 17000],
    ["Petra", "Cristo Redentor", 12000],
    ["Cristo Redentor", "Machu Picchu", 3500],
    ["Machu Picchu", "Chichen Itza", 4000],
    ["Chichen Itza", "Coliseo de Roma", 10000],
    ["Coliseo de Roma", "Taj Mahal", 6500],
    # Distancias entre maravillas naturales
    ["Amazonas", "Bahía de Ha-Long", 17000],
    ["Amazonas", "Cataratas del Iguazú", 1000],
    ["Cataratas del Iguazú", "Isla Jeju", 18000],
    ["Isla Jeju", "Montaña de la Mesa", 13000],
    ["Montaña de la Mesa", "Parque Nacional de Komodo", 7000],
    ["Parque Nacional de Komodo", "Río subterráneo de Puerto Princesa", 2000]
]

for origen, destino,peso in distancias:
    grafo.insert_arista(origen,destino,peso)

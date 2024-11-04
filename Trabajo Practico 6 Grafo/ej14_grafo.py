# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
from grafo import Graph
# Punto a
ambientes= ['cocina','comedor','cochera','quincho','baño 1','baño 2','habitacion 1','habitacion 2','sala de estar', 'terraza','patio']

grafo = Graph(dirigido=False)
for ambiente in ambientes:
    nodo = {
        'value': ambiente,
        'aristas': [],
        }
    grafo.insert_vertice(ambiente)

distancias = [
    ["cocina", "comedor", 5],
    ["cocina", "baño 1", 3],
    ["cocina", "habitación 1", 8],
    ["comedor", "sala de estar", 4],
    ["comedor", "terraza", 6],
    ["comedor", "baño 2", 7],
    ["cochera", "quincho", 10],
    ["cochera", "patio", 15],
    ["cochera", "habitacion 2", 22],
    ["quincho", "patio", 12],
    ["quincho","sala de estar", 30],
    ["quincho","terraza", 25],
    ["baño 1", "baño 2", 15],
    ["baño 1", "habitación 2", 4],
    ["baño 1", "habitacion 1", 7],
    ["baño 1", "quincho", 30],
    ["baño 2", "cocina", 12],
    ["habitacion 1", "cochera", 11],
    ["habitacion 1", "habitacion 2", 3],
    ["habitacion 2", "terraza", 7],
    ["sala de estar", "patio", 10],
    ["terraza", "patio", 5],
    ["terraza", "terraza", 20],
]

# Punto b
for origen, destino, peso in distancias:
    grafo.insert_arista(origen, destino, peso)

# Punto c : Camino mas corto

camino = grafo.dijkstra('habitacion 1')
destino = 'sala de estar'
peso_total = None
camino_completo = []
while camino.size() > 0:
    value = camino.pop()
    if value[1][0] == destino:
        if peso_total is None:
            peso_total = value[0]
        camino_completo.append(value[1][0])
        destino = value[1][2]
camino_completo.reverse()
# print(f'el camino mas corto es: {'-'.join(camino_completo)}')
print(f'Desde el router al SmartTV hay {peso_total} metros')

# grafo.mark_as_not_visited()
# grafo.amplitude_show('cocina')
# print(grafo.kruskal('cocina'))

# Punto d: sumatoria de pesos(metros)
new_grafo= grafo.kruskal('cocina')
def calcular_peso_total(bosque):
    peso_total = 0
    for arbol in bosque:
        aristas = arbol.split(';')
        for arista in aristas:
            peso = arista.split('-')
            if len(peso) >= 0:
                peso = int(peso[-1])
                peso_total += peso
    return peso_total

print('La cantidad de metros para conectar todos los ambientes son:',calcular_peso_total(new_grafo))


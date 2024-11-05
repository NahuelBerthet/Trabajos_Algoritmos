from cola import Queue
from heap import HeapMin
from pila import Stack

class Graph:
    def __init__(self, dirigido=True):
        self.elements = []
        self.dirigido = dirigido

    def show_graph(self):
        print()
        print("nodos")
        for index, nodo in enumerate(self.elements):
            print(nodo['value'])
            print(f"    aristas")
            for second_index, second_element in enumerate(nodo['aristas']):
                print(f'    destino {second_element['value']} peso: {second_element['peso']}')
        print()

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index

    def search_arista(self, vertice_value, value):
        pos_origen = self.search(vertice_value)
        if pos_origen is not None:
            for index, element in enumerate(self.elements[pos_origen]['aristas']):
                if element['value'] == value:
                    return pos_origen, index

    def insert_vertice(self, value, other_value=None):
        nodo = {
        'value': value,
        'aristas': [],
        'visitado': False,
        'other_value': other_value
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            # print(origen, destino)
            arista = {
                'value': destino,
                'peso': peso
            }
            self.elements[pos_origen]['aristas'].append(arista)
            if not self.dirigido:
                arista = {
                    'value': origen,
                    'peso': peso
                }
                self.elements[pos_destino]['aristas'].append(arista)

    
    def delete_arista(self, origen, destino):
        result = self.search_arista(origen, destino)
        if result:
            pos_vertice, pos_arista = result
            value = self.elements[pos_vertice]['aristas'].pop(pos_arista)
            if not self.dirigido:
                result = self.search_arista(destino, origen)
                if result:
                    pos_vertice, pos_arista = result
                    self.elements[pos_vertice]['aristas'].pop(pos_arista)
            return value
    
    def delete_vertice(self, value):
        pos_vertice = self.search(value)
        if pos_vertice is not None:
            delete_value = self.elements.pop(pos_vertice)
            for nodo in self.elements:
                self.delete_arista(nodo['value'], value)
            return delete_value
    
    def mark_as_not_visited(self):
        for nodo in self.elements:
            nodo['visitado'] = False

    def deep_show(self, origin):
        def __deep_show(graph, origin):
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    print(graph.elements[pos_vertice]['value'])
                    adyacentes = graph.elements[pos_vertice]['aristas']
                    for adyacente in adyacentes:
                        __deep_show(graph, adyacente['value'])
        
        self.mark_as_not_visited()
        __deep_show(self, origin)

    def amplitude_show(self, origin):
        self.mark_as_not_visited()
        cola = Queue()
        pos_vertice = self.search(origin)
        if pos_vertice is not None:
            if not self.elements[pos_vertice]['visitado']:
                cola.arrive(self.elements[pos_vertice])
                while cola.size() > 0:
                    nodo = cola.attention()
                    nodo['visitado'] = True
                    print(nodo['value'])
                    adyacentes = nodo['aristas']
                    for adyacente in adyacentes:
                        pos_adyaecnte = self.search(adyacente['value'])
                        if not self.elements[pos_adyaecnte]['visitado']:
                            cola.arrive(self.elements[pos_adyaecnte])
    
    def exist_path(self, origen, destino):
        def __exist_path(graph, origin, destino):
            result = False
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    if graph.elements[pos_vertice]['value'] == destino:
                        return True
                    else:
                        adyacentes = graph.elements[pos_vertice]['aristas']
                        for adyacente in adyacentes:
                            result = __exist_path(graph, adyacente['value'], destino)
                            if result:
                                break
            return result
        
        self.mark_as_not_visited()
        result = __exist_path(self, origen, destino)
        return result

    def dijkstra(self, origen):
        from math import inf
        no_visitados = HeapMin()
        camino = Stack()
        for nodo in self.elements:
            distancia = 0 if nodo['value'] == origen else inf
            no_visitados.arrive([nodo['value'], nodo, None], distancia)
        while len(no_visitados.elements) > 0:
            node = no_visitados.atention()
            costo_nodo_actual = node[0]
            camino.push(node)
            adjacentes = node[1][1]['aristas']
            # print(costo_nodo_actual, adjacentes)
            for adjacente in adjacentes:
                pos = no_visitados.search(adjacente['value'])
                if pos is not None:
                    if costo_nodo_actual + adjacente['peso'] < no_visitados.elements[pos][0]:
                        no_visitados.elements[pos][1][2] = node[1][0]
                        no_visitados.change_proirity(pos, costo_nodo_actual + adjacente['peso'])
        return camino

    def kruskal(self, origen):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                # print(buscado, arbol)
                if buscado in arbol:
                    return index

        bosque = []
        aristas = HeapMin()
        for nodo in self.elements:
            bosque.append(nodo['value'])
            adjacentes = nodo['aristas']
            for adjacente in adjacentes:
                aristas.arrive([nodo['value'], adjacente['value']], adjacente['peso'])

        # print(aristas.elements)
        while len(bosque) > 1 and len(aristas.elements) > 0:
            arista = aristas.atention()
            # print(bosque)
            # print(arista[1][0], arista[1][1])
            # print(arista)
            origen = buscar_en_bosque(bosque, arista[1][0])
            destino = buscar_en_bosque(bosque, arista[1][1])
            # print(origen, destino)
            if origen is not None and destino is not None:
                if origen != destino:
                    if origen > destino:
                        vertice_ori = bosque.pop(origen)
                        vertice_des = bosque.pop(destino)
                    else:
                        vertice_des = bosque.pop(destino)
                        vertice_ori = bosque.pop(origen)

                    if '-' not in vertice_ori and '-' not in vertice_des:
                        bosque.append(f'{vertice_ori}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_des:
                        bosque.append(vertice_ori+';'+f'{arista[1][0]}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_ori:
                        bosque.append(vertice_des+';'+f'{vertice_ori}-{arista[1][1]}-{arista[0]}')
                    else:
                        bosque.append(vertice_ori+';'+vertice_des+';'+f'{arista[1][0]}-{arista[1][1]}-{arista[0]}')
        return bosque
    
    def kruskal_por_tipo(self, tipo):
            def buscar_en_bosque(bosque, buscado):
                for index, arbol in enumerate(bosque):
                    if buscado in arbol:
                        return index

            bosque = []
            aristas = HeapMin()

            for nodo in self.elements:
                if nodo['other_value']['tipo'] == tipo:
                    bosque.append([nodo['value']])
                    for adjacente in nodo['aristas']:
                        if self.elements[self.search(adjacente['value'])]['other_value']['tipo'] == tipo:
                            aristas.arrive([nodo['value'], adjacente['value']], adjacente['peso'])

            aux = []  

            while len(bosque) > 1 and len(aristas.elements) > 0:
                arista = aristas.atention()
                origen = buscar_en_bosque(bosque, arista[1][0])
                destino = buscar_en_bosque(bosque, arista[1][1])

                if origen is not None and destino is not None and origen != destino:
                    aux.append(arista)
                    bosque[origen].extend(bosque.pop(destino))

            return aux

    def get_paises_con_ambas_maravillas(self):
        arquitectonicas = set()
        naturales = set()

        for nodo in self.elements:
            tipo = nodo['other_value']['tipo']
            paises = nodo['other_value']['pais']
            if tipo == 'arquitectonica':
                arquitectonicas.update(paises)
            elif tipo == 'natural':
                naturales.update(paises)

        paises_con_ambas = arquitectonicas.intersection(naturales)
        return paises_con_ambas
    
    def pais_con_multiples_maravillas_mismo_tipo(self):
        maravillas_por_pais_y_tipo = {}

        for nodo in self.elements:
            tipo = nodo['other_value']['tipo']
            paises = nodo['other_value']['pais']

            for pais in paises:
                if pais not in maravillas_por_pais_y_tipo:
                    maravillas_por_pais_y_tipo[pais] = {'arquitectonica': 0, 'natural': 0}
                maravillas_por_pais_y_tipo[pais][tipo] += 1

        paises_multiples_maravillas = {pais for pais, tipos in maravillas_por_pais_y_tipo.items()
            if tipos['arquitectonica'] > 1 or tipos['natural'] > 1}
        return paises_multiples_maravillas

# Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
# que contemple las siguientes actividades: 
# a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
# tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
# b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
# c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, pokemon):
        index = self.hash_function(key)
        self.table[index].append(pokemon)

    def search(self, key):
        index = self.hash_function(key)
        return self.table[index]

def hash_numero(numero):
    return int(str(numero)[-1])

def hash_nivel(nivel):
    return nivel // 10


tabla_tipo = HashTable(10)  
tabla_numero = HashTable(10)  
tabla_nivel = HashTable(10)  

# Lista de Pokémons
pokemons = [
    [1, 'Bulbasaur', ['Planta', 'Veneno'], 5],
    [4, 'Charmander', ['Fuego'], 8],
    [7, 'Squirtle', ['Agua'], 70],
    [25, 'Pikachu', ['Electrico'], 10],
    [39, 'Jigglypuff', ['Normal', 'Hada'], 4],
    [52, 'Meowth', ['Normal'], 61],
    [63, 'Abra', ['Psiquico'], 13],
    [81, 'Magnemite', ['Electrico', 'Acero'], 9],
    [104, 'Cubone', ['Tierra'], 81],
    [133, 'Eevee', ['Normal'], 33]
]

# Función para cargar Pokémons
def cargar_pokemon(numero, nombre, tipos, nivel):
    pokemon = [numero, nombre, tipos, nivel]
    for tipo in tipos:
        tabla_tipo.insert(hash(tipo), pokemon)  
    tabla_numero.insert(hash_numero(numero), pokemon)
    tabla_nivel.insert(hash_nivel(nivel), pokemon)

for pokemon in pokemons:
    cargar_pokemon(*pokemon)


def mostrar_por_numero(numeros):
    for numero in numeros:
        for pokemon in tabla_numero.search(numero):
            print(pokemon)

def mostrar_por_nivel(multiplos):
    for i in range(10):
        for pokemon in tabla_nivel.search(i):
            if any(pokemon[3] % multiplo == 0 for multiplo in multiplos):
                print(pokemon)
                    

# Función para mostrar Pokémons de tipos específicos
def mostrar_por_tipo(tipos_especificos):
    pokemones_mostrados = []
    for tipo in tipos_especificos:
        for pokemon in tabla_tipo.search(hash(tipo)):
            if pokemon[0] not in pokemones_mostrados:  
                print(pokemon)
                pokemones_mostrados.append(pokemon[0])  

# Llamada a las funciones de muestra con parámetros
print("Pokemones cuyos números terminan en 3, 7 y 9:")
mostrar_por_numero([3, 7, 9])
print("\nPokemones con niveles multiplos de 2, 5 y 10:")
mostrar_por_nivel([2, 5, 10])
print("\nPokemones de tipo Acero, Fuego, Electrico, Hielo:")
tipos_aux = ["Acero", "Fuego", "Electrico", "Hielo"]
mostrar_por_tipo(tipos_aux)

# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
from random import choice
from lista import show_list_list, by_name, search, by_tournament_wins

entrenadores = [
    {"nombre": "Ash Ketchum","torneos_ganados": 7, "batallas_perdidas": 50, "batallas_ganadas": 120},
    {"nombre": "Goh", "torneos_ganados": 2, "batallas_perdidas": 10, "batallas_ganadas": 40},
    {"nombre": "Leon", "torneos_ganados": 10, "batallas_perdidas": 5, "batallas_ganadas": 100},
    {"nombre": "Chloe","torneos_ganados": 1, "batallas_perdidas": 8, "batallas_ganadas": 30},
    {"nombre": "Raihan", "torneos_ganados": 4, "batallas_perdidas": 15, "batallas_ganadas": 60}
]

pokemons = [
    {"nombre": "Pikachu", "nivel": 35, "tipo": "Eléctrico", "subtipo": None},
    {"nombre": "Pikachu", "nivel": 20, "tipo": "Eléctrico", "subtipo": None},
    {"nombre": "Charizard", "nivel": 40, "tipo": "Fuego", "subtipo": "Volador"},
    {"nombre": "Bulbasaur", "nivel": 30, "tipo": "Planta", "subtipo": "Veneno"},
    {"nombre": "Starmie", "nivel": 30,"tipo": "Agua", "subtipo": "Psíquico"},
    {"nombre": "Psyduck", "nivel": 25,"tipo": "Agua", "subtipo": None},
    {"nombre": "Gyarados", "nivel": 35, "tipo": "Agua", "subtipo": "Volador"},
    {"nombre": "Onix", "nivel": 38, "tipo": "Roca", "subtipo": "Tierra"},
    {"nombre": "Geodude","nivel": 28,"tipo": "Roca","subtipo": "Tierra"},
    {"nombre": "Vulpix","nivel": 20,"tipo": "Fuego","subtipo": None},
    {"nombre": "Blastoise","nivel": 50,"tipo": "Agua","subtipo": None},
    {"nombre": "Umbreon","nivel": 45,"tipo": "Siniestro","subtipo": None},
    {"nombre": "Nidoking","nivel": 40,"tipo": "Veneno","subtipo": "Tierra"},
    {"nombre": "Dragonite","nivel": 55,"tipo": "Dragón","subtipo": "Volador"},
    {"nombre": "Aerodactyl","nivel": 52,"tipo": "Roca","subtipo": "Volador"}
]

names = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(names))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('no existe el entrenador')

# lista_entrenadores.sort(key=by_name)
# show_list_list('Entrenadores', 'Pokemons', lista_entrenadores)

# a. Obtener la cantidad de Pokémons de un determinado entrenador
print("----------Cantidad de pokemons de entrenador----------")
def cantidad_pokemons(entrenador_nombre):
    for entrenador in lista_entrenadores:
        if entrenador["nombre"] == entrenador_nombre:
            cantidad = len(lista_entrenadores[pos]['sublist'])
    return cantidad

print("Pokemons del entrenador: ", cantidad_pokemons("Leon"))
# b. listar los entrenadores que hayan ganado más de tres torneos;
print("----------Ganaron mas de tres torneos----------")
for entrenador in entrenadores:
    mas_de_tres_torneos_ganados = []
    if entrenador["torneos_ganados"] > 3:
        mas_de_tres_torneos_ganados.append(entrenador)
        print(f"Nombre: {entrenador['nombre']}, torneos ganados: {entrenador['torneos_ganados']}")

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print("----------Mayor niv Pokemon, Entrenador mas torneos ganados----------")
lista_entrenadores.sort(key= by_tournament_wins)

for entrenador in lista_entrenadores:
    entrenador_mas_exitoso = None
    max_torneos_ganados = -1
    if entrenador['torneos_ganados'] > max_torneos_ganados:
        max_torneos_ganados = entrenador['torneos_ganados']
        entrenador_mas_exitoso = entrenador


for pokemon in entrenador_mas_exitoso['sublist']:
    pokemon_mayor_nivel = None
    max_nivel = -1
    if pokemon['nivel'] > max_nivel:
        max_nivel = pokemon['nivel']
        pokemon_mayor_nivel = pokemon

print(entrenador_mas_exitoso["nombre"],entrenador_mas_exitoso["torneos_ganados"], pokemon_mayor_nivel)

# d. mostrar todos los datos de un entrenador y sus Pokémos;
print("----------Datos de entrenador y sus pokemons----------")
def datos_entrenador(name):
    for entrenador in lista_entrenadores:
        if entrenador["nombre"] == name:

            return entrenador

print(datos_entrenador("Ash Ketchum"))

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print("----------Winrate > 79%----------")
def porcentaje_victorias(entrenador):
    total_batallas = entrenador["batallas_perdidas"] + entrenador["batallas_ganadas"]
    if total_batallas == 0:
        return 0.0
    porcentaje = (entrenador["batallas_ganadas"] / total_batallas) * 100
    return porcentaje

entrenadores_destacados = []

for entrenador in entrenadores:
    if porcentaje_victorias(entrenador) > 79.0:
        entrenadores_destacados.append(entrenador)

for entrenador in entrenadores_destacados:
    print(f"Nombre: {entrenador['nombre']}, Victorias: {porcentaje_victorias(entrenador):.2f}%")

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print("----------Promedio nivel----------")
def promedio_nivel_pokemon(name):
    for entrenador in lista_entrenadores:
        if entrenador['nombre'] == name:
            pokemones = entrenador['sublist']
            if len(pokemones) == 0:
                print(f"{name} no tiene pokémones.")
                return
            total_niveles = sum(pokemon['nivel'] for pokemon in pokemones)
            promedio = total_niveles / len(pokemones)
            return f"El promedio de nivel de los pokemones de {name} es: {promedio:.2f}"
    print(f"No se encontró al entrenador {name}.")

print(promedio_nivel_pokemon("Leon"))

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;

def contar_entrenadores_con_pokemon(name):
    contador = 0
    for entrenador in lista_entrenadores:
        for pokemon in entrenador['sublist']:
            if pokemon['nombre'] == name:
                contador += 1
                break  
    return contador

pokemon_buscado = "Pikachu"
cantidad_entrenadores = contar_entrenadores_con_pokemon(pokemon_buscado)
print(f"{cantidad_entrenadores} entrenador(es) tienen a {pokemon_buscado}.")

# i. mostrar los entrenadores que tienen Pokémons repetidos;

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;

def entrenadores_con_pokemon_especifico(pokemon_especifico):
    entrenadores_con_pokemon = []
    for entrenador in lista_entrenadores:
        for pokemon in entrenador['sublist']:
            if pokemon['nombre'] == "Tyrantrum" or "Terrakion" or "Wingull":
                entrenadores_con_pokemon.append(entrenador['nombre'])
                break 
    if entrenadores_con_pokemon:
        print(f"Los entrenadores que tienen a {pokemon_especifico} son:")
        for nombre_entrenador in entrenadores_con_pokemon:
            print(nombre_entrenador)
    else:
        print(f"Ningún entrenador tiene a {pokemon_especifico}.")

pokemon_especifico = "Tyrantrum"
entrenadores_con_pokemon_especifico(pokemon_especifico)

# k. determinar si un entrenador “X” tiene al Pokémon “Y”

def determinar_entrenador_pokemon(nombre, pokemon_buscado):
    for entrenador in lista_entrenadores:
        entrenador_aux = None
        if nombre == entrenador["nombre"]:
            entrenador_aux = entrenador
    
    for pokemon in entrenador_aux['sublist']:
        pokemon_aux = None
        if pokemon_buscado == pokemon["nombre"]:
            pokemon_aux = pokemon
            print("Datos entrenador y su pokemon")
            print(entrenador_aux)
            print(pokemon_aux)

            
print(determinar_entrenador_pokemon("Leon", "Pikachu"))

from pila import Stack
personajes = [
    {"nombre":"Iron Man", "participaciones": 10},
    {"nombre":"Captain America", "participaciones": 8},
    {"nombre":"Thor", "participaciones": 7},
    {"nombre":"Black Widow", "participaciones": 6},
    {"nombre": "Doctor Strange", "participaciones": 2},
    {"nombre":"Hulk", "participaciones": 5},
    {"nombre":"Hawkeye", "participaciones": 5},
    {"nombre":"Rocket Raccoon", "participaciones": 4},
    {"nombre":"Groot", "participaciones": 4},
    {"nombre": "Drax", "participaciones": 3}
]

personajes_aux = []

# Mostrar si aparece Rocket y Groot
print("----------Posicion personajes----------")
for i in range(len(personajes)):
    if personajes[i]["nombre"] == "Rocket Raccoon":
        posicion_rocket = i + 1
    elif personajes[i]["nombre"] == "Groot":
        posicion_groot = i + 1

print("Rocket Raccoon se encuentra en la posición:", posicion_rocket)
print("Groot se encuentra en la posición:", posicion_groot)

# Personajes con 5 o mas apariciones
print("----------5 o mas apariciones----------")
for i in personajes:
    if i["participaciones"] >= 5:
       personajes_aux.append((i["nombre"], i["participaciones"]))

for i in personajes_aux:
    print(i[0], "aparece en", i[1], "películas.")

# Peliculas en las que participo la Viuda Negra
print("----------Participaciones de la viuda negra----------")
for i in personajes:
    if i["nombre"] == "Black Widow":
       print("Black Widow aparece en: ", i["participaciones"], " peliculas.")

# Personajes que inician con C,D,G
print("----------Inician con C,D,G----------")
letras = {"C", "D", "G"}
for i in personajes:
    if i["nombre"][0] in letras:
        print(i["nombre"])

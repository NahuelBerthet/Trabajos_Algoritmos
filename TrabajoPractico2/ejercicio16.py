# Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de
# las que conocemos su nombre, largo, tripulación y cantidad de pasajeros, desarrollar los algo-
# ritmos necesarios para resolver las actividades detalladas a continuación:

# a. realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de
# las mismas de manera descendente;
# b. mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
# c. determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
# d. indicar cuál es la nave que requiere mayor cantidad de tripulación;
# e. mostrar todas las naves que comienzan con AT;
# f. listar todas las naves que pueden llevar seis o más pasajeros;
# g. mostrar toda la información de la nave más pequeña y la más grande.
from pila import Stack
class Nave:
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

    def __str__(self):
        return f"Nave: {self.nombre}, Largo: {self.largo}, Tripulación: {self.tripulacion}, Pasajeros: {self.pasajeros}"

# Crear una lista de naves
naves = [
    Nave("Halcón Milenario", 34.37, 4, 75),
    Nave("Estrella de la Muerte", 160, 342, 843342),
    Nave("Nave1", 25, 3, 50),
    Nave("AT-AT Walker", 20, 5, 10),
    Nave("AT-ST Walker", 8.6, 2, 0),
    Nave("X-wing", 12.5, 1, 0),
    Nave("Y-wing", 16.8, 1, 0),
    Nave("TIE Fighter", 6.3, 1, 0)
]

# Ordenar las naves por nombre de manera ascendente y por largo de manera descendente
def ordenar_naves(naves):
    naves.sort(key=lambda x: x.nombre)  # Ordenar por nombre ascendente
    naves.sort(key=lambda x: x.largo, reverse=True)  # Ordenar por largo descendente
    return naves

# Mostrar toda la informacion del "Halcón Milenario" y la "Estrella de la Muerte"
def info_naves_especificas(naves):
    for nave in naves:
        if nave.nombre == "Halcón Milenario" or nave.nombre == "Estrella de la Muerte":
            print(nave)

# Determinar las cinco naves con mayor cantidad de pasajeros
def cinco_naves_mas_pasajeros(naves):
    return sorted(naves, key=lambda x: x.pasajeros, reverse=True)[:5]

# Indicar cual es la nave que requiere mayor cantidad de tripulacion
def nave_mayor_tripulacion(naves):
    return max(naves, key=lambda x: x.tripulacion)

# Mostrar todas las naves que comienzan con "AT"
def naves_con_prefijo(naves, prefijo):
    return [nave for nave in naves if nave.nombre.startswith(prefijo)]

# Lista de todas las naves que pueden llevar seis o mas pasajeros
def naves_con_mas_pasajeros(naves, cantidad_pasajeros):
    return [nave for nave in naves if nave.pasajeros >= cantidad_pasajeros]

# Mostrar toda la informacion de la nave más pequenia y la mas grande
def info_naves_extremas(naves):
    naves.sort(key=lambda x: x.largo)  # Ordenar por largo ascendente
    return naves[0], naves[-1]

# Uso de funciones.
naves_ordenadas = ordenar_naves(naves)
print("Listado ordenado por nombre (ascendente) y por largo (descendente):")
for nave in naves_ordenadas:
    print(nave)

print ("-------------------------------------------------")

print("\n Información del Halcón Milenario y la Estrella de la Muerte:")
info_naves_especificas(naves)

print ("-------------------------------------------------")

print("\n Las cinco naves con mayor cantidad de pasajeros:")
cinco_naves = cinco_naves_mas_pasajeros(naves)
for nave in cinco_naves:
    print(nave)

print ("-------------------------------------------------")

print("\nLa nave que requiere mayor cantidad de tripulación:")
print(nave_mayor_tripulacion(naves))

print ("-------------------------------------------------")

print("\nNaves que comienzan con 'AT':")
naves_AT = naves_con_prefijo(naves, "AT")
for nave in naves_AT:
    print(nave)

print ("-------------------------------------------------")

print("\nNaves que pueden llevar seis o más pasajeros:")
naves_seis_pasajeros = naves_con_mas_pasajeros(naves, 6)
for nave in naves_seis_pasajeros:
    print(nave)

# print("\ng. Nave mas pequeña y la más grande:")
# nave_mas_pequenia, nave_mas_grande = info_naves_extremas(naves)
# print("Nave más pequeña:")
# print(nave_mas_pequenia)
# print("\nNave más grande:")
# print(nave_mas_grande)

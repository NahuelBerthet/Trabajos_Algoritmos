# Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
def cantidadDigitos(num):
    if num < 10:
        return 1
    else:
        return 1 + cantidadDigitos(num//10)
print(cantidadDigitos(20))
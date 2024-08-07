# Implementar una función que calcule la suma de todos los números enteros comprendidos
# entre cero y un número entero positivo dado.
def sumaEnteroPositivo(num):
    if num == 0:
        return 0
    else:
        return num + sumaEnteroPositivo(num -1)
    
print(sumaEnteroPositivo(5))

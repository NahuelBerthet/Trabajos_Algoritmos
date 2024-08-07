# Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un
# número dado.

def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(20))
# Para ver la sucesion 
aux = 20
for i in range(aux+1):
    print(fibonacci(i), end= ",")

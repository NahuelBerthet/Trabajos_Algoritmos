#Desarrollar una función que permita convertir un número romano en un número decimal.
def convertirRomano_a_Decimal(num_romano):
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if len(num_romano) == 1: 
        return valores[num_romano]

    if valores[num_romano[0]] < valores[num_romano[1]]:
        return -valores[num_romano[0]] + convertirRomano_a_Decimal(num_romano[1:])
    else:
        return valores[num_romano[0]] + convertirRomano_a_Decimal(num_romano[1:])

numero_romano = 'MMXXIV'
numero_decimal = convertirRomano_a_Decimal(numero_romano)
print(f"{numero_romano} en decimal es: {numero_decimal}")
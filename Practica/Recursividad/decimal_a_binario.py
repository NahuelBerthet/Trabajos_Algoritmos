
def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    elif numero == 1:
        return '1'
    else:
        return decimal_a_binario(numero//2) + str(numero%2)
print(decimal_a_binario(10))
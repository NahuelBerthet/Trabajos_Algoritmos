
def listar_inversamente(lista):
    if len(lista) == 0:
        return "La lista esta vacia"
    else:
        listar_inversamente(lista[1:])
    return print(lista[0])
    
lista = ["a","b","c","d","f","g","d"]
print(listar_inversamente(lista))

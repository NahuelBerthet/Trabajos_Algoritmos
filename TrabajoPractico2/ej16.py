from pila import Stack


def interseccion(stack1, stack2):
    interseccion_stack = Stack()
 
    elementos_stack1 = {}

    # Insertar elementos en stack1
    while stack1.size() > 0:
        element = stack1.pop()
        elementos_stack1[element] = True

    # Buscar elementos de stack2 en stack1
    while stack2.size() > 0:
        element = stack2.pop()
        if element in elementos_stack1:
            interseccion_stack.push(element)

    return interseccion_stack

stack1 = Stack()
stack1.push("Luke Skywalker")
stack1.push("Han Solo")
stack1.push("Leia Organa")

stack2 = Stack()
stack2.push("Han Solo")
stack2.push("Leia Organa")
stack2.push("Rey")

intersect = interseccion(stack1, stack2)
print("Intersección de las pilas:")
while intersect.size() > 0:
    print(intersect.pop())
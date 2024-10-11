# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
from heap import HeapMin

heap = HeapMin()
characters = [
    ("Tony Stark", "Iron Man", "M"),
    ("Steve Rogers", "Capitán América", "M"),
    ("Natasha Romanoff", "Black Widow", "F"),
    ("Carol Danvers", "Capitana Marvel", "F"),
    ("Scott Lang", "Ant-Man", "M"),
    ("Bruce Banner", "Hulk", "M"),
]
heap= HeapMin()
for character in characters:
    heap.add(character)


# #! Determinar nombre de personaje

def determinar_nombre(personaje):
    for character in heap.elements:
        if character[1]== personaje:
            return character[0]
    
print(determinar_nombre('Iron Man'))


# #! Mostrar nombre superheroes femeninos

def superheroes_femeninos(genero):
        aux = []
        for character in heap.elements:
            if character[2]== genero:
                aux.append(character[1])
        return aux

print(superheroes_femeninos("F"))
print(superheroes_femeninos("M"))

# #! Determinar personaje
def determinar_nombre(nombre):
    for character in heap.elements:
        if character[0]== nombre:
            return character[1]
    
print('El nombre de superheroe de Scott Lang es: ',determinar_nombre("Scott Lang"))

# #! Empiezan con S

def empiezan_con_(letra):
    aux =[]
    for character in heap.elements:
        if character[1].startswith(letra) or character[0].startswith(letra):
            aux.append(character)
    return aux

print(empiezan_con_("S"))

# #! Determinar si el personaje se encuentra y mostrar su nombre

def personaje_encontrado_nombre(buscado):
    nombre=[]
    for character in heap.elements:
        if character[0] == buscado:
            nombre.append(character[1])
    return 'Se encuentra en la cola', 'Su nombre de superheroe es: ', nombre


print(personaje_encontrado_nombre('Carol Danvers'))
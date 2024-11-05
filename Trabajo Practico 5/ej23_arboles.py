# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.
from arbol_avl import BinaryTree
Enfrentamientos = [
    {'criatura': 'Ceto', 'derrotado': None, 'descripcion': 'Monstruo marino en la mitología griega, asociado con los océanos y los peligros del mar.', 'capturado': None}, 
    {'criatura': 'Cerda de Cromión', 'derrotado': 'Teseo', 'descripcion': 'Una cerda salvaje y feroz que devastaba la región de Cromión, vencida por Teseo.', 'capturado': None}, 
    {'criatura': 'Tifón', 'derrotado': 'Zeus', 'descripcion': 'Gigante monstruoso, padre de muchos monstruos, considerado el más temible de la mitología griega.', 'capturado': None}, 
    {'criatura': 'Ortro', 'derrotado': 'Heracles', 'descripcion': 'Perro de dos cabezas guardián del ganado de Gerión, asesinado por Heracles.', 'capturado': None}, 
    {'criatura': 'Equidna', 'derrotado': 'Argos Panoptes', 'descripcion': 'Ser mitad mujer y mitad serpiente, madre de numerosos monstruos mitológicos.', 'capturado': None}, 
    {'criatura': 'Toro de Creta', 'derrotado': 'Teseo', 'descripcion': 'Bestia poderosa capturada por Heracles y luego enfrentada por Teseo.', 'capturado': 'Heracles'}, 
    {'criatura': 'Dino', 'derrotado': None, 'descripcion': 'Una de las Grayas, hermanas monstruosas que compartían un solo ojo y un diente.', 'capturado': None}, 
    {'criatura': 'Jabalí de Calidón', 'derrotado': 'Atalanta', 'descripcion': 'Jabalí gigantesco enviado por Artemisa como castigo, cazado en una famosa expedición.', 'capturado': None}, 
    {'criatura': 'Pefredo', 'derrotado': None, 'descripcion': 'Otra de las Grayas, compañera de Dino, compartiendo el ojo y el diente.', 'capturado': None}, 
    {'criatura': 'Carcinos', 'derrotado': None, 'descripcion': 'Un gran cangrejo que ayudó a la Hidra de Lerna en su lucha contra Heracles.', 'capturado': None}, 
    {'criatura': 'Enio', 'derrotado': None, 'descripcion': 'Otra de las Grayas, hermana de Dino y Pefredo, monstruosa y de aspecto envejecido.', 'capturado': None}, 
    {'criatura': 'Gerión', 'derrotado': 'Heracles', 'descripcion': 'Gigante de tres cuerpos que custodiaba un gran rebaño de ganado.', 'capturado': None}, 
    {'criatura': 'Escila', 'derrotado': None, 'descripcion': 'Monstruo marino de múltiples cabezas, que atacaba a los marineros en el estrecho de Mesina.', 'capturado': None}, 
    {'criatura': 'Cloto', 'derrotado': None, 'descripcion': 'Una de las Moiras, diosas del destino, encargada de hilar el hilo de la vida.', 'capturado': None}, 
    {'criatura': 'Caribdis', 'derrotado': None, 'descripcion': 'Monstruo marino que generaba remolinos gigantes, devorando a los marineros.', 'capturado': None}, 
    {'criatura': 'Láquesis', 'derrotado': None, 'descripcion': 'Membra de las Moiras, diosa del destino, asignaba la longitud del hilo de la vida.', 'capturado': None}, 
    {'criatura': 'Euríale', 'derrotado': None, 'descripcion': 'Una de las Gorgonas inmortales, hermana de Medusa y Esteno.', 'capturado': None}, 
    {'criatura': 'Átropos', 'derrotado': None, 'descripcion': 'Otra de las Moiras, quien corta el hilo de la vida, marcando la muerte.', 'capturado': None}, 
    {'criatura': 'Esteno', 'derrotado': None, 'descripcion': 'Hermana inmortal de Medusa, parte de las temibles Gorgonas.', 'capturado': None}, 
    {'criatura': 'Minotauro de Creta', 'derrotado': 'Teseo', 'descripcion': 'Criatura con cuerpo humano y cabeza de toro, encerrado en el laberinto de Creta.', 'capturado': None}, 
    {'criatura': 'Medusa', 'derrotado': 'Perseo', 'descripcion': 'Gorgona mortal con serpientes en la cabeza; su mirada convertía a las personas en piedra.', 'capturado': None}, 
    {'criatura': 'Harpías', 'derrotado': None, 'descripcion': 'Criaturas aladas con rostro de mujer y cuerpo de ave, conocidas por robar comida y atormentar a las personas.', 'capturado': None}, 
    {'criatura': 'Ladón', 'derrotado': 'Heracles', 'descripcion': 'Dragón de múltiples cabezas que custodiaba las manzanas de oro del jardín de las Hespérides.', 'capturado': None}, 
    {'criatura': 'Argos Panoptes', 'derrotado': 'Hermes', 'descripcion': 'Gigante con múltiples ojos por todo el cuerpo, conocido por su vigilancia incansable.', 'capturado': None}, 
    {'criatura': 'Águila del Cáucaso', 'derrotado': None, 'descripcion': 'Águila enviada para devorar el hígado de Prometeo diariamente como castigo.', 'capturado': None}, 
    {'criatura': 'Aves del Estínfalo', 'derrotado': None, 'descripcion': 'Aves con plumas metálicas que lanzaban como flechas, enfrentadas por Heracles.', 'capturado': 'Heracles'}, 
    {'criatura': 'Quimera', 'derrotado': 'Belerofonte', 'descripcion': 'Criatura híbrida con partes de león, cabra y serpiente, vencida por Belerofonte.', 'capturado': None}, 
    {'criatura': 'Talos', 'derrotado': 'Medea', 'descripcion': 'Gigante de bronce que protegía Creta, derrotado por Medea con magia.', 'capturado': None}, 
    {'criatura': 'Hidra de Lerna', 'derrotado': 'Heracles', 'descripcion': 'Serpiente con múltiples cabezas que se regeneraban, vencida por Heracles.', 'capturado': None}, 
    {'criatura': 'Sirenas', 'derrotado': None, 'descripcion': 'Seres con apariencia de mujer y ave, que con su canto hipnotizaban a los marineros.', 'capturado': None}, 
    {'criatura': 'Pitón', 'derrotado': 'Apolo', 'descripcion': 'Serpiente gigante de Delfos vencida por el dios Apolo.', 'capturado': None}, 
    {'criatura': 'Cierva de Cerinea', 'derrotado': None, 'descripcion': 'Cierva sagrada de Artemisa, capturada pero no asesinada por Heracles.', 'capturado': 'Heracles'}, 
    {'criatura': 'Dragón de la Cólquida', 'derrotado': None, 'descripcion': 'Dragón que protegía el Vellocino de Oro en la Cólquida.', 'capturado': None}, 
    {'criatura': 'Basilisco', 'derrotado': None, 'descripcion': 'Serpiente con mirada letal que podía matar o petrificar a quien la mirase.', 'capturado': None}, 
    {'criatura': 'Cerbero', 'derrotado': None, 'descripcion': 'Perro de tres cabezas que custodiaba las puertas del inframundo.', 'capturado': 'Heracles'}, 
    {'criatura': 'Jabalí de Erimanto', 'derrotado': None, 'descripcion': 'Jabalí gigantesco y feroz enfrentado por Heracles como parte de sus trabajos.', 'capturado': 'Heracles'}
]


tree = BinaryTree()

for enfrentamiento in Enfrentamientos:
    tree.insert_node(enfrentamiento['criatura'],enfrentamiento) 

#Punto a
tree.inorden()

#Punto c
print('\nInformacion de talos: \n')
tree.proximity_search_all_info('Talos')

#Punto e
def criaturas_derrotadas_por(value):
    def __criaturas_derrotadas(root):
        if root is not None:
            if root.other_value.get('derrotado') == value:
                print(root.value)
            __criaturas_derrotadas(root.left)
            __criaturas_derrotadas(root.right)

    __criaturas_derrotadas(tree.root)

print('\nDerrotas por Heracles:')
criaturas_derrotadas_por('Heracles')

#Punto f
print('\nCriaturas no derrotadas')
tree.criaturas_no_derrotadas()

#Punto j

tree.delete_node('Basilisco')
tree.delete_node('Sirenas')

#Punto k
aves_stinfalo = tree.search('Aves del Estínfalo')
if aves_stinfalo:
    aves_stinfalo.other_value['derrotado'] = 'Heracles'

#Punto l

ladon = tree.search('Ladón')
if ladon:
    tree.delete_node('Ladón')
    tree.insert_node('Dragón Ladón', ladon.other_value)

#Punto m
tree.by_level()

#Punto n
def criaturas_capturadas_por(value):
    def __criaturas_capturadas(root):
        if root is not None:
            if root.other_value.get('capturado') == value:
                print(root.value)
            __criaturas_capturadas(root.left)
            __criaturas_capturadas(root.right)

    __criaturas_capturadas(tree.root)

print('\nCapturado por Heracles:')
criaturas_capturadas_por('Heracles')
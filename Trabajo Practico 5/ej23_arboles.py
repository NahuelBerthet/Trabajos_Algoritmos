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

Enfrentamientos = [ 
    {'criatura': 'Ceto', 'derrotado': None}, 
    {'criatura': 'Cerda de Cromión', 'derrotado': 'Teseo'}, 
    {'criatura': 'Tifón', 'derrotado': 'Zeus'}, 
    {'criatura': 'Ortro', 'derrotado': 'Heracles'}, 
    {'criatura': 'Equidna', 'derrotado': 'Argos Panoptes'}, 
    {'criatura': 'Toro de Creta', 'derrotado': 'Teseo'}, 
    {'criatura': 'Dino', 'derrotado': None}, 
    {'criatura': 'Jabalí de Calidón', 'derrotado': 'Atalanta'}, 
    {'criatura': 'Pefredo', 'derrotado': None}, 
    {'criatura': 'Carcinos', 'derrotado': None}, 
    {'criatura': 'Enio', 'derrotado': None}, 
    {'criatura': 'Gerión', 'derrotado': 'Heracles'}, 
    {'criatura': 'Escila', 'derrotado': None}, 
    {'criatura': 'Cloto', 'derrotado': None}, 
    {'criatura': 'Caribdis', 'derrotado': None}, 
    {'criatura': 'Láquesis', 'derrotado': None}, 
    {'criatura': 'Euríale', 'derrotado': None}, 
    {'criatura': 'Átropos', 'derrotado': None}, 
    {'criatura': 'Esteno', 'derrotado': None}, 
    {'criatura': 'Minotauro de Creta', 'derrotado': 'Teseo'}, 
    {'criatura': 'Medusa', 'derrotado': 'Perseo'}, 
    {'criatura': 'Harpías', 'derrotado': None}, 
    {'criatura': 'Ladón', 'derrotado': 'Heracles'}, 
    {'criatura': 'Argos Panoptes', 'derrotado': 'Hermes'}, 
    {'criatura': 'Águila del Cáucaso', 'derrotado': None}, 
    {'criatura': 'Aves del Estínfalo', 'derrotado': None}, 
    {'criatura': 'Quimera', 'derrotado': 'Belerofonte'}, 
    {'criatura': 'Talos', 'derrotado': 'Medea'}, 
    {'criatura': 'Hidra de Lerna', 'derrotado': 'Heracles'}, 
    {'criatura': 'Sirenas', 'derrotado': None}, 
    {'criatura': 'Pitón', 'derrotado': 'Apolo'}, 
    {'criatura': 'Cierva de Cerinea', 'derrotado': None}, 
    {'criatura': 'Dragón de la Cólquida', 'derrotado': None}, 
    {'criatura': 'Basilisco', 'derrotado': None}, 
    {'criatura': 'Cerbero', 'derrotado': None}, 
    {'criatura': 'Jabalí de Erimanto', 'derrotado': None}, 
    
]
    
# Listas 
#una lista es una coleccion de elementos que pueden ser de cualquier tipo de dato. se pueden agregar, eliminar o modificar elementos en una lista. las listas son mutables, es decir, se pueden modificar. las listas son ordenadas, es decir, tienen un orden definido. se pueden anidar listas dentro de otras listas.
#las listas se definen con corchetes [ ] y los elementos se separan por comas.
#las listas son mutables, es decir, se pueden modificar. las listas son ordenadas, es decir, tienen un orden definido. se pueden anidar listas dentro de otras listas.


#def (funciones)
#if, elif, else(Sentencias condicionales)
#for, while(bucles)
#class (clases)


lista = [30, True, 3.1415, "El número de Avogadro sí que mola"] #aqui definimos una lista con varios tipos de datos

print(lista) #imprimiendo la lista completa
print(lista[-1]) #imprimiendo el ultimo elemento de la lista que es el 4to 
print(lista[1:3]) #imprimiendo los elementos de la lista desde el 1 al 3 (sin incluir el 3)

lista[2] = "He cambiado este elemento" #aqui modificamos el tercer elemento de la lista

lista[2] = [3, 2, 1]   #aqui modificamos el tercer elemento de la lista y le asignamos una lista como valor
print(lista) #imprimiendo la lista completa

print(len(lista)) #imprimiendo la longitud de la lista 
#el len es una funcion que devuelve la longitud de un objeto. en este caso devuelve la longitud de la lista
#la longitud de la lista es 4 porque tiene 4 elementos

#TUPLAS

tupla = ("la tierra es plana?", True , False)
print(tupla) #imprimiendo la tupla completa

print(tupla[0]) #imprimiendo el primer elemento de la tupla
print(tupla[1])
print(tupla[2])

print(tupla.count(True)) #aqui contamos cuantas veces se repite el valor True en la tupla 
#true es un booleano y se repite 1 vez #un booleano es un tipo de dato que solo puede ser True o False
print(tupla.index(False)) #aqui buscamos el indice del primer elemento que sea False en la tupla
#index es una funcion que devuelve el indice de la primera ocurrencia del valor False en la tupla 

print((1)) #imprimiendo el valor 1
print((1,)) #imprimiendo una tupla con un solo elemento

# CONJUNTOS
print(set())

print(set([5, 2, 5, 1, 1.5]))
print(set((5, 2, 5, 1, 1.5)))
print(set("52511.5"))

conjunto = set([2, 3, 3, 4])
conjunto_2 = set([5, 3, 5, 6])
conjunto_3 = set([4, 2])

print(conjunto)
print(conjunto_2)
print(conjunto_3)

conjunto.add(1)
print(conjunto)

conjunto.remove(1)
print(conjunto)

print(conjunto.intersection(conjunto_2))
print(conjunto_2.issubset(conjunto))
print(conjunto_3.issubset(conjunto))

# DICCiONARIOS

diccionario = {1: "Uno", 2: "Dos"} #aqui definimos un diccionario con dos elementos
diccionario[3] = "Tres" #agregando un nuevo elemento al diccionario
print(diccionario)

dict_lista_tuplas = dict([(1, "Uno"), (2, "Dos"), (3, "Tres")])
print(dict_lista_tuplas)

dict_lista_string = dict(Uno = 1, Dos = 2, Tres = 3)
print(dict_lista_string)

dict_tipos = {1: "integer", 
              2.2: "float", 
              "texto": "string", 
              (1, 2): "tupla"}

print(dict_tipos)

dict_repeticion = {1: "Primero", 1: "Último"}
print(dict_repeticion)

print(diccionario, 
      diccionario.keys(), 
      diccionario.values(), 
      diccionario.items())

claves = diccionario.values()
print(claves)
diccionario[1] = "One"
print(claves)
diccionario.pop(2)
print(diccionario)
#diccionarios : un grupo de pares de clave-valor. los elementos PARES del diccionario de indexan por clave unica que se utilizan para acceder a los valores.
#se escriben entre llaves { } y se separan por comas. cada elemento se separa por comas. cada elemento tiene una clave y un valor separados por dos puntos : .
dic_vacio= {} #diccionario vacio
#clave -valor
new_person= {'name': 'john', 'age': 38, 'weight': 70.2, 'has_glasses': False } #agregando un nuevo elemento al diccionario
#a traves de la clave 'name' se puede acceder al valor 'john'

new_person['name']= 'javiera' #modificando el valor de la clave 'name' en el diccionario
new_person['hobbies']= ['estudiar', 'jugar'] #no existe la clave hobbies, entonces hay que crearla y asignarle un valor
new_person= {'name': 'john', 'age': 38, 'weight': 70.2, 'has_glasses': False , 'hobbies': ['estudiar', 'jugar']} #agregando la clve hobbies al diccionario
print(new_person) #imprimiendo el diccionario completo
#salida ??? 
print(new_person['hobbies']) #imprimiendo el valor de la clave hobbies
print(new_person['hobbies'][0]) #imprimiendo el primer elemento de la lista hobbies, el 0 es la posicion de la lista
print(new_person['hobbies'][1]) #imprimiendo el segundo elemento de la lista hobbies, el 1 es la posicion de la lista


#que es un diccionario? es una coleccion de pares clave-valor. se puede acceder a los valores a traves de las claves. las claves son unicas y no pueden repetirse. los valores pueden ser de cualquier tipo de dato. los diccionarios son mutables, es decir, se pueden modificar. se pueden agregar, eliminar o modificar elementos en un diccionario. los diccionarios son desordenados, es decir, no tienen un orden definido. se pueden anidar diccionarios dentro de otros diccionarios.



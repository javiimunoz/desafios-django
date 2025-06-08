import string


print("esta es una cadena de ejemplo")
nombre= "javiera"
print("mi nombre es", nombre) #diferencia entre el , y el + 
print("mi nombre es " + nombre) #el + une cadenas y el , separa los argumentos

#separando argumentos con comas, se puede imprimir varios argumentos separados por comas

#interpolacion

nombre = "javiera"
print(f"mi nombre es {nombre}") #f-string, se usa la f antes de la cadena para interpolar variables dentro de la cadena
string.format()
first_name = "javiera"
last_name = "muñoz"
age = 18
print("mi nombre es {} {} y tengo {} años".format(first_name, last_name, age)) #se usa el metodo format para interpolar variables dentro de la cadena
print("mi nombre es {} {} y tengo {} años".format(first_name, last_name, age)) #se puede usar el indice de la variable dentro de la cadena
#{} se usa para indicar el lugar donde se va a insertar la variable, se puede usar el indice de la variable dentro de las llaves
#input

input("ingrese su nombre") #se usa para pedir un dato al usuario, el dato se guarda en una variable
#input sirve para pedir un dato al usuario, el dato se guarda en una variable
correo= input("ingrese su correo") #se usa para pedir un dato al usuario, el dato se guarda en una variable
print(f"{correo}") #se imprime el correo ingresado por el usuario 
#la f antes de la cadena indica que se va a usar interpolacion, se puede usar el metodo format() para interpolar variables dentro de la cadena
#la interpolacion es una forma de insertar variables dentro de una cadena, se puede usar el metodo format() o la f-string


#crea un menu de bienvenida y solicitar: nombre,apellido,direccion,edad,sexo,email

print("bienvenido al sistema de registro")
print("por favor ingrese los siguientes datos")
nombre= input("ingrese su nombre: ") #se usa para pedir un dato al usuario, el dato se guarda en una variable
apellido= input("ingrese su apellido: ")
direccion= input("ingrese su direccion: ")
edad= input("ingrese su edad: ")
sexo= input("ingrese su sexo (M/F): ")
email= input("ingrese su email: ")

#imprimir los datos ingresados

print("datos ingresados") #se imprime el mensaje
print(f"nombre: {nombre}")
print(f"apellido: {apellido}")
print(f"direccion: {direccion}")
print(f"edad: {edad}")
print(f"sexo: {sexo}") #la f antes de la cadena indica que se va a usar una variable dentro de la cadena
print(f"email: {email}")
print(f"es chileno: {False}") #se imprime el mensaje de si es chileno o no
print("gracias por registrarse") #se imprime el mensaje de gracias

#el input siempre captura string, por lo que si se quiere capturar un numero se debe convertir a int o float
# type nos dice el tipo de dato de la variable
# print(type(edad)) #se imprime el tipo de dato de la variable edad
# edad= int(edad) #se convierte la variable edad a int
#tuplas conjunto de datos inmutables, no se pueden modificar, se definen con ()
#tiposde datos en python
#string o cadenas de texto
#listas, se definen con []
#diccionarios, se definen con {}
#conjuntos, se definen con set()
#booleanos, se definen con True o False
#numeros, se definen con int o float
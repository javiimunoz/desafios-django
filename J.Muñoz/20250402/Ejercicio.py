#ejercicio solicitar al usuario su nombre, apellido, direccion, edad, direccion y email y agregarlos a una lista y imprimir la lista completa

print("Por favor ingrese los siguientes datos")
nombre= input("ingrese su nombre: ") #se usa para pedir un dato al usuario, el dato se guarda en una variable
apellido= input("ingrese su apellido: ")
direccion= input("ingrese su direccion: ")
edad= int(input("ingrese su edad: "))
correo= input("ingrese su correo: ")

datos_usuario= [] #se crea una lista vacia para almacenar los datos del usuario
datos_usuario.append(nombre) #se agrega el nombre a la lista
datos_usuario.append(apellido) #se agrega el apellido a la lista
datos_usuario.append(direccion) #se agrega la direccion a la lista
datos_usuario.append(edad) #se agrega la edad a la lista
datos_usuario.append(correo) #se agrega el correo a la lista

#imprimir los datos ingresados
print(datos_usuario) #se imprime la lista completa

#imprimir un mensaje de saludo al usuario
print(f"Hola {nombre} {apellido}, bienvenido al sistema de registro") #se imprime el mensaje de saludo al usuario
print(f"su edad es {edad} años") #se imprime la edad del usuario
print(f"su direccion es {direccion}") #se imprime la direccion del usuario
print(f"su correo es {correo}") #se imprime el correo del usuario
print("gracias por registrarse") #se imprime el mensaje de gracias





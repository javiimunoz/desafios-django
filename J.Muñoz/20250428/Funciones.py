#Una funcion es un bloque de codigo que solo se ejecuta cuando es llamada.
# por que usar funciones?
# - Reutilizacion de codigo
# - Mejora la legibilidad del codigo
# - organiza el codigo en partes mas pequeñas y manejables
# - modularidad
# entonces una funcion en resumen es un bloque de codigo que se puede reutilizar y que mejora la legibilidad del codigo.

''' 
def nombre_funcion(parametros): #parametros son opcionales
"""documentacion opcional"""
    intrucciones    #print, if-for, while, etc.
    return valor #si
'''
# ejemplo 

def saludar1_funcion(): #definicion de la funcion
    print("Hola, mundo!")
saludar1_funcion()
#llamar una funcion es ejecutar el bloque de codigo que contiene la funcion, en este caso saludar_funcion() ejecuta el print("Hola, mundo!")
#para llamar una funcion se usa el nombre de la funcion seguido de parentesis () y si tiene parametros se le pasan dentro de los parentesis.

#parametro = variable que se pasa a la funcion, es un valor que se le da a la funcion para que lo use dentro de su bloque de codigo.


#funciones con parametros

def saludar2(javi): #definicion de la funcion con un parametro
    print(f"Hola, {javi}!") #f-string, es una forma de formatear cadenas de texto en python, se usa la letra f antes de la cadena y se pueden usar llaves {} para insertar variables dentro de la cadena.
    saludar2("javi") #llamada a la funcion con el parametro "javi" #("javi") es el argumento que se le pasa a la funcion, es el valor que se le da al parametro nombre.

#funciones con valor de retorno

def sumar(a, b): #definicion de la funcion con dos parametros
    return a + b #return devuelve el resultado de la suma de a y b, el valor que devuelve la funcion se puede almacenar en una variable o usar directamente.
resultado = sumar(3,5)
print(resultado) #imprime el resultado de la suma de 3 y 5, que es 8.

sumar(4,6) #valor retornado no es utilizado, solo se imprime el resultado de la suma de 4 y 6, que es 10.

#salida = 8

#parametros por defecto
nombre = "amigo" #definicion de la variable nombre con un valor por defecto
def saludar3(nombre="amigo") : #definicion de la funcion con un parametro por defecto
   print(f"Hola, {nombre}!") #f-string, es una forma de formatear cadenas de texto en python, se usa la letra f antes de la cadena y se pueden usar llaves {} para insertar variables dentro de la cadena.
   saludar3()
   saludar3("carlos")
   saludar3("javiera muñoz")
   
#salida = Hola, amigo! Hola, carlos!

#Funciones anidadas
z = 10
def mayor(x, y):
    def mensaje():
        print("calculando el mayor...")
        mensaje()
        return x if x > y else y #return devuelve el mayor de los dos numeros, si x es mayor que y devuelve x, si no devuelve y.
    print(mayor(5,4)) 
    
    
    
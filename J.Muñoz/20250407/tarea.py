#solicitar al usuario el ingreso de la edad y validar que es menor de edad, mayor de edad y si es mayor de edad 
edad = int(input("Ingrese su edad: "))
if edad < 18: #< menor de edad
    print("menor de edad")
elif edad >= 60: #>= mayor de edad
    print("adulto mayor")
else:
    print("es mayor de edad") 

#ejercicio 2 soliciatar al usuario el ingreso de un numero y validar si es distinto de 0 y validar si es positivo o negativo.

numero = int(input("Ingrese un numero: "))
if numero == 0: #== igual a cero
    print("El numero es cero")
else: #!= distinto de cero
    print("El numero es distinto de cero")
    if numero > 0: #> mayor que cero
        print("El numero es positivo")
    else: #< menor que cero
        print("El numero es negativo")
    
    #revisar todo
   # 4< x and x > 8 # x es mayor que 4 y menor que 8
    
    
    #tarea con nota, calculo del imc en python 
    #imc = peso / altura^2
    imc= int(input("Ingrese su peso: "))
    
    #solicitar al usuario el ingreso de un monto en dolar y convertirlo a pesos chilenos
    input("Ingrese el monto en dolares: ")
    
peso = 990 #valor del dolar en pesos chilenos
pesos = peso * 990
print("El monto en pesos chilenos es: ", pesos)


#luego a pesos argentinos

#propociciones 
#diagrama de flujo
#python 
#listas,duplas,tuplas,diccionarios
#if,elif,else



    
    
    
    
    
    
    
    
    
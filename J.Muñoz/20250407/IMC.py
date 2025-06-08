#calcular el imc 
# crear la variable de altura y peso 
#float es un tipo de dato que permite almacenar decimales
#el and se utiliza para evaluar dos condiciones al mismo tiempo
#el or se utiliza para evaluar si alguna de las condiciones es verdadera
#el if se utiliza para evaluar una condicion y ejecutar un bloque de codigo si es verdadera
#el elif se utiliza para evaluar una condicion y ejecutar un bloque de codigo si es verdadera, si no se evalua la siguiente condicion
Peso = float(input("Ingrese su peso en Kg: "))
ALtura = float(input(" Ingrese su Altura en Metros: "))

if Peso == 0 or ALtura == 0:
    print("Error: Peso o altura no pueden ser cero")
if Peso and ALtura != 0:
    imc = Peso / (ALtura * ALtura)
    if imc < 18.5:
        print("Bajo peso")
        print(f"Su IMC es: {imc}")
        print(f"Su peso es {Peso}")
        print(f"Su altura es {ALtura}")
        print(f"Usted sufre de bajo ")
        
    elif imc >= 18.5 and imc < 24.9:
        print("Normal")
        print(f"Su IMC es: {imc}")
        print(f"Su peso es {Peso}")
        print(f"Su altura es {ALtura}")
        print(f"usted tiene un peso normal")
    elif imc >= 25.0 and imc < 29.9:
        print("Sobrepeso")
        print(f"Su IMC es: {imc}")
        print(f"Su peso es {Peso}")
        print(f"Su altura es {ALtura}")
        print(f"Usted sufre de sobrepeso ")
    elif imc >= 30.0 and imc < 34.9:
        print("Obesidad tipo I")
        print(f"Su IMC es: {imc}")
        print(f"Su peso es {Peso}")
        print(f"Su altura es {ALtura}")
        print(f"Usted sufre de obesidad tipo I")
    elif imc >= 35.0 and imc < 39.9:
        print("Obesidad tipo II")
        print(f"Su IMC es: {imc}")
        print(f"Su peso es {Peso}")
        print(f"Su altura es {ALtura}")
        print(f"Usted sufre de obesidad tipo II")
    else :
        print("Obesidad tipo III")
        print(f"Su IMC es: {imc}")
        print(f"Su peso es {Peso}")
        print(f"Su altura es {ALtura}")
        print(f"Usted sufre de obesidad tipo III")
        
        

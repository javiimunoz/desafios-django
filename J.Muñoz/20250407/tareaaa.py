#calcular el imc y colocar si esta bajo, normal o sobrepeso
# imc clasification
# imc = peso / (altura * altura)
# peso = kg
# altura = m
# imc < 18.5 = bajo peso
# imc >= 18.5 and imc < 24.9 = normal
# imc >= 25 and imc < 29.9 = sobrepeso
# imc >= 30 = obesidad I
# imc >= 35 = obesidad tipo II
# imc >= 40 = obesidad tipo III
# imc >= 45 = obesidad tipo IV

print("Bienvenido al programa de calculo de IMC")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))
imc = peso / (altura * altura)
print("Su IMC es: ", imc)
if imc < 18.5:
    print("Bajo peso")
elif imc >= 18.5 and imc < 24.9:
    print("Normal")
elif imc >= 25 and imc < 29.9:
    print("Sobrepeso")
elif imc >= 30 and imc < 34.9:
    print("Obesidad tipo I")
elif imc >= 35 and imc < 39.9:
    print("Obesidad tipo II")
elif imc >= 40 and imc < 44.9:
    print("Obesidad tipo III")
elif imc >= 45:
    print("Obesidad tipo IV")
else:
    print("Gracias por usar el programa de calculo de IMC")




#Grande Tamaño: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: ran_tamanio= [- 1, 3, 5, -5] devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]


grande_tamanio = [-1, 3, 5, -5]
#recorriendo la lista
""" for numero in gran_tamanio:
print(numero)
if numero > 0:
"""
for posicion in range(0, len(grande_tamanio)): #el for esta indicando que va a recorrer la lista desde la posicion 0 hasta la longitud de la lista
    #print(posicion) #imprimiendo la posicion de la lista, 0, 1, 2, 3
    #print(grande_tamanio[posicion]) #-1, 3, 5, -5
    if grande_tamanio[posicion] > 0: #if esta indicando que si el valor de la lista en la posicion es mayor a 0
        grande_tamanio[posicion]= "big" #aqui estamos cambiando el valor de la lista en la posicion que cumple la condicion
        
    print(grande_tamanio) #imprimiendo la lista completa
    

 #Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: contar_positivos=[- 1, 1, 1,1 ], cambia la lista original a [-1, 1, 1, 3] y la imprime
#Ejemplo: contar_positivos=[1, 6, -4, -2, -7, -2], cambia la lista a [1, 6, -4, -2, -7, 2] y la imprime

#print(mi_lista) #imprimiendo la lista completa

lista2=[-1, 1, 1, 1] #definiendo una lista con varios tipos de datos
contador=0
for i in range(0,len(lista2)):
    if lista2[i]>0:
        contador+1 #contador = contador +1 #contador++
        
        if contador > 0:
            lista2[len(lista2)-1]= contador
            #len(lista2) retorna cantidad de elementos de la lista, en la ultima posicion se coloca el contador
            print(lista2) #imprimiendo la lista completa 
            
        
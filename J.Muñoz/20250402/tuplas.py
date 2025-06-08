#tuplas son inmutables, no se pueden modificar, se definen con ()
Dog= ( 'ayun', 'bulldog frances', 5 ,False)
print(Dog[0]) #imprime el primer elemento de la tupla
#ERROR: no se puede modificar el valor de la tupla (el objeto 'tupla' no admite la asignacion de elementos)
print(Dog) #imprime la tupla completa

#listas un conjunto de datos mutables y puede contener un grupo de valores generalmente destinado a almacernar un grupo de datos
#las listas siempre estan separadas por comas 

lista_vacia = 0  #lista vacia
ninjas= ['naruto', 'sasuke', 'sakura'] #lista de ninjas
print(ninjas[2])  #salida: sakura
ninjas[0]= 'Caitlyn' #modificando el primer elemento de la lista 
print(ninjas[0]) #sobreescribiendo el primer elemento de la lista en la posicion 0
ninjas.append('sai') #agregando al final un elemento a la lista en este caso 'sai'
print(ninjas) #imprimiendo la lista completa
ninjas.pop() #elimina el ultimo elemento de la lista
print(ninjas) #salida: naruto, sasuke, sakura, sai
ninjas.pop(1) #elimina el segundo elemento de la lista #chao sasuke
print(ninjas) #salida: naruto, sakura, sai
#ninjas[3]= 'viktor'
#print(ninjas[3]) #python no nos deja salir del rango de la lista, si lo hacemos nos da un error de index out of range
ninjas.append('javiera') #agregando al final un elemento a la lista en este caso 'javiera'
print(ninjas) #imprimiendo la lista completa





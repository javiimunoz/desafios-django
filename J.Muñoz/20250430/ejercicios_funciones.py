"""Cuenta regresiva:
crea una funcion que acepte un numero como entrada.
devuelve una nueva lista que cuenta hacia atras en uno, 
desde el numero
(como el elemento 0) hasta el 0 (como el ultimo elemento)
ejemplo: la cuenta regresiva (5)
deberia devolver: [5, 4, 3, 2, 1, 0]"""

def cuenta_regresiva(numero) : 
    lista_numeros = [] #definiendo una lista vacia
    for i in range(numero, -1, -1) :
        #print(i)
        lista_numeros.append(i) #agregar numero a la lista
        return lista_numeros
    
resultado = cuenta_regresiva(0) #asigno la lista retornada 
print(resultado) #imprime el contenido de la variable 


#ejercicio 2

"""Imprimir y volver : 
crea una función que recibirá una lista con dos números.
Imprima el primer valor y devuelva el segundo.
Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2"""

def print_and_return(lista):
    print(f"primer valor {lista[0]}")
    return lista[1]

valor_retornado=print_and_return([1,2])
print(f"valor retornado : {valor_retornado}")

#ejercicio 3
"""First Plus Length : crea una función que acepta una lista y 
devuelve la suma del primer valor de la lista más la longitud de la lista.
Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)"""

def first_plus_length (lista):
    return lista[0]+ len(lista)

suma=first_plus_length ([1,2,3,4,5])
print(f"la suma del primer elemento y el tamaño es {suma}")

"""Valores mayores que el segundo : 
escribe una función que acepte una lista 
y crea una nueva lista que contenga solo los valores de la lista original 
que sean mayores que su segundo valor. Imprima cuántos valores son 
y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
Ejemplo: values_greater_than_second ([3]) debería devolver False"""

def values_greater_than_second(lista):
    if len(lista) < 2:
        return False

    segundo_valor = lista[1]
    nueva_lista = [valor for valor in lista if valor > segundo_valor]

    print(len(nueva_lista))
    return nueva_lista

# Ejemplos de uso
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  # Imprime 3, devuelve [5, 3, 4]
print(values_greater_than_second([3]))                # Devuelve False

 ##DICCIONARIOS
mi_diccionario = { "nombre": "Noelle", "lenguaje": "Python" }
for k in mi_diccionario : #aqui se define una variable k que va a iterar a traves de las llaves del diccionario
    print(k)
# salida: nombre, lenguaje

for k in mi_diccionario : 
    print(mi_diccionario[k])

#otra forma de iterar a través de claves o llaves
for key in mi_diccionario.keys( ): 
     print(key)

#iterar con valores
for val in mi_diccionario.values():
     print(val)

#iterar con ambos, llaves y valores
for key, val in mi_diccionario.items():
     print(key, " = ", val)
     
     



##Trabajo por Javiera Muñoz y Benjamin Saavedra 2025/04/24

cantidad_estudiantes = input("Ingrese la cantidad de estudiantes: ")
bucle = 0 # si la cantidad de estudiantes llega a 0 (iguala el bucle) se termina el while
diccionario_alumno = {}
lista_notas = [] # donde se almacenan las notas
promedio = ""
mejor_promedio = None # les asignamos None asi al momento de comparar no lo toma como string no ponemos numero para que no afecte la comparacion
peor_promedio = None
nombre_mejor = ""
nombre_peor = ""
cantidad_de_notas = 0

try:
    cantidad_estudiantes = int(cantidad_estudiantes)  # transformar cantidad de estudiantes a int, si no se puede se termina el codigo

    while cantidad_estudiantes != bucle: #mientras se diferente de bucle el while funcionara
        nombre = input("Ingrese nombre del estudiante: ")
        diccionario_alumno[nombre] = []  # creamos las llaves en base al nombre del estudiante
        cantidad_de_notas = input(f"Ingrese la cantidad de notas de {nombre}: ")

        try:
            cantidad_de_notas = int(cantidad_de_notas)  # Convertimos la cantidad de notas a entero

            for i in range(0, cantidad_de_notas):# se ingresan las notas
                notas = input(f"Ingrese la nota numero {i+1}, si es un decimal separelo por un punto: ")

                try:
                    notas = float(notas)  # Convertimos la nota a flotante

                    # Verificamos si la nota está dentro del rango permitido
                    if notas > 7 or notas < 1:#si esta fuera de rango no añade la nota
                        print("Has ingresado un número fuera de rango")
                    else:
                        lista_notas.append(notas)  # Agregamos la nota a la lista de notas

                except ValueError:#si no se puede convertir en float pasa de largo
                    print("La nota ingresada no es válida")

        except ValueError:
            print("La cantidad de notas no es un número válido")

        diccionario_alumno[nombre] = lista_notas  # se asignan las notas que estan en la lista a las claves de nombres
        lista_notas = []  # Limpiamos la lista de notas para el siguiente estudiante
        cantidad_estudiantes -= 1  # se reduce el contador de estudiantes

    print("---RESULTADOS---")

    # Calculamos los promedios para cada estudiante
    for k, v in diccionario_alumno.items():
        if len(v) > 0:  # verificar que haya por lo menos un valor
            promedio = sum(v) / len(v)  # suma los valores y los divide en la cantidad de valores

            print(k, v, "Promedio:", promedio)

            # Comprobamos si este es el mejor promedio
            if mejor_promedio is None or promedio > mejor_promedio:
                mejor_promedio = promedio
                nombre_mejor = k

            # Comprobamos si este es el peor promedio
            if peor_promedio is None or promedio < peor_promedio:
                peor_promedio = promedio
                nombre_peor = k

    print("---RESUMEN---")
    print("Mejor promedio:", mejor_promedio, "", nombre_mejor)
    print("Peor promedio:", peor_promedio, "", nombre_peor)

except ValueError:
    print("La cantidad de estudiantes no es un número válido")
    
#declaraciones condicionales nos permiten tomar decisiones en el flujo de un programa
# if, elif, else
# if: se ejecuta si la condicion es verdadera
# elif: se ejecuta si la condicion es verdadera y la anterior fue falsa
# else: se ejecuta si todas las condiciones anteriores fueron falsas
x = 12 # variable de tipo entero
if x > 50 : 
    print( "mayor que 50")
else : 
    print( "menor que 50")
    
    x = 55 # variable de tipo entero
if x > 10 :
    print( "menor que 10")
elif x > 50 :
    print( "mayor que 50")
else :
    print( "menor que 10") 
    #aunque x sea mayor que 10 y 50, la primera declaracion verdadera es la unica que se ejecutara, por lo que solo veremos 'mayor que 10' 
    if x < 10:
        print("menor que 10")
        # no sucedera nada porque la declaracion es falsa  
        

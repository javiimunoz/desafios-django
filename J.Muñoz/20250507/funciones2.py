class Persona: #definicion de objeto o clase = maqueta o molde
    def __init__(self,nombre,rut):
     self.rut= ""       #"1-9"
     self.nombre="javi"   #"javi"
     self.apellido="Muñoz"
     self.edad=18
     self.direccion="Casa"
     self.telefono="+56974138312"
     self.correo="javii56munoz@gmail.com"
     
     def login(self):
         print(self.nombre - self.rut)

     
 #instancia de la clase (creacion del objeto)
javi = Persona("javi","2-8") #acaba de crear el objeto javi
javi.rut="4-8"
juan = Persona("juan", "3-7")
juan.rut="7-7"
print(juan.rut)
print(javi.rut)
javi.login() #llamado a la funcion login de la clase Persona, se ejecuta el bloque de codigo que contiene la funcion login.

    
class Persona():
    def __init__(self, nombre, rut):
        self.__rut = rut
        self.__nombre = nombre
        self.apellido = "Muñoz"
        self.edad = 18
        self.direccion = "Casa"
        self.telefono = "+56974138312"
        self.correo = ""
        self.usuario = True 
    
    # Getter para el nombre
    def get_nombre(self): # Usamos "get_" para obtener el valor de el nombre
        """devuelve el """
        return self.__nombre
    
    # Setter para el nombre
    def set_nombre(self, nuevo_nombre): # usamos "set_" para modificar el nombre de forma controlada.
        if len(nuevo_nombre) > 0: 
            # Forma segura de cambiar el nombre: solo si no esta vacío
            self.__nombre = nuevo_nombre
        else:
            # Manejo de error si el nombre está vacío :D
            print("El nombre no puede estar vacío") 
        
    #rut
    def get_rut(self):
        return self.__rut
    def set_rut(self, nuevo_rut):
        if len(nuevo_rut) > 0:
            self.__rut = nuevo_rut
        else:
            print("El RUT no puede estar vacío")
    #---
    def login(self):
        if self.usuario:
            print(f"Bienvenido {self.__nombre} - {self.__rut}") # aqui se usa el nombre privado __nombre
        else:
            print("Usuario no registrado")

# Clase hija (hereda de persona)
class Estudiante(Persona):
    def __init__(self, nombre, rut, carrera): #init es el constructor de la clase 
        super().__init__(nombre, rut)  # Llama al constructor de la clase padre
        self.carrera = carrera # Atributo específico de Estudiante
    
    def mostrar_info(self):
        print(f"Estudiante: {self.get_nombre()}, Carrera: {self.carrera}")
        

persona = Persona("javi", "22285495-4")
print(persona.get_nombre())  # Imprime el nombre actual
persona.set_nombre("Juan")  # Cambia el nombre a "Juan" 
persona.login() 

# Solicitar datos al usuario
nombre_input = input("Ingresa tu nombre: ")
rut_input = input("Ingresa tu RUT: ")

# Crear objeto con los datos ingresados
persona = Persona(nombre_input, rut_input)

# Ejecutar el login
persona.login()

# 4 pilares de la programacion orientada a objetos

# 1. Encapsulacion: ocultar los detalles internos de la clase y exponer solo lo necesario.

# 2. Abstraccion: simplificar la complejidad al ocultar los detalles innecesarios.

# 3. Herencia: permite crear nuevas clases basadas en clases existentes, heredando sus atributos y métodos.

# 4. Polimorfismo: permite que diferentes clases implementen métodos con el mismo nombre, pero con comportamientos diferentmish

# ahora practica tu velocidad de escritura con la siguiente pagina: 
# https://monkeytype.com/
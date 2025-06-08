class Persona():
    def __init__(self, nombre, rut):
        self.rut = rut
        self.nombre = nombre
        self.apellido = "Muñoz"
        self.edad = 18
        self.direccion = "Casa"
        self.telefono = "+56974138312"
        self.correo = ""
        self.usuario = True 
        
    def login(self):
        if self.usuario:
            print(f"Bienvenido {self.nombre} - {self.rut}")
        else:
            print("Usuario no registrado")

persona = Persona("javi", "22285495-4")
persona.login()

# Solicitar datos al usuario
nombre_input = input("Ingresa tu nombre: ")
rut_input = input("Ingresa tu RUT: ")

# Crear objeto con los datos ingresados
persona = Persona(nombre_input, rut_input)

# Ejecutar el login
persona.login()


#4 pilares de la programacion orientada a objetos
# 1. Encapsulacion: ocultar los detalles internos de la clase y exponer solo lo necesario.
# 2. Abstraccion: simplificar la complejidad al ocultar los detalles innecesarios.
# 3. Herencia: permite crear nuevas clases basadas en clases existentes, heredando sus atributos y métodos.
# 4. Polimorfismo: permite que diferentes clases implementen métodos con el mismo nombre, pero con comportamientos diferentes.

#teniamo que investigar eso,no era implementarlo tt


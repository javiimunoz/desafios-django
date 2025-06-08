class Persona ():
    def __init__(self, nombre, rut, email):
        self.rut = rut
        self.nombre = nombre
        self.direccion = "Casa"
        self.email = "javii56munoz@gmail.com"
        
        
    def operacion_banco(self, monto):
        self.cuenta = Banco(0, 0)
obj_javi = Persona("javi", "22285495-4", "javii56munoz@gmail.com")
#obj_javi.cuenta.deposito(50000).informacion()#funciona

class Banco():
    def __init__(self, intereses, saldo):
        self.intereses = intereses
        self.saldo = saldo
        
    def deposito(self,monto):
        self.saldo += monto #self.saldo = self.saldo + monto
        return self
    
    def giro(self,monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("el monto a girar es mayor al saldo")
            return self
    
    def informacion(self):
        print(f"El saldo es: {self.saldo}")
        return self
    
    #esto es lo mismo pero mas corto
#instancia de la clase

''' banco_javi = Banco(0, 50000)
banco_javi.informacion()
banco_javi.deposito(100000)
banco_javi.informacion()
giro = banco_javi.giro(30000)
banco_javi.informacion()
'''
#banco_javi = Banco(0, 50000)

#banco_javi.informacion().deposito(100000).informacion().giro(30000).informacion()
 
 #instancia B
 
 #B) +30000 deposito into
#banco_javi2 = Banco(0, 50000)
#banco_javi2.informacion().deposito(30000).informacion().giro(30000).informacion()


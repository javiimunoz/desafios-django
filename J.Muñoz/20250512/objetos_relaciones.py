#class banco():
  #      def __init__(self): #constructor (tasa_interes,balance o saldo):
   #         self.deposito #aumenta el saldo
    #        self.giro #disminuye el saldo
     ##      self.intereses # ?
       # def deposito(self, monto):
            
#instancias
#a) 100000 deposito - 30000 giro 
#b) +30000 desposito into


class banco():
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        self.deposito = 0
        self.giro = 0
        self.intereses = 0
        
    def deposito(self, monto): #aumenta el saldo
        self.balance += monto
        self.deposito = monto
        print(f"Deposito: {monto}")
        print(f"Nuevo saldo: {self.balance}")
        
    def giro(self, monto): #disminuye el saldo
        if monto <= self.balance:
            self.balance -= monto
            self.giro = monto
            print(f"Giro: {monto}")
            print(f"Nuevo saldo: {self.balance}")
        else:
            print("Fondos insuficientes para el giro.") 
            
            def mostrar_saldo(self):
                print(f"Saldo actual: {self.balance}")
            
    
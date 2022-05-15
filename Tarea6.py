class Cuenta:
    
    def __init__(self, nombre, saldo = 0.0):
        self.nombre= nombre
        self.saldo= saldo

    def mostrar(self):
        print(f"El titular de la saldo {self.nombre} posee: ${self.saldo} pesos.")
    
    def ingresar(self, ingreso):
        if ingreso > 0:
            self.saldo += ingreso
            print(f"El titular {self.nombre} ingreso ${ingreso}")
        else:
            print(f"El monto ingresado(${ingreso}) no es valido, ingrese numeros positivos")
    
    def retirar(self, retiro):
        if retiro > 0:
            self.saldo -= retiro
            print(f"El titular {self.nombre} retiro ${retiro}")
        else:
            print(f"El monto ingresado(${retiro}) no es valido, ingrese numeros positivos")

usuario1 = Cuenta("gustavo",233)

usuario1.mostrar()
usuario1.ingresar(100)
usuario1.ingresar(-100)
usuario1.mostrar()
usuario1.retirar(-4)
usuario1.retirar(200)
usuario1.mostrar()
usuario1.retirar(200)


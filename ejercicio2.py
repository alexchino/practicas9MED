class Usuario:
    def __init__(self, nombre, saldo_inicial=0):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self.saldo}"
        else:
            return "La cantidad a depositar debe ser mayor que cero."

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self.saldo}"
        elif cantidad > self.saldo:
            return "Fondos insuficientes."
        else:
            return "La cantidad a retirar debe ser mayor que cero."

    def consultar_saldo(self):
        return f"Saldo actual de {self.nombre}: ${self.saldo}"


if __name__ == "__main__":
    
    usuario1 = Usuario("sander", 1000)

    print(usuario1.consultar_saldo())  
    print(usuario1.depositar(500))     
    print(usuario1.retirar(200))       
    print(usuario1.consultar_saldo())  
    print(usuario1.retirar(2000))      
class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_a_vender):
        if cantidad_a_vender <= 0:
            return "La cantidad a vender debe ser mayor que cero."
        elif cantidad_a_vender > self.cantidad:
            return "No hay suficiente stock para completar la venta."
        else:
            self.cantidad -= cantidad_a_vender
            total_venta = cantidad_a_vender * self.precio
            return f"Venta realizada: {cantidad_a_vender} {self.nombre}(s) por ${total_venta}. Stock restante: {self.cantidad}"

if __name__ == "__main__":
   
    articulo1 = Articulo("pantalon", 23, 43)

    resultado_venta = articulo1.vender(15)
    print(resultado_venta) 

    resultado_venta = articulo1.vender(5)
    print(resultado_venta)  

    print(f"Stock de {articulo1.nombre}: {articulo1.cantidad}")

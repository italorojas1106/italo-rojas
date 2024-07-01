# Clase product, se guardan los datos capturados desde la API
class Product:
    def __init__(self, name, quantity, price, adicional, stock):
        self.name = name
        self.quantity = quantity
        self.price = float(price) + float(price)*0.16 # Se guarda el precio incluido con el IVA
        self.adicional = adicional
        self.stock = stock

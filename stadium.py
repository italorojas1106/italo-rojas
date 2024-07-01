# Clase stadium, se guardan los datos capturados desde la API
class Stadium:
    def __init__(self, id, name, city, capacity_general, capacity_vip, restaurants):
        self.id = id
        self.name = name
        self.city = city
        self.capacity_general = capacity_general
        self.capacity_vip = capacity_vip
        self.restaurants = restaurants
        self.asientos = [["Disponible" for _ in range(self.capacity_vip)] for _ in range(self.capacity_general)]

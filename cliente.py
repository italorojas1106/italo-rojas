import string
import random

# Clase cliente, se guardan los datos capturados desde la API
class Cliente:
    def __init__(self, nombre, cedula, edad, tipo_entrada, nombre_estadio,orden):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_entrada = tipo_entrada
        self.nombre_estadio = nombre_estadio
        self.id_boleto = self.generar_id_boleto() # Se genera un id de boleto aleatorio cada vez que se crea un cliente
        self.orden = orden
    def generar_id_boleto(self): # Funcion para generar un id aleatorio para el boleto
        caracteres = string.ascii_letters + string.digits
        id_boleto = ''.join(random.choice(caracteres) for _ in range(8))
        return id_boleto

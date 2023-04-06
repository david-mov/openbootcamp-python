class Vehiculo:
	def __init__(self, color, ruedas, puertas):
		self.color = color
		self.ruedas = ruedas
		self.puertas = puertas

class Coche(Vehiculo):
	def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
		self.velocidad = velocidad
		self.cilindrada = cilindrada

		Vehiculo.__init__(self, color, ruedas, puertas)

coche = Coche('Rojo', 4, 4, 150, 6)
print(coche)
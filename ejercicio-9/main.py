class Alumno:
	def __init__ (self, nombre, nota):
		self.nombre = nombre
		self.nota = nota

	def status (self):
		if self.nota > 6:
			return f'Alumno aprobado con {self.nota}'
		else:
			return f'Alumno reprobado con {self.nota}'

	def __str__(self):
		return f'Nombre: {self.nombre} - Nota: {self.nota}'

alumno_a = Alumno('Lisa', 7)
print(alumno_a)
print(alumno_a.status())

alumno_b = Alumno('Bart', 3)
print(alumno_b)
print(alumno_b.status())


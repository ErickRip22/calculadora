
'''
Alumno: Erick Raul Ibarra
'''
class Calculadora():
	

	def __init__(self):
		self.resultado = 0


	def obtener_resultado(self):
		return self.resultado

	def suma(self, num1, num2):
		try:
			self.resultado = num1 + num2
		except Exception:
			self.resultado = 'Datos Incorrectos'

	def resta(self, num1, num2):
		try:
			self.resultado = num1 - num2
		except Exception:
			self.resultado = 'Datos Incorrectos'

	def multiplicacion(self, num1, num2):
		try:
			self.resultado = int(num1) * int(num2)
		except Exception:
			self.resultado = 'Datos Incorrectos'

	def potencia(self, num1, num2):
		try:
			self.resultado = int(num1) ** int(num2)
		except Exception:
			self.resultado = 'Datos Incorrectos'

	def division(self, num1, num2):
		try:
			if(int(num2) == 0):
				self.resultado = 'No dividir entre 0'
			else:
				self.resultado = int(num1) / (int(num2) + 0.0)

		except Exception:
			self.resultado = 'Datos Incorrectos'

	def raiz(self, num1):
		try:
			if(int(num1) < 0):
				self.resultado = 'No puede calcular negativos'
			else:
				self.resultado = int(num1) ** 0.5

		except Exception:
			self.resultado = 'Datos Incorrectos'
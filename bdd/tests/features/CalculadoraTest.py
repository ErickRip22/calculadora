import unittest
from calculadora import Calculadora 
class CalculadoraTest(unittest.TestCase):

	def setUp(self):
		self.calc = Calculadora()

	def test_valor_de_inicio_igual_a_cero(self):
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_sumar_2_mas_2(self):		
		self.calc.suma(2, 2)
		self.assertEquals(self.calc.obtener_resultado(), 4)

	def test_sumar_negativo_positivo(self):
		self.calc.suma(-1, 10)
		self.assertEquals(self.calc.obtener_resultado(), 9)

	def test_sumar_3_mas_3(self):
		self.calc.suma(3, 3)
		self.assertEquals(self.calc.obtener_resultado(), 6)

	def test_sumar_una_letra(self):
		self.calc.suma('L', 1)
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')

	def test_resta_3_menos_2(self):
		self.calc.resta(3, 2)
		self.assertEquals(self.calc.obtener_resultado(), 1)

	def test_resta_1_menos_2(self):
		self.calc.resta(1, 2)
		self.assertEquals(self.calc.obtener_resultado(), -1)

	def test_resta_3_menos_menos_2(self):
		self.calc.resta(3, -2)
		self.assertEquals(self.calc.obtener_resultado(), 5)

	def test_resta_3_menos_letra(self):
		self.calc.resta(3, 'a')
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')

	def test_multiplicacion_3_por_2(self):
		self.calc.multiplicacion(3, 2)
		self.assertEquals(self.calc.obtener_resultado(), 6)

	def test_multiplicacion_0_por_2(self):
		self.calc.multiplicacion(0, 2)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_multiplicacion_3_por_menos_2(self):
		self.calc.multiplicacion(3, -2)
		self.assertEquals(self.calc.obtener_resultado(), -6)

	def test_multiplicacion_3_menos_letra(self):
		self.calc.multiplicacion(3, 'a')
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')

	def test_division_3_por_2(self):
		self.calc.division(3, 2)
		self.assertEquals(self.calc.obtener_resultado(), 1.5)

	def test_division_0_por_2(self):
		self.calc.division(0, 2)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_division_3_por_menos_2(self):
		self.calc.division(3, -2)
		self.assertEquals(self.calc.obtener_resultado(), -1.5)

	def test_division_3_por_0(self):
		self.calc.division(3, 0)
		self.assertEquals(self.calc.obtener_resultado(), 'No dividir entre 0')

	def test_division_3_menos_letra(self):
		self.calc.division(3, 'a')
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')

	def test_potencia_3_por_2(self):
		self.calc.potencia(3, 2)
		self.assertEquals(self.calc.obtener_resultado(), 9)

	def test_potencia_4_por_3(self):
		self.calc.potencia(4, 3)
		self.assertEquals(self.calc.obtener_resultado(), 64)

	def test_potencia_menos_3_por_3(self):
		self.calc.potencia(-3, 3)
		self.assertEquals(self.calc.obtener_resultado(), -27)

	def test_potencia_3_por_0(self):
		self.calc.potencia(3, 0)
		self.assertEquals(self.calc.obtener_resultado(), 1)

	def test_potencia_3_menos_letra(self):
		self.calc.potencia(3, 'a')
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')

	def test_raiz_25(self):
		self.calc.raiz(25)
		self.assertEquals(self.calc.obtener_resultado(), 5)

	def test_raiz_4(self):
		self.calc.raiz(4)
		self.assertEquals(self.calc.obtener_resultado(), 2)

	def test_raiz_9(self):
		self.calc.raiz(9)
		self.assertEquals(self.calc.obtener_resultado(), 3)

	def test_raiz_menos_4(self):
		self.calc.raiz(-4)
		self.assertEquals(self.calc.obtener_resultado(), 'No puede calcular negativos')

	def test_raiz_letra(self):
		self.calc.raiz('a')
		self.assertEquals(self.calc.obtener_resultado(), 'Datos Incorrectos')


if __name__ == '__main__':
	unittest.main()
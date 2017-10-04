Feature: Multiplicacion de dos numeros
	Como usuario de la calculadora
	deseo realizar la multiplicacion de dos numeros
	para obtener el resultado preciso

	Scenario: Multiplicacion de 2 por 2
		Dado que ingreso el par de numeros "2" por "2"
		cuando realizo la operacion
		entoces obtengo el resultado "4"

	Scenario: Multiplicacion de 7 por 5
		Dado que ingreso el par de numeros "7" por "5"
		cuando realizo la operacion
		entoces obtengo el resultado "35"

	Scenario: Multiplicacion de 0 por -7
		Dado que ingreso el par de numeros "0" por "-7"
		cuando realizo la operacion
		entoces obtengo el resultado "0"

	Scenario: Multiplicacion de 1000 por 100
		Dado que ingreso el par de numeros "1000" por "100"
		cuando realizo la operacion
		entoces obtengo el resultado "100000"
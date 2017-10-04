Feature: Divisin de dos numeros
	Como usuario de la calculadora
	deseo realizar la division de dos numeros
	para obtener el resultado preciso

	Scenario: Division de 2 entre 2
		Dado que ingreso el par de numeros "2" entre "2"
		cuando realizo la operacion
		entoces obtengo el resultado "1"

	Scenario: Division de 7 entre 2
		Dado que ingreso el par de numeros "7" entre "7"
		cuando realizo la operacion
		entoces obtengo el resultado "1"

	Scenario: Division de 0 entre 2
		Dado que ingreso el par de numeros "0" entre "2"
		cuando realizo la operacion
		entoces obtengo el resultado "0"

	Scenario: Division de 1000 entre 100
		Dado que ingreso el par de numeros "1000" entre "100"
		cuando realizo la operacion
		entoces obtengo el resultado "10"
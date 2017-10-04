Feature: Resta de dos numeros
	Como usuario de la calculadora
	deseo realizar la resta de dos numeros
	para obtener el resultado preciso

	Scenario: Resta de 2 menos 2
		Dado que ingreso el par de numeros "2" y "2"
		cuando realizo la operacion
		entoces obtengo el resultado "0"

	Scenario: Resta de 7 mas 5
		Dado que ingreso el par de numeros "7" y "5"
		cuando realizo la operacion
		entoces obtengo el resultado "2"

	Scenario: Resta de 0 mas -7
		Dado que ingreso el par de numeros "0" y "-7"
		cuando realizo la operacion
		entoces obtengo el resultado "7"

	Scenario: Resta de 1000 mas 100
		Dado que ingreso el par de numeros "1000" y "100"
		cuando realizo la operacion
		entoces obtengo el resultado "900"
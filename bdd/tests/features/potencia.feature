Feature: Potencia de dos numeros
	Como usuario de la calculadora
	deseo realizar la potenciacion de dos numeros
	para obtener el resultado preciso

	Scenario: Potencia de 2 a la 2
		Dado que ingreso el par de numeros "2" al "2"
		cuando realizo la operacion
		entoces obtengo el resultado "4"

	Scenario: Potencia de -3 a la 3
		Dado que ingreso el par de numeros "-3" al "3"
		cuando realizo la operacion
		entoces obtengo el resultado "-27"

	Scenario: Potencia de 0 a la 2
		Dado que ingreso el par de numeros "0" al "2"
		cuando realizo la operacion
		entoces obtengo el resultado "0"

	Scenario: Potenica de -2 a la 4
		Dado que ingreso el par de numeros "-2" al "4"
		cuando realizo la operacion
		entoces obtengo el resultado "16"
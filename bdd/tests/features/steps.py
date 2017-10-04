# -*- coding: utf-8 -*-
from lettuce import step, world
from calculadora import Calculadora

@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass
@step(u'Dado que ingreso los numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.suma(int(num1), int(num2))
@step(u'entoces obtengo el resultado "([^"]*)"')
def entoces_obtengo_el_resultado_group1(step, esperado):
    obtenido =  world.cal.obtener_resultado()
    assert int(esperado) == obtenido, 'El resultado esperado es' + esperado + ' y el obtenido es ' + obtenido
@step(u'Dado que ingreso el par de numeros "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_el_par_de_numeros_group1_y_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.resta(int(num1), int(num2))

@step(u'Dado que ingreso el par de numeros "([^"]*)" entre "([^"]*)"')
def dado_que_ingreso_el_par_de_numeros_group1_entre_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.division(int(num1), int(num2))
@step(u'Dado que ingreso el par de numeros "([^"]*)" por "([^"]*)"')
def dado_que_ingreso_el_par_de_numeros_group1_por_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicacion(int(num1), int(num2))

@step(u'Dado que ingreso el par de numeros "([^"]*)" al "([^"]*)"')
def dado_que_ingreso_el_par_de_numeros_group1_al_group1(step, num1, num2):
    world.cal = Calculadora()
    world.cal.potencia(int(num1), int(num2))
@step(u'Dado que ingreso el numero "([^"]*)"')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.cal = Calculadora()
    world.cal.raiz(num1)

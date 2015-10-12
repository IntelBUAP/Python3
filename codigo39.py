#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Limpieza usando finally
def divicion(numero1, numero2):
	try:
		resultado = numero1 / numero2
	except ZeroDivisionError:
		print ("Division entre cero no existe")
	else:
		print ("El resultado es", resultado)
	finally:
		print ("Ejecucion de finally")


divicion(2,1)
divicion(2,0)
divicion("1","2")

#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Funciones anonimas.


def incrementos(numero):
	"""docstring for incremetos"""
	return lambda x: x + numero


numero = 2
funcion = incrementos(numero)
numero = eval(input("Ingresa el numero"))
print ("El incremento es: {0}".format(funcion(numero)))


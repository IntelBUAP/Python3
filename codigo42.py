#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Decoradores pro
def decorador(funcion):
	def funcionDecorada(*args, **kwargs):
		print ("La funcion decorada es:", funcion.__name__)
		funcion(*args, **kwargs)

	return funcionDecorada


@decorador 
def suma(numero1, numero2):
	print ("El resultado es %d" % int(numero1 + numero2))

@decorador
def resta(numero1, numero2):
	print ("El resultado es %d" % int(numero1 - numero2))

suma(1, 2)
resta(2, 1)


#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Decoracion de funciones
def suma (numero1, numero2):
	print (numero1 + numero2)

def resta (numero1, numero2):
	print (numero1 - numero2)

def decorador(funcion):
	def funcionDecorada(*args, **kwargs):
		print ("La funcion decorada es:", funcion.__name__)
		funcion(*args, **kwargs)

	return funcionDecorada

print ("Primera forma de decoración")
decorador(suma)(1, 2)
decorador(resta)(2, 1)
print ("Segunda forma de decoración")
funcion = decorador(suma)
funcion(1, 2)
funcion	= decorador(resta)
funcion(1, 2)

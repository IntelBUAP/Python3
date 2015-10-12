#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Calculo de numeros fibonacci

def fibonacci(numero):
	"""
	Devuelve la serie fibonacci hasta n
	"""
	a, b = 0, 1
	while b < numero:
		print (b, end=" ")
		a, b = b, a + b

	print ("")


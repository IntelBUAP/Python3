#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Generador yield.

def funcion(maximo):
	numero = 0
	while numero < maximo:
		yield numero ** 2
		numero += 1

mi = funcion(10)
print (next(mi))
print (next(mi))
print (next(mi))
print (next(mi))
print (next(mi))
print (next(mi))
print (next(mi))
print (next(mi))

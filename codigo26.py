#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Funciones y parametros arbitrarios
def funcion(*nombres):
	for alumno in nombres:
		print ("%s es alumno" % alumno)

	return nombres

print (funcion("Adrian", "Niño", "Roberto", "Celina"))

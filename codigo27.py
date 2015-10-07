#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Funciones y parametros arbitrarios
def funcion(**nombres):
	for alumno in nombres:
		print ("%s es alumno y tiene %d años" % (alumno, nombres[alumno]))

	return nombres
#diccionario = {"Adrian":25, "Niño":25, "Roberto":23, "Celina":23}
print (funcion(Adrian = 25, Nino = 25, Roberto = 23, Celina = 23))

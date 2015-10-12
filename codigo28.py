#! /usr/bin/python3
# -*- coding:utf-8 -*-
# recursividad
def medidor_guapura(intento=1):
	respuesta = input("¿Qué instructor es mas guapo <Adrian> o <Spitia>? ")
	
	if respuesta == "Adrian" or respuesta == "adrian":
		print ("\nEso es verdad y lo sabes!=P")
		intento += 1
		medidor_guapura(intento) # Llamada recursiva

	else:
		print ("\nEstas muy Ciego")

medidor_guapura()


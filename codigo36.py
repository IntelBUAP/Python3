#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Iniciando con las excepciones
import sys

while True:
	try:
		numero = int(input("Ingresa un numero: \n"))
		break
	except EOFError as Error:
		print ("Error de lectura: {0}".format(Error))
	except KeyboardInterrupt:
		print ("Salida por teclado del usuario")
	except:
		print ("Error inesperado =P:", sys.exc_info()[0])
		raise

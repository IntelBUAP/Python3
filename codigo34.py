#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Iniciando con las excepciones
while True:
	try:
		numero = int(input("Ingresa un numero > "))
		break
	except KeyboardInterrupt:
		print ("Ooop! Falle en la lectura intentalo nuevamente plis =P")

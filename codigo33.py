#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Iniciando con las excepciones
while True:
	try:
		numero = int(input("Ingresa un numero > "))
		break
	except ValueError:
		print ("Ooop! No es valor valido")

#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Leemos el nombre y salimos del ciclo cuando leemos el nomre scrap
nombre = ""
intentos = 0
while intentos < 15 and ( nombre != "Scrap" or nombre != "scrap" ):
	nombre = input("Ingresa el nombre -> ")
	if	nombre == "Scrap" or nombre == "scrap":
		print ("Salio scrap [ =P ]")
		break
	intentos += 1
	print ("El numero de intentos sin que salga scrap < %d >" % intentos)

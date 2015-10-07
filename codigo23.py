#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Iterando cadenas usando for
# Ademas de contar vocales y consonantes de una cadena leida por teclado
contador_consonantes = 0
contador_vocales = 0
nombre = input("Ingresa tu nombre completo > ")
for caracter in nombre:
	if	caracter == "a" or caracter == "A":
		contador_vocales += 1
	
	elif caracter == "e" or caracter == "E":
		contador_vocales += 1
	
	elif caracter == "i" or caracter == "I":
		contador_vocales += 1
	
	elif caracter == "o" or caracter == "O":
		contador_vocales += 1

	elif caracter == "u" or caracter == "U":
		contador_vocales += 1

	else:
		contador_consonantes += 1
	
	print ("%s" % caracter, end="|")

print ("")
print ("""Tu nombre esta compuesto por [ %d] numero de vocales y [ %d ] 
		numero de consonantes""" % (contador_vocales, contador_consonantes))

#! /usr/bin/python3
# -*- coding:utf-8 -*-
# impresion de puros numeros pares e impares
for numero in range(0,10):
	print ("\t %d" % numero, end="|")

print ("\n")

for numero_par in range(0,12,2):
	print ("\t %d es un numero par" % numero_par)

#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Excepciones con paso de parametros
import sys

for arg in sys.argv[1:]:
	try:
		archivo = open(arg, "r")
	except IOError:
		print ("No se puede abrir", arg)
	else:
		print (arg,"tiene",len(archivo.readlines()), "lineas")
		archivo.close()

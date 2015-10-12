#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Levantando Excepciones

try:
	raise NameError("Hola Mundo Piñata")
except NameError:
	print ("Sucedio una excepcion Piñata")
	raise

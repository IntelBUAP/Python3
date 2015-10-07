#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Iterando diccionarios usando for
distribuciones = {"Ubuntu":14.10, "Fedora":21, "Suse":13.3, 
	"Debian":7.8, "CentOS":7.1}
print ("Muestra cada par (identificador, valor) del diccionario")
for elemento in distribuciones.items():
	print (elemento)

print ("Muestra el contenido de identificador del Diccionario")
for identificador in distribuciones.keys():
	print (identificador)

print ("Muestra cada valor del diccionario")
for valor in distribuciones.values():
	print (valor)

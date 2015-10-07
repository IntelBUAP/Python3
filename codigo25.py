#! /usr/bin/python3
# -*- coding:utf-8 -*-
# usando funciones
Pi = 3.141592653589793
def perimetro_circulo(radio):
	return ( Pi * ( radio ** 2 ))

radio = eval(input("Ingresa el radio del circulo > "))
print ("El perimetro del circulo es [ %f ]" % perimetro_circulo(radio))


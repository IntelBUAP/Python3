#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Validar_Contraseña
import sys
try:
    while (1):
        Cadena = input("Ingrese su contraseña: ")

        if(len(Cadena) < 8):
            print ("La contraseña debe tener al menos 8 caracteres.")
        elif(Cadena.isalpha()):
            print ("La contraseña debe ser Alfanumerica.")
        elif(Cadena.isdigit()):
            print ("La contraseña debe ser Alfanumerica.")
        elif(Cadena.isalnum() and " " not in Cadena):
            print ("TRUE")
            break
        else:
            print ("La contraseña no puede tener espacios")
except(ValueError, EOFError, KeyboardInterrupt, NameError):
        print ("Error:", sys.exc_info()[0])
        raise
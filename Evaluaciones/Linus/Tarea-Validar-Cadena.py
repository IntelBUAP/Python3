#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Validar_Usuario
import sys
try:
    while (1):
        Cadena = input("Ingrese el nombre de Usuario: ")
        if(len(Cadena) < 6):
            print ("El nombre de usuario debe contener al menos 6 caracteres.")
        elif(len(Cadena) > 12):
            print ("El nombre de usuario no puede contener mas de 12 caracteres.")
        elif(Cadena.isalpha()):
            print ("El nombre de usuario debe ser Alfanumerico.")
        elif(Cadena.isdigit()):
            print ("El nombre de usuario debe ser Alfanumerico.")
        elif(Cadena.isalnum()):
            print ("TRUE")
            break
        else:
            print ("El nombre de usuario solo puede contener letras y números.")
except(ValueError, EOFError, KeyboardInterrupt, NameError):
        print ("Error :", sys.exc_info()[0])
        raise
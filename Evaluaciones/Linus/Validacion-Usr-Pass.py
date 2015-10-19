#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Validar_Usuario_Contraseña
import sys

def ValidaUsuario(Cadena):
        if(len(Cadena) < 6):
            print ("El nombre de usuario debe contener al menos 6 caracteres.")
        elif(len(Cadena) > 12):
            print ("El nombre de usuario no puede contener mas de 12 caracteres.")
        elif(Cadena.isalpha()):
            print ("El nombre de usuario debe ser Alfanumerico.")
        elif(Cadena.isdigit()):
            print ("El nombre de usuario debe ser Alfanumerico.")
        elif(Cadena.isalnum()):
            print ("Usuario Correcto")
            return True
        else:
            print ("El nombre de usuario solo puede contener letras y números.")

def ValidaContraseña(Cadena):
        if(len(Cadena) < 8):
            print ("La contraseña debe tener al menos 8 caracteres.")
        elif(Cadena.isalpha()):
            print ("La contraseña debe ser Alfanumerica.")
        elif(Cadena.isdigit()):
            print ("La contraseña debe ser Alfanumerica.")
        elif(Cadena.isalnum() and " " not in Cadena):
            print ("Contraseña correcta")
            return True
        else:
            print ("La contraseña no puede tener espacios")

try:
    while(1):
        Cadena = input("Ingrese el nombre de Usuario:")
        Cadena2 = input("Ingrese Contraseña:")
        if(ValidaUsuario(Cadena) and ValidaContraseña(Cadena2)):
            print ("Datos Correctos")
            break
        else:
            print ("Datos incorrectos")

except(ValueError, EOFError, KeyboardInterrupt, NameError):
        print ("Error:", sys.exc_info()[0])
        raise
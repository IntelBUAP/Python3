#! /usr/bin/python3
import re

err = "La contraseña no es segura"
msg = "Escriba una contraseña al menos 8 caracteres alfanumericos"


def ismayor8(a):
    """
    Compara si es mayor a 8 caracteres
    """
    if (len(a) < 8):
        return False
    return True


def minus(a):
    """
    compara si existe alguna letra minuscula
    """
    patron = ('[a-z]')
    flag = False
    for letra in a:
        if (re.match(patron, letra)):
            flag = True
    return flag


def mayus(a):
    """
    Compara si existe alguna letra mayuscula
    """
    patron = ('[A-Z]')
    flag = False
    for letra in a:
        if (re.match(patron, letra)):
            flag = True
    return flag


def unnum(a):
    """
    Compara si existe algun número
    """
    patron = ('[0-9]')
    flag = False
    for letra in a:
        if (re.match(patron, letra)):
            flag = True
    return flag


def alfanumeric(a):
    """
    Compara si la cadena es alfanumerica
    """
    if (a.isalnum()):
        return True
    else:
        return False


def vpass():
    """
    Validamos contraseña
    """
    salida = False
    while salida is False:
        try:
            print (msg, end='\n')
            paswd = str(input('passwd: '))
            if (ismayor8(paswd)):
                if (alfanumeric(paswd)):
                    if (minus(paswd) and mayus(paswd) and unnum(paswd)):
                        salida = True
                    else:
                        print (err, end='\n')
            else:
                print (err, end='\n')
        except (KeyboardInterrupt, EOFError):
            print (msg, end='\n')
    return salida

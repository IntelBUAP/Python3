import os

def validacion(usuario):
    tam = len(usuario)
    minusculas = 0
    mayusculas = 0
    numeros = 0
    if tam < 13:
        if tam > 5:
            if usuario.isalnum():
                for letra in range(0, tam):
                    if usuario[letra].islower():
                        minusculas += 1
                    elif usuario[letra].isupper():
                        mayusculas += 1
                    elif usuario[letra].isdigit():
                        numeros += 1
                if (minusculas == 0 and mayusculas == 0) or numeros == 0:
                    print("El nombre de usuario debe contener letras y números")
                    return False
                else:
                    print ("True")
                    return True
            else:
                print("El nombre de usuario solo puede contener letras y números")
                return False
        else:
            print("El nombre de usuario debe contener al menos 6 caracteres.")
            return False
    else:
        print("El nombre de usuario no puede contener mas de 12 caracteres.")
        return False


def validacioncon(contra):
    tam = len(contra)
    minusculas = 0
    mayusculas = 0
    numeros = 0
    if tam > 7:
        for letra in range(0, tam):
            if contra[letra].islower():
                minusculas += 1
            elif contra[letra].isupper():
                mayusculas += 1
            elif contra[letra].isdigit():
                numeros += 1
            elif contra[letra].isspace():
                print("La contraseña no puede tener espacios en blanco")
                return False
        if minusculas == 0 or mayusculas == 0 or numeros == 0:
            print("La contraseña no es segura")
            return False
        else:
            print ("True")
            return True
    else:
        print("La contraseña debe contener al menos 8 caracteres.")
        return False

bandera = 0
while bandera != 1:
    try:
        usuario = input("Usuario: ")
        valida = validacion(usuario)
        while valida is False:
            usuario = input("Usuario: ")
            valida = validacion(usuario)
        if valida == True:
            bandera = 1
    except (EOFError, KeyboardInterrupt):
        print ("ERROR")

bandera = 0
while bandera != 1:
    try:
        contra = input("Contraseña: ")
        validacon = validacioncon(contra)
        while validacon is False:
            contra = input("Contraseña: ")
            validacon = validacioncon(contra)
        if validacon == True:
            bandera = 1
    except (EOFError, KeyboardInterrupt):
        print ("ERROR")

bandera = 0
while bandera != 1:
    try:
        os.system('clear')
        print ("Comprobando usuario y contraseña")
        vusuario = input("Ingrese usuario ")
        vcontra = input ("Ingrese contraseña ")
        while vusuario != usuario or vcontra != contra:
            os.system('clear')
            print ("Usuario o contraseña incorrecto")
            vusuario = input("Ingrese usuario ")
            vcontra = input ("Ingrese contraseña ")
        if vusuario == usuario and vcontra == contra:
            print ("Bienvenido usuario y contraseña correctos")
            bandera = 1
    except (EOFError, KeyboardInterrupt):
        print ("ERROR")

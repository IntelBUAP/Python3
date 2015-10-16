# -*- coding:utf-8 -*-
##definicion de funcion


def password(contra):
    size = len(contra)

    a = [False] * 4

    if not(size >= 8 and contra.find(' ') == -1 and contra.isalnum()):
        return False

    for i in range(0, size):
        if contra[i].islower():
            a[0] = True
        elif contra[i].isupper():
            a[1] = True
        elif contra[i].isdigit():
            a[2] = True

        if (a[0] and a[1] and a[2]):
            return True

    return False


def valuser(nameusr):

#    try:
        minC = len(nameusr)
        b = [0] * 3
        if minC >= 6 and minC <= 12 and nameusr.find(' ') == -1:
            b[0] = 1  # min
            b[1] = 1  # max
            #print("tamao y sin espacios")

            if nameusr.isalnum():
                b[2] = 1

            if b[0] and b[1] and b[2]:
                return True
            else:
                b[2] = 0
                print("El nombre de usuario solo puede"
                                "contener numeros y letras")

        elif minC < 6:
            b[0] = 0
            print("El nombre de usuario debe contener al menos 6 caracteres")

        elif minC > 12:
            b[1] = 0
            print("El nombre de usuario no puede tener mas de 12 caracteres")
        else:
            b[0] = 1  # min
            b[1] = 1  # max
            b[2] = 0
            print("la contraseña no es segura")

##Implementacion

try:
    test = valuser(input("usuario: "))
    if test:
        prueb = password(input("Contraseña: "))
        if prueb:
            print("True")
        else:
            print("La contraseña no es segura")
    else:
        print("Usuario invalido")

except (ValueError, EOFError, KeyboardInterrupt, AttributeError):
    print("Tienes que insertar un numero entero valido")
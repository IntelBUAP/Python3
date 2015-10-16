#! /usr/bin/python3

msg1 = "Escriba un nombre de usuario de 6 a 12 caracteres alfanumericos"

def ismayor6(a):
    """
    Compara si la cadena contiene al menos 6 caracteres
    """
    if (len(a) < 6):
        print ('El nombre de usuario debe contener al menos 6 caracteres', end='\n')
        return False
    return True


def ismenor12(a):
    """
    Compara si la cadena contiene a lo mas 12 caracteres
    """
    if (len(a) > 12):
        print ('El nombre de usuario no puede contener mas de 12 caracteres.', end='\n')
        return False
    return True


def alfanumeric(a):
    """
    Compara si la cadena es alfanumerica
    """
    if (a.isalnum()):
        return True
    else:
        print ('No es Alfanumerica', end='\n')
        return False


def vuser():
    """
    solicitamos usuario y validamos
    """
    salida = False
    while salida is False:
        try:
            print (msg1, end='\n')
            user = str(input('User: '))
            if (ismenor12(user) and ismayor6(user) and alfanumeric(user)):
                salida = True
            else:
                print ('Intente nuevamente...', end='\n')
        except (KeyboardInterrupt, EOFError):
            print (msg1, end='\n')
    return salida
#! /usr/bin/python3
import math
import os


def suma(a, b):
    r = a + b
    return r


def resta(a, b):
    r = a - b
    return r


def multi(a, b):
    r = a * b
    return r


def divi(a, b):
    r = a / b
    return r


def expo(a, b):
    r = a ** b
    return r


def loga(a):
    r = math.log(a, 10)
    return r


def seno(a):
    r = math.sin(a)
    return r


def coseno(a):
    r = math.cos(a)
    return r


def tangente(a):
    r = math.tan(a)
    return r


def aseno(a):
    r = math.asin(a)
    return r


def acoseno(a):
    r = math.acos(a)
    return r


def atangente(a):
    r = math.tanh(a)
    return r


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("clc")
        
def leerDosValores():
	 operando1 = eval(input('{:80}'.format('Primer valor ')))
	 operando2 = eval(input('{:80}'.format('Segundo valor: ')))
	 return (operando1, operando2)


def leerValor():
	 operando1 = eval(input('{:80}'.format("Valor: ")))
	 return (operando1)
	
salida = False
while salida is False:
    print ('{:*^80}'.format("Calculadora"))
    print ('{:*^80}'.format("1. suma", end='\n'))
    print ('{:*^80}'.format("2. resta", end='\n'))
    print ('{:*^80}'.format("3. multiplicación", end='\n'))
    print ('{:*^80}'.format("4. división", end='\n'))
    print ('{:*^80}'.format("5. x elevado a la y", end='\n'))
    print ('{:*^80}'.format("6. Logaritmo base 10", end='\n'))
    print ('{:*^80}'.format("7. seno", end='\n'))
    print ('{:*^80}'.format("8. coseno", end='\n'))
    print ('{:*^80}'.format("9. tangente", end='\n'))
    print ('{:*^80}'.format("10. arco seno", end='\n'))
    print ('{:*^80}'.format("11. arco coseno", end='\n'))
    print ('{:*^80}'.format("12. arco tangente", end='\n'))
    print ('{:*^80}'.format(" ---", end='\n'))
    print ('{:*^80}'.format("20. Salir", end='\n'))
    try:
        op = eval(input('{:80}'.format('Selecciona: ')))
        if op == 1:
            operando1, operando2 = leerDosValores()
            print (suma(operando1, operando2))
        elif op == 2:
            operando1, operando2 = leerDosValores()
            print (resta(operando1, operando2))
        elif op == 3:
            operando1, operando2 = leerDosValores()
            print (multi(operando1, operando2))
        elif op == 4:
            operando1, operando2 = leerDosValores()
            print (divi(operando1, operando2))
        elif op == 5:
            operando1, operando2 = leerDosValores()
            print (expo(operando1, operando2))
        elif op == 6:
            operando1 = eval(input("Valor: "))
            print (loga(operando1))
        elif op == 7:
            operando1 = eval(input("Valor: "))
            print (seno(operando1))
        elif op == 8:
            operando1 = eval(input("Valor: "))
            print (coseno(operando1))
        elif op == 9:
            operando1 = eval(input("Valor: "))
            print (tangente(operando1))
        elif op == 10:
            operando1 = eval(input("Valor: "))
            print (aseno(operando1))
        elif op == 11:
            operando1 = eval(input("Valor: "))
            print (acoseno(operando1))
        elif op == 12:
            operando1 = eval(input("Valor: "))
            print (atangente(operando1))
        elif op == 20:
            print ("Adios")
            salida = True
        else:
            print ("Opción no valida")
            break
    except ValueError:
        print ("Ooop! No es valor valido")
    except (KeyboardInterrupt, EOFError):
        print ("Para salir, seleccione la opción de Salida en el menú")
    except ZeroDivisionError:
        print ("Division entre cero no existe")
    except NameError:
        print("Opcion no valida")
    print ("Presione una tecla para continuar")
    input()
    clear()

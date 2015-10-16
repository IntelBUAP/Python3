#yolanda alvarez
#pedro ambrosio
#ignacio acevedo
#raul arias
#monica canizo

import os
import math


def suma():
    try:
        print ('{:^30}'.format('SUMA'))
        num1 = int(input("Valor a: "))
        num2 = int(input("Valor b: "))
        print ('{} + {} = {}'.format(num1, num2, num1 + num2))
        input(" ")
    except ValueError:
        print ("Introduzca solo numeros ")


def resta():
    try:
        print ('{:^30}'.format('RESTA'))
        num01 = int(input("Valor a: "))
        num02 = int(input("Valor b: "))
        print ('{} - {} = {}'.format(num01, num02, num01 - num02))
        input(" ")
    except ValueError:
        print("Introduzca solo numeros")


def div():
    try:
        print ('{:^30}'.format('DIVISION'))
        num1 = int(input("Valor a: "))
        num2 = int(input("Valor b: "))
        res = num1 / num2
        print ('{} / {} = {}'.format(num1, num2, res))
        input(" ")
    except ZeroDivisionError:
        print ("Error: Division entre cero ")
    except ValueError:
        print("Introduzca solo numeros")


def multi():
    try:
        print ('{:^30}'.format('MULTIPLICACION'))
        num1 = int(input("Valor a: "))
        num2 = int(input("Valor b: "))
        print ('{} * {} = {}'.format(num1, num2, num1 * num2))
        input(" ")
    except ValueError:
        print("Introduzca solo numeros")


def exponente():
    try:
        print ('{:^30}'.format('EXPONENTE'))
        num01 = int(input("Número : "))
        num02 = int(input("Exponente : "))
        print ('{} ^ {} = {}'.format(num01, num02, num01 ** num02))
        input(" ")
    except ValueError:
        print("Introduzca solo numeros")


def logaritmo():
    try:
        print ('{:^30}'.format('LOGARITMO'))
        num01 = int(input("Logaritmo: "))
        num02 = int(input("Base: "))
        aux = math.log(num01, num02)
        print ('log({}) = {}'.format(num01, float(aux)))
        input(" ")
    except ValueError:
        print("Introduzca solo numeros")


def seno():
    try:
        print ('{:^30}'.format('SENO'))
        grados = int(input("Ingresa grados: "))
        im= math.sin(math.radians(grados))
        print ('sin({}) = {}'.format(grados, im))
        input(" ")
    except ValueError:
        print("Introduzca solo numeros")


def coseno():
    try:
        print ('{:^30}'.format('COSENO'))
        grados = int(input("Ingresa grados: "))
        im= math.cos(math.radians(grados))
        print ('cos({}) = {}'.format(grados, im))
        input(" ")
    except ValueError:
        print("Introduzca solo numeros")


def tangente():
    try:
        print ('{:^30}'.format('TANGENTE'))
        num01 = int(input("Ingresa grados: "))
        aux = math.tan(math.radians(num01))
        print ('tan({}) = {}'.format(num01, aux))
        input(" ")
    except ValueError:
        print("Introduzca solo numeros")


def inverso():
    try:
        print ('{:^30}'.format('INVERSO'))
        num1 = int(input("Valor: "))
        print (' {} = {}'.format(num1, num1 * (-1)))
        input(" ")
    except ValueError:
        print("Introduzca solo numeros")


opcion = 0
while opcion != 11:
    try:
        os.system('clear')
        print ('{:^50}'.format('Calculadora'))
        print ('{:^50}'.format('1. Suma'))
        print ('{:^50}'.format('2. Resta'))
        print ('{:^50}'.format('3. Division'))
        print ('{:^50}'.format('4. Multiplicacion'))
        print ('{:^50}'.format('5. Exponente'))
        print ('{:^50}'.format('6. Log'))
        print ('{:^50}'.format('7. Seno'))
        print ('{:^50}'.format('8. Coseno'))
        print ('{:^50}'.format('9. Tangente'))
        print ('{:^50}'.format('10. Inverso'))
        print ('{:^50}'.format('11. Salir'))

        if opcion == 1:
            suma()

        if opcion == 2:
            resta()

        if opcion == 3:
            div()

        if opcion == 4:
            multi()

        if opcion == 5:
            exponente()

        if opcion == 6:
            logaritmo()

        if opcion == 7:
            seno()

        if opcion == 8:
            coseno()

        if opcion == 9:
            tangente()

        if opcion == 10:
            inverso()

        opcion = int(input("Ingresa opcion: "))

    except ValueError:
        print("Introduzca solo numeros")
    except (EOFError, KeyboardInterrupt):
        print ("ERROR")

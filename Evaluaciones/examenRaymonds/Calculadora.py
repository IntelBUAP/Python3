import signal
import sys
import os
import math

def suma(x, y):
    return x+y

def resta(x, y):
    return x-y

def multiplicacion(x, y):
    return x*y

def division(x, y):
 try:
  resultado=x/y
 except ZeroDivisionError:
   print("Division entre cero no existe")
 else:
   return resultado

def exponente(x, y):
    return x**y

def logaritmo(x):
 try:
  loga = math.log(x)
 except ValueError:
    print("No hay logaritmo de cero")
 else:
   return loga


def seno(n):

    try:
        return math.sin(math.radians(n))
    except TypeError:
        return "Error de tipo de dato"


def arcoSeno(n):
    try:
        return math.asin(math.radians(n))
    except ValueError:
        return "Error de valor"
    except TypeError:
        return "Error de tipo de dato"


def coseno(n):
    try:
        return math.cos(math.radians(n))
    except TypeError:
        return "Error de tipo de dato"


def arcoCoseno(n):
    try:
        return math.acos(math.radians(n))
    except ValueError:
        return "Error de valor"
    except TypeError:
        return "Error de tipo de dato"


def tangente(n):
    try:
        return math.tan(math.radians(n))
    except TypeError:
        return "Error de tipo de dato"


def arcoTangente(n):
    try:
        return math.atan(math.radians(n))
    except TypeError:
        return "Error de tipo de dato"


ans=True
t=70
while ans:
    try:
        os.system('clear')
        #stri="1.Suma\n2.Resta\n3.Multilicacion\n4.Division\n5.Exponente\n6.Log\n7.Seno\n8.Coseno\n9.Tangente\n10.Seno Inverso\n11.Coseno Inverso\n12.Tangente Inverso\n13.Salir"

        print("1.Suma".center(t," "))
        print("2.Resta".center(t," "))
        print("3.Multiplicacion".center(t," "))
        print("4.Division".center(t," "))
        print("5.Exponente".center(t," "))
        print("6.Logaritmo".center(t," "))
        print("7.Seno".center(t," "))
        print("8.Coseno".center(t," "))
        print("9.Tangente".center(t," "))
        print("10.ArcoSeno".center(t," "))
        print("11.ArcoCoseno".center(t," "))
        print("12.ArcoTangente".center(t," "))
        print("13.Salir".center(t," "))
        ans=input("Que operacion deseas hacer?\n".center(t," "))


        if ans=="1":
          print("\n Suma")
          x=float(input("Dame el valor x? "))
          y=float(input("Dame el valor y? "))
          print(suma(x,y))

        elif ans=="2":

          print("\n Resta")
          x=float(input("Dame el valor x? "))
          y=float(input("Dame el valor y? "))
          print(resta(x,y))

        elif ans=="3":
          print("\n Multilicacion")
          x=float(input("Dame el valor x? "))
          y=float(input("Dame el valor y? "))
          print(multiplicacion(x,y))

        elif ans=="4":
          print("\n Division")
          x=float(input("Dame el valor x? "))
          y=float(input("Dame el valor y? "))
          print(division(x,y))

        elif ans=="5":
          print("\n Exponente")
          x=float(input("Dame la base? "))
          y=float(input("Dame el exponente? "))
          print(exponente(x,y))

        elif ans=="6":
          print("\n Log")
          x=float(input("Dame el valor x? "))
          print(logaritmo(x))

        elif ans=="7":
          print("Seno")
          n=float(input("Dame el valor n? "))
          print((seno(n)))

        elif ans=="8":
          print("\n Coseno")
          n=float(input("Dame el valor n? "))
          print(coseno(n))

        elif ans=="9":
          print("\n Tangente")
          n=float(input("Dame el valor n? "))
          print(tangente(n))

        elif ans=="10":
          print("\n Seno Inverso")
          n=float(input("Dame el valor n? "))
          print(arcoSeno(n))

        elif ans=="11":
          print("\n Coseno Inverso")
          n=float(input("Dame el valor n? "))
          print(arcoCoseno(n))

        elif ans=="12":
          print("\n Tangente Inverso")
          n=float(input("Dame el valor n? "))
          print(arcoTangente(n))

        elif ans=="13":
          print("\n Adios")
          ans=False
        elif ans !="":
          print("\n Opcion no valida, intenta de nuevo")
        input(" Presiona enter ")

    except (EOFError, KeyboardInterrupt):
        print("A donde vas conejo blaz")
    except ValueError:
        print("Dato invalido")
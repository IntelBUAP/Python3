#! /usr/bin/python3
# -*- coding:utf-8 -*-
import os 
import time
import math
numero = 0
opc = 1
result = 0
dato1 = 0;
dato2 = 0;
resultado = 0;
while (opc >0 and opc <13):
    try:
        #os.system("clear");
        print("Calculadora Menu".center(80," "))
        print("1) Suma".center(80," "))
        print("2) Resta".center(80," "))
        print("3) Multiplicacion".center(80," "))
        print("4) Division".center(80," "))
        print("5) Exponente".center(80," "))
        print("6) Log".center(80," "))
        print("7) Sen".center(80," "))
        print("8) Cos".center(80," "))
        print("9) Tan".center(80," "))
        print("10) arcoseno".center(80," "))
        print("11) arcosecante".center(80," "))
        print("12) arcotangente".center(80," "))
        print("13) Salir".center(80," "))
        opc = int(input("Ingresa Opcion: "))

        if opc == 1:     
            print ("Suma")
            dato1 = int(input("Ingrese el primer numero: "));
            dato2 = int(input("Ingrese el segundo numero: "));
            resultado = (dato1 + dato2);
            print ('{:d}'.format(resultado));
            time.sleep(2)
            os.system("clear");

        elif opc == 2:
            print ("Resta")
            dato1 = int(input("Ingrese el primer numero: "));
            dato2 = int(input("Ingrese el segundo numero: "));
            resultado = (dato1 - dato2);
            print ('{:d}'.format(resultado));
            time.sleep(2)
            os.system("clear");

        elif opc == 3:
            print ("Multiplicacion")
            dato1 = int(input("Ingrese el primer numero: "));
            dato2 = int(input("Ingrese el segundo numero: "));
            resultado = (dato1 * dato2);
            print ('{:d}'.format(resultado));
            time.sleep(2)
            os.system("clear");

        elif opc == 4:
            print ("Division")
            dato1 = int(input("Ingrese el primer numero: "));
            dato2 = int(input("Ingrese el segundo numero: "));
            resultado = (dato1 / dato2);
            print ('{:f}'.format(resultado));
            time.sleep(2)
            os.system("clear");

        elif (opc == 5):
            print ("Potencia")
            x = int(input("Ingrese un Numero: "))
            y = int(input("Ingrese potencia: "))
            result = math.pow(x,y)
            print ('{:3.3f}'.format(result))
            time.sleep(2)
            os.system("clear");
        
        elif(opc == 6):
            print ("Logaritmo")
            print ("log(x)/log(base)")
            x = int(input("Ingrese el valor x: "))
            base = int(input("Ingrese el valor base: "))
            result = math.log(x,base)
            print ('{:3.3f}'.format(result))
            time.sleep(2)
            os.system("clear");

        elif (opc == 7):
            print ("Seno")
            x = int(input("Ingrese un Numero: "))
            print ('{:f}'.format(math.sin(x)))  
            time.sleep(2)
            os.system("clear");

        elif (opc == 7):
            print ("Coseno")
            x = int(input("Ingrese un Numero: "))
            print ('{:f}'.format(math.cos(x)))
            time.sleep(2)
            os.system("clear");

        elif (opc == 9):
            print ("Tangente")
            dato1 = int(input("Ingrese un Numero: "))
            resultado = math.tan(dato1);
            print("tan {:3.3f}".format(resultado));
            time.sleep(2)
            os.system("clear");

        elif (opc == 10):
            print ("arc seno")
            dato1 = int(input("Ingrese un Numero 0 y 1: "))
            resultado = math.asin(dato1);
            print("arc sen {:3.3f}".format(resultado));
            time.sleep(2)
            os.system("clear");

        elif (opc == 11):
            print ("arc coseno")
            dato1 = int(input("Ingrese un Numero 0 y 1: "))
            resultado = math.acos(dato1);
            print("arc cos {:3.3f}".format(resultado));
            time.sleep(2)
            os.system("clear");

        elif (opc == 12):
            print ("arc tangente")
            dato1 = int(input("Ingrese un Numero: "))
            resultado = math.atan(dato1);
            print("arc tan {:3.3f}".format(resultado));
            time.sleep(2)
            os.system("clear"); 

    except KeyboardInterrupt:
        print ("Intentalo nuevamente")
    except ValueError:
        print ("Valor no valido")
    except ZeroDivisionError:
        print ("Division sobre 0")

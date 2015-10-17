#!/usr/bin/python3
#calculadora Cientifica!
#librerias a importar
from time import sleep
from os import system
from math import log, sin, cos, tan, asin, acos, atan

#definicion de funciones
def Suma( x,y ):
    return x + y
    
def Resta( x,y ):
    return x - y
    
def Multiplicacion( x,y ):
    return x * y
    
def Division( x,y ):
    return x / y
    
def Exponente( x,y ):
    return x ** y
    
def Log( x ):
    return  log(x) 
    
def Seno( x ):
    return sin(x) 
    
def Coseno( x ):
    return cos(x) 
	
def Tangente( x ):
    return tan(x)
   
def aSeno( x ):
    return asin(x) 
    
def aCoseno( x ):
    return acos(x) 
	
def aTangente( x ):
    return atan(x)
    
opc = 0

#menu
while True:
	try:
		print ('{:^80}'.format('Calculadora Científica'))
		print ('{:^80}'.format('1.suma'))
		print ('{:^80}'.format('2.resta'))
		print ('{:^80}'.format('3.multiplicación'))
		print ('{:^80}'.format('4.división'))
		print ('{:^80}'.format('5.exponente'))
		print ('{:^80}'.format('6.logaritmo'))
		print ('{:^80}'.format('7.seno'))
		print ('{:^80}'.format('8.seno invertido'))
		print ('{:^80}'.format('9.coseno'))
		print ('{:^80}'.format('10.coseno invertido'))
		print ('{:^80}'.format('11.tangente'))
		print ('{:^80}'.format('12.tangente invertido'))
		print ('{:^80}'.format('13. SALIR'))
		opc=int(input("ingrese una opcion:"))
		system('clear')
		if opc == 1:
			num1 = eval(input("ingresa a ="))
			num2 = eval(input("ingresa b ="))
			print ("suma de {} + {} = {}".format(num1,num2,Suma(num1,num2)))
		
		elif opc ==2 :
			num1 = eval(input("ingresa a ="))
			num2 = eval(input("ingresa b ="))
			print ("resta de {} - {} = {}".format(num1,num2,Resta(num1,num2)))
		
		elif opc ==3 :
			num1 = eval(input("ingresa a ="))
			num2 = eval(input("ingresa b ="))
			print ("multiplicación de {} X {} = {}".format(num1,num2,Multiplicacion(num1,num2)))

		elif opc ==4 :
			num1 = eval(input("ingresa a ="))
			num2 = eval(input("ingresa b ="))
			print ("división de {} / {} = {}".format(num1,num2,Division(num1,num2)))

		elif opc ==5 :
			num1 = eval(input("ingresa a ="))
			num2 = eval(input("ingresa b ="))
			print ("exponte de {} ^ {} = {}".format(num1,num2,Exponente(num1,num2)))
	
		elif opc ==6 :
			num1 = eval(input("ingresa a ="))
			print ("logaritmo ({}) = {} ".format(num1,Log(num1)))

		elif opc ==7 :
			num1 = eval(input("ingresa a="))
			print ("seno ({}) = {} ".format(num1,Seno(num1)))

		elif opc ==8 :
			num1 = eval(input("ingresa a="))
			print ("seno invertido ({}) = {} ".format(num1,aSeno(num1)))
	
		elif opc ==9 :
			num1 = eval(input("ingresa a="))
			print ("coseno ({}) = {} ".format(num1,Coseno(num1)))

		elif opc ==10 :
			num1 = eval(input("ingresa a="))
			print ("coseno invertido ({}) = {} ".format(num1,aCoseno(num1)))

		elif opc ==11 :
			num1 = eval(input("ingresa a="))
			print ("tangente ({}) = {} ".format(num1,Tangente(num1)))

		elif opc ==12 :
			num1 = eval(input("ingresa a="))
			print ("tangente invertida ({}) = {} ".format(num1,aTangente(num1)))
	
		elif opc ==13 :
			break
		else :
			print ("opcion no valida")
	#excepciones
	except ValueError as x:
		print("\nError {}: ".format(x))
	except (ZeroDivisionError):
		print("\nError Division entre 0")
	except (KeyboardInterrupt, EOFError):
		print("\nPara salir intente la opcion 13")
	except (NameError):
		print("\nError de tipo de dato")
	sleep(2)
	system('clear')


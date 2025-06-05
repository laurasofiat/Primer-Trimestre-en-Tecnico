edad=int(input("Ingrese su edad:"))
if edad>=18: #El if=si, se cumple esa función.
    print("Usted es mayor de edad")
else: print("Usted es menor de edad") #El else=si no, se cumple esa función.
print("---------------------------------------------")
com=input("¿Usted come carne(sí o no)?")
if com=="no": #Se pueden hacer multiples ifs, lo cual sería identación logrando una sentencia.
    print("Usted es vegetariano o vegano.")
else: print("Usted no es vegano o vegetariano.")
print("---------------------------------------------")
x=int(input("Ingrese un número entero:"))
if x>=50:
    print("El número es mayor a 50.")
else: print("El número está por debajo del 50.")
print("---------------------------------------------")
m1=int(input("Ingrese un número entero:"))
m2=int(input("Ingrese un número entero:"))
mul=m1*m2
print(mul)
if mul<500:
    print("El resultado de la multiplicación es un número menor a 500.")
elif mul>=500 and mul<=999: #El elif=si no,si
    print("El resultado de la multiplicación es un número mayor a 500.")
elif mul>=1000:
     print("El resultado de la multiplicación es un número mayor a 1000.")
else: print("El resultado de la multiplicación es un número grande.")
print("---------------------------------------------")
#Programa creado.
print("Generaciones digitales.")
año=int(input("Ingrese su año de nacimiento:"))
if año>=1920 and año<=1945:
    print("Usted es de la generación silenciosa.")
elif año>=1946 and año<=1964:
     print("Usted es de la generación Bommer.")
elif año>=1965 and año<=1979:
    print("Usted es de la generación X.")
elif año>=1980 and año<=2000:
    print("Usted es de la generación Y.")
elif año>=2011 and año<=2010:
    print("Usted es de la generación Z.")
elif año>2010:
    print("Usted es de la generación de Nativos Digitales.")
else: print("¿Usted si nació en ese año?-Retifique y modifique su fecha de nacimiento.")
print("---------------------------------------------")











print("Ejercicios condicionales y Operaciones matemáticas.")
print("Ejercicio 1")
v1=float(input("Ingrese un número:"))
if v1==0:
    print("El número ingresado es cero.")
elif v1>=1:
    print("El número ingresado es positivo.")
elif v1<=-1:
    print("El número ingresado es negativo.")
print("---------------------------------------------------")
print("Ejercicio 2")
v2=float(input("Ingrese un número:"))
v3=float(input("Ingrese un número:"))
if v2>v3:
    print("El número primer número ingresado es mayor al segundo número ingresado.")
elif v2<v3:
    print("El número primer número ingresado es menor al segundo número ingresado.")
print("---------------------------------------------------")
print("Ejercicio 3")
v=float(input("ingrese un número:"))
if v %2==0:
    print("El número es par.")
else: print("El número es impar.")
print("---------------------------------------------------")
print("Ejercicio 4")
v=int(input("Ingrese un número:"))
if v>=10 and v<=20: #and=y---Es una condición.
    print("El número se encuentra entre 10 y 20.")
else: print("El número no se encuentra entre 10 y 20.")
print("---------------------------------------------------")
print("Ejercicio 5")
v4=float(input("Ingrese un número:"))
v5=float(input("Ingrese un número:"))
v6=float(input("Ingrese un número:"))
if v4>v5 and v4>v6:
    print(v4,"Es el número mayor.")
elif v5>v4 and v5>v6:
    print(v5,"Es el número mayor.")
else: print(v6,"Es el número mayor.")
print("---------------------------------------------------")
print("Ejercicio 6.")
v7=float(input("Ingrese precio:"))
if v7>=100:
    rs=(10/v7)*100
    print("El 10 porciento de 100 es:",rs)
else: print("El número no cumple con los requisitos,no se calculará porcentaje.")
print("---------------------------------------------------")
print("Ejercicio 7")
v8=input("¿Cuántos años tienes?")
if v8>=18:
    print("Puedes votar.")
else: print("No cumple con los requisitos, no puede votar.")
print("---------------------------------------------------")
print("Ejercicio 8")
v9=float(input("Ingrese precio:"))
v10=input("¿Usted es cliente VIP o normal?")
if v10=="VIP" or v10=="vip":
    rs1=(20/v9)*100
    print("El descuento se ha realizado,descuento de:",rs1,"%")
else: print("No cumple con los requisitos, no se hará descuento de 20%")
print("---------------------------------------------------")
print("Ejercicio 9")
v11=float(input("Ingrese un número:"))
if v11 %5==0 and  v11 %3==0: #El % se utiliza para encontrar un divisor de un número.
    print("El número ingresado es multiplo de 3 y 5.")
else: print("El número ingresado no es multiplo de 3 y 5.")
print("---------------------------------------------------")
print("Listas y Condicionales")
print("Ejercicio 10")
v12=float(input("Ingrese un número:"))
if v12%2==0 and v12%4==0:
    print("El número ingresado se puede dividir entre 2 y 4.")
else: print("El número ingreado no se puede dividir entre 2 y 4.")
print("-----------------------------------------------------")
print("Ejercicio 11")
lis1=[2,4,6,8,10]
print(lis1)
vv=lis1[2]
print(vv)
if vv>10:
    print("El número 6 es mayor a 10.")
else: print("El número 6 no es mayor a 10.")
print("-----------------------------------------------------")
print("Ejercicio 12")
lis2=[3,5,7,9]
print(lis2)
vv1=lis2.index==7
if vv1=="true":
    print(" Está en la lista.")
else: print("No está en la lista.")
print("-----------------------------------------------------")
print("Ejercicico 13")
lis3=[4,6,2,8]
print(lis2)
vv2=lis3[0]+lis3[3]
print(vv2)
if vv2>=10:
    print("Suma alta.")
else: print("Suma baja.")
print("-----------------------------------------------------")
print("Ejercicio 14")
lis4= ["Ana", "Luis", "Pedro", "Marta"]
print(lis4)
vv3=lis4[3]
print(vv3)
if vv3=="Marta":
    print("Nombre correcto")
else: print("Nombre diferente")
print("-----------------------------------------------------")
print("Ejercicico 15")
lis5=[input("Ingrese un color:"),input("Ingrese un color:"),input("Ingrese un color:")]
print(lis5)
if lis5[2]=="azul" or lis5[2]=="Azul": 
    vv5=input("Ingrese otro color diferente a azul:")
    lis5[-1]=vv5
    print(lis5)
else: print("La lista de colores cumple con la condición.")
print("-------------------------------------------------------")
print("Tuplas y Condicionales")
print("Ejercicio 16")
tup=(5, 8, 12, 20)
print(tup)
if tup[0]<tup[3]:
    print("Orden ascendente.")
else: print("Orden descendente.")
print("-------------------------------------------------------")
print("Ejercicio 17")
tup1= (25, 32, 28)
print(tup1)
if tup1[1]>tup[2]:
    print("Edad mayor a 30.")
else: print("Edad menor o igual a 30.")
print("-------------------------------------------------------")
print("Ejercicio 18")
tup2=(1, 2, 3)
print(tup2)
v13=list(tup2)
print(tup2)
if tup2[1]==2:
    v13[1]=10
    v14=tuple(v13)
    print(v14)
else: print("Cumple con la condición.")
print("---------------------------------------------------------")
print("Ejercicio 19")





























































































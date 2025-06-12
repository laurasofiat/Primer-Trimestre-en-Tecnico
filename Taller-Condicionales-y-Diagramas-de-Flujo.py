print("Ejercicios condicionales y Operaciones matemáticas.")
print("Ejercicio 1")
v1=float(input("Ingrese un número:"))
if v1==0:
    print("El número ingresado es cero.")
elif v1>=1:
    print("El número ingresado es positivo.")
else: print("El número ingresado es negativo.")
print("---------------------------------------------------")
print("Ejercicio 2")
v2=float(input("Ingrese un número:"))
v3=float(input("Ingrese un número:"))
if v2>v3:
    print("El número primer número ingresado es mayor al segundo número ingresado.")
else:print("El número segundo número ingresado es mayor al primer número ingresado.")
print("---------------------------------------------------")
print("Ejercicio 3")
v=float(input("ingrese un número:"))
if v %2==0:
    print("El número es par.")
else: print("El número es impar.")
print("---------------------------------------------------")
print("Ejercicio 4")
vn=int(input("Ingrese un número:"))
if vn>=10 and vn<=20: #and=y---Es una condición.
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
v7=float(input("Ingrese un número:"))
if v7>=100:
    rs=(10/v7)*100
    print("El 10 porciento de 100 es:",rs)
else: print("El número no cumple con los requisitos,no se calculará porcentaje.")
print("---------------------------------------------------")
print("Ejercicio 7")
v8=float(input("¿Cuántos años tienes?"))
if v8>=18:
    print("Puede votar.")
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
lis1=[float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:"))]
print(lis1)
vv=lis1[2]
print(vv)
if vv>10:
    print("El número",vv,"es mayor a 10.")
else: print("El número",vv,"no es mayor a 10.")
print("-----------------------------------------------------")
print("Ejercicio 12")
lis2=[float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:"))]
print(lis2)
vv1=lis2.index==7
if vv1=="true":
    print("El número 7 está en la lista.")
else: print("El número 7 no está en la lista.")
print("-----------------------------------------------------")
print("Ejercicico 13")
lis3=[float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:"))]
print(lis3)
vv2=lis3[0]+lis3[3]
print(vv2)
if vv2>=10:
    print("Suma alta.")
else: print("Suma baja.")
print("-----------------------------------------------------")
print("Ejercicio 14")
lis4= [input("Ingrese un nombre:"),input("Ingrese un nombre:"),input("Ingrese un nombre:"),input("Ingrese un nombre:")]
print(lis4)
vv3=lis4[3]
print(vv3)
if vv3=="Marta":
    print("Nombre correcto (Martha)")
else: print("Nombre diferente a Martha")
print("-----------------------------------------------------")
print("Ejercicico 15")
lis5=[input("Ingrese un color:"),input("Ingrese un color:"),input("Ingrese un color:")]
print(lis5)
if lis5[2]=="azul": 
    vv5=input("Ingrese otro color diferente a azul:")
    lis5[-1]=vv5
    print(lis5)
else: print("La lista de colores cumple con la condición.")
print("-------------------------------------------------------")
print("Tuplas y Condicionales")
print("Ejercicio 16")
lis6=[float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:"))]
tup=tuple(lis6)
print(tup)
if tup[0]<tup[3]:
    print("Orden ascendente.")
else: print("Orden descendente.")
print("-------------------------------------------------------")
print("Ejercicio 17")
lis7=[float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:"))]
tup1=tuple(lis7)
print(tup1)
if tup1[1]>30:
    print("Edad mayor a 30.")
else: print("Edad menor o igual a 30.")
print("-------------------------------------------------------")
print("Ejercicio 18")
lis8=[float(input("Ingrese un número:")),float(input("Ingrese un número:")),float(input("Ingrese un número:"))]
if lis8[1]==2:
    lis8[1]==10
    tup2=tuple(lis8)
    print(tup2)
else: tup2=tuple(lis8) 
print(tup2)
print("---------------------------------------------------------")
print("Ejercicio 19")
lis9=[float(input("Ingrese un número:")),float(input("Ingrese un número:"))]
tup3=tuple(lis9)
print(lis9)
if tup3[1]>5:
    print("Coordenada alta")
else: print("Coordenada baja")
print("---------------------------------------------------------")
print("Ejercicio 20")
lis10=[float(input("Ingrese un número:")),float(input("Ingrese un número:"))]
lis11=[float(input("Ingrese un número:")),float(input("Ingrese un número:"))]
tup4=tuple(lis10)
tup5=tuple(lis11)
print(tup4)
print(tup5)
if tup4==tup5:
    print("Tuplas iguales.")
else: print("Tuplas diferentes.")
print("---------------------------------------------------------")
print("Diccionarios y Condicionales")
print("Ejercicio 21")
v13=input("Ingrese nombre:")
v14=int(input("Ingrese edad:"))
dic={"Nombre":v13}
dic1={"Edad":v14}
print(dic,dic1)
if v14>=18:
    print("Adulto")
else: print("Menor de edad.")
print("---------------------------------------------------------")
print("Ejercicio 22")
v15=input("Ingrese nombre:")
v16=int(input("Ingrese edad:"))
dic2={"Nombre":v15}
dic3={"Edad":v16}
print(dic2,dic3)
if v16>18:
    dic3["Edad"]=21
    print(dic3)
else: print("El diccionario cumple con los requisitos.")
print("---------------------------------------------------------")
print("Ejercicio 23")
v17=input("Ingrese nombre:")
v18=input("¿Desea agregar ciudad?")
if v18=="no":
    v19="Bogotá"
    dic5={"Nombre":v17}
    dic6={"Ciudad":v19}
    print(dic5,dic6)
elif v18=="si":
     v19=input("Ingrese Ciudad:")
     dic5={"Nombre":v17}
     dic66={"Ciudad":v19}
     print(dic5,dic66)
else: print("Respuesta incorrecta.")
print("---------------------------------------------------------")
print("Ejercicio 24")
v20=input("Agrege producto:")
v21=input("¿Desea agregar precio?")
if v21=="no":
    print("No hay precio")
elif v21=="si":
    v22=float(input("Ingrese precio:"))
    d7={"Producto":v20}
    d8={"precio":v21}
    print(d7,d8)
else: print("Respuesta Incorrecta.")
print("---------------------------------------------------------")
print("Ejercicio 25")
v22=input("Ingrese producto de 2000:")
v23=input("¿Desea agregar precio de pan?")
if v23=="no":
    print("Producto no disponible")
    dic7={v22:"2000"}
    print(dic7)
elif v23=="si":
    v24=input("Ingrese precio:")
    dic9={v22:"2000"}
    dic10={"pan":v24}
    print(dic9,dic10)
else: print("Respuesta incorrecta.")





























































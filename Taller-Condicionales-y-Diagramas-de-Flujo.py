print("Ejercicios condicionales y Operaciones matemáticas.")
print("---------------------------------------------------")
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
print("Ejercicio 3")#Lo haré en la proxima clase profe, no entendí y preferí continuar :).
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
if v10=="VIP":
    rs1=(20/v9)*100
    print("El descuento se ha realizado,descuento de:",rs1,"%")
else: print("No cumple con los requisitos, no se hará descuento de 20%")
print("---------------------------------------------------")
























































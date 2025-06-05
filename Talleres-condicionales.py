print("Taller 1-Crédito Bancario")
nom_usuario=input("Ingrese nombre de ususario:")
x=input("¿Tu edad es mayor a 18?:")
if x=="si":
    print(nom_usuario,"Sí cumple con los requisitos.")
    print("Puede hacer procesos de crédito.")
else: print(nom_usuario,"No cumple con los requisitos.")
print("-----------------------------------------------------")
print("Taller 2-Empresa que calcula ingrese de clientes.")
edad=int(input("Ingrese su edad:"))
if edad>=1 and edad<=4:
    print("Entrada gratis.")
elif edad>=5 and edad<18:
    print("Debe pagar 5 euros.")
elif edad>=18:
    print("Debe pagar 18 euros.")
print("-----------------------------------------------------")
print("Taller 3-Simulador de una calculadora")
print("Ingrese operación deseada:"
"Suma=S--------------------Resta=R----------------"
"Multiplicación=M----------División=D")
v=(input("¿qué operación desea realizar?:")).upper
if v=="S":
    v1=float(input("Ingrese un número:"))
    v2=float(input("Ingrese un número:"))
    print("El resultado de la suma es:",v1+v2)
elif v=="R":
    v3=float(input("Ingrese un número:"))
    v4=float(input("Ingrese un número:"))
    print("El resultado de la resta es:",v3-v4)
elif v=="M":
    v5=float(input("Ingrese un número:"))
    v6=float(input("Ingrese un número:"))
    print("El resultado de la multiplicación es es:",v5*v6)
elif v=="D":
    v7=float(input("Ingrese un número:"))
    v8=float(input("Ingrese un número:"))
    print("El resultado de la división es:",v7/v8)
























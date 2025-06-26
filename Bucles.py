# print("Ejercicios con while,condicionales y estructuras")
# t=0 #Ejercicio 1
# v1=int(input("Ingrese un número entero:"))
# while v1!=0:
#     t+=v1
#     v1=int(input("Ingrese un número entero(0 para terminar):"))
#     print(t,"Programa finalizado")
# v2=input("Ingrese contraseña:") #Ejercicio 2
# con="python123"
# while v2!=con:
#     print("Contraseña incorrecta.")
#     v2=input("Ingrese contraseña correcta:")
# lis=[ ] #Ejercicio 3
# v3=input("Empieza a ingresar un producto(si deseas terminar la lista ingresa fin):")
# while v3!="fin":
#     v3=input("Ingresa un producto:")
#     lis+=[v3]
#     print(lis)
# v4=1 #Ejercicio 4
# while v4<=100000000000:
#     v4=int(input("Ingrese 10 números par, y cierre el programa:"))
#     if v4%2==1:
#          print("Número impar")
#     else: print("Número par")
lis1=[ ] #Ejercicio 5
v5=float(input("Ingresa una nota:"))    
v6=input("¿Deseas dejar de agregar notas?. Agrega salir para confirmar:")
while v6!="salir":
    v5=float(input("Ingresa una nota:"))
    lis1+=[v5]
    print(v5)
    if v6=="salir":
        v7=lis1/v5
        print("Promedio:",v7)

    











































































# print("Ejercicios con while,condicionales y estructuras")
#print("-------------------------------------------------------------------------------")
# t=0 #Ejercicio 1
# v1=int(input("Ingrese un número entero:"))
# while v1!=0:
#     t+=v1
#     v1=int(input("Ingrese un número entero(0 para terminar):"))
#     print(t,"Programa finalizado")
#print("--------------------------------------------------------------------------------")
# v2=input("Ingrese contraseña:") #Ejercicio 2
# con="python123"
# while v2!=con:
#     print("Contraseña incorrecta.")
#     v2=input("Ingrese contraseña correcta:")
#print("--------------------------------------------------------------------------------")
# lis=[ ] #Ejercicio 3
# v3=input("Empieza a ingresar un producto(si deseas terminar la lista ingresa fin):")
# while v3!="fin":
#     v3=input("Ingresa un producto:")
#     lis+=[v3]
#     print(lis)
#print("--------------------------------------------------------------------------------")
# v4=1 #Ejercicio 4
# while v4<=100000000000:
#     v4=int(input("Ingrese 10 números par, y cierre el programa:"))
#     if v4%2==1:
#          print("Número impar")
    # else: print("Número par")
# print("--------------------------------------------------------------------------------")
# lis1=[ ] #Ejercicio 5
# tt=0
# v5=float(input("Ingresa una nota:"))    
# lis1+=[v5]
# tt+=v5
# v6=input("¿Deseas dejar de agregar notas?. Agrega salir para confirmar,si no, agrega NO:").lower
# while v6!="salir" or v6!="SALIR":
#     v5=float(input("Ingresa una nota:"))
#     tt+=v5
#     lis1+=[v5]
#     print(lis1)
#     v6=input("¿Deseas dejar de agregar notas?. Agrega salir para confirmar,si no, agrega NO:")
#     if v6=="salir" or v6=="SALIR":
#         print("total de suma:",tt)
#         v7=int(input("¿Cuántos números agrego a la lista?"))
#         v8=tt/v7
#         print("Promedio de las notas:",v8)
#         break
# print("--------------------------------------------------------------------------------")
# v9=float(input("Ingrese un número para ver su tabla de multiplicar:"))
# tb=1
# while tb<=10:
#     print(f"{v9}x{tb}={v9*tb}")
#     tb+=1
# print("--------------------------------------------------------------------------------")
# v10=13 #Ejercicio 7
# print("Hola usuario,tienes que adivinar el número secreto.Te diré si es mayor o menor en el proceso.")
# v11=float(input("Ingresa el número:"))
# while True:
#     if v11>v10:
#         print("Mayor")
#         v11=float(input("Intentalo nuevamente:"))
#     if v11<v10:
#         print("Menor")
#         v11=float(input("Intentalo nuevamente:"))
#     if v11==v10:
#         print("El número ingresado es correcto.")
#         print("¡Felicidades!")
#         break
# print("--------------------------------------------------------------------------------")
# tup=("mamoncillo","guayaba manzana","kiwi") #Ejercicio 8
# v12=input("Hola usuario.Ingresa una fruta, hasta que adivines una de la lista secreta. ")
# while  v12!=tup[0] or v12!=tup[1] or v12!=tup[2]:
#         v12=input("Intenta de nuevo:")
#         if v12==tup[0] or v12==tup[1] or v12==tup[2] or v12==tup[3]:
#              print("¡Felicidades,has adivinado una fruta de la lista!")
#              print(tup)
#              break
# print("-------------------------------------------------------------------------------")
# dicc={"gato":"cat","perro":"dog","cielo":"darling","azul":"cielo"} #Ejercicio 9
# print(dicc)
# while True:
#     v13=input("Ingresa una palabra para traducirla al español(o ingresa salir):")
#     if v13=="salir" or v13=="SALIR":
#         break
#     if v13 in dicc:
#         print("Traducción",dicc[v13])
#     else: print("La palabra que ingreso no se encuentra en el diccionario.")
# print("-------------------------------------------------------------------------------")
# while True:  #Ejercicio 10
#     v14=input("Ingresa en nombre la operación que deseas realizar:resta,suma,multiplicación o división" \
#     "    O si deseas retirarte(salir):")
#     if v14=="suma":
#         v15=float(input("ingrese primer número:"))
#         v16=float(input("Ingrese segundo número:"))
#         v17=v15+v16
#         print(v17)
#     elif v14=="resta":
#         v15=float(input("ingrese primer número:"))
#         v16=float(input("Ingrese segundo número:"))
#         v17=v15-v16
#         print(v17)
#     elif v14=="multiplicación":
#         v15=float(input("ingrese primer número:"))
#         v16=float(input("Ingrese segundo número:"))
#         v17=v15*v16
#         print(v17)    
#     elif v14=="división":
#         v15=float(input("ingrese primer número:"))
#         v16=float(input("Ingrese segundo número:"))
#         v17=v15/v16
#         print(v17)
#     elif v14=="salir":
#         break
#     else: print("Operación erronea.")
dicc1={ } #Ejercicio 11
while True:
    v18=int(input("Ingresa tu edad:"))
    v19=input("ingresa un nombre:")
    m1=("Nombre",v19)
    m2=("Edad",v18)
    dicc1+=[m1]
    dicc1+=[m2]
    v20=input("¿Deseas salir(SI O NO?")
    if v20=="SI" or v20=="salir":
        print(dicc1)
        break




































































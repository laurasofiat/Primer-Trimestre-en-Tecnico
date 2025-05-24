print("Ejercicio 1")
#Crea una lista vacía llamada productos.Pide al usuario 3 nombres y guárdalos con .append .Imprime lista completa.
productos=[]
productos.append(input("Ingresar el nombre de un producto: "))
productos.append(input("Ingresar el nombre de un producto: "))
productos.append(input("Ingrese el nombre de un producto: "))
print(productos)
print("Ejercicio 2")
# Pide al usuario que ingrese el precio de tres artículos diferentes (usar float()),guárdalos en una lista llamada precios y luego imprime su suma total.
precios=[]
precios.append(float(input("Ingrese el primer precio: ")))
precios.append(float(input("Ingrese el segundo precio: ")))
precios.append(float(input("Ingrese el tercer precio: ")))
pp=precios[0]+precios[1]+precios[2]
print("La suma total de los precios es: ",pp)
print("Ejercicio 3")
#Pide al usuario que insegrese 4 números uno por uno,guárdalos  con .append en una lista llamada números y luego imprime cuál fue el mayor y el menor(usando max y min).
números=[]
números.append(int(input("Ingrese un número entero: ")))
números.append(int(input("Ingrese número entero: ")))
números.append(int(input("Ingrese número entero: ")))
print("El número mayor es:",{max(números)},"y el número nmenor es: ",{min(números)})
print("Ejercicio 4")
list=["Mariana","Julia","Abigail","Salomé","Carol","Sara","Luisa"]
print(list)
list.insert(7,"JULIANA") #holllll
print(list)
ll=len(list)
print(ll,"Nombres")
ord=min(list)
ord1=max(list)
print("El mayor nombre alfabéticamente es",ord,"El menor alfabéticamente es",ord1)
mmm=len(list)//2
mm=list[mmm]
print("El nombre que esta en la mitad alfabéticamente  es: ",mm)
list.remove("Carol")
print(list)
print(list.index("JULIANA"))
print("Lista resultante: ",list)
print("productos y cálculos")
print("----------------------------------------------------------------")
inn=input("Ingrese el nombre del producto:")
in1=float(input("Ingrese precio unitario:"))
in2=int(input("Ingrese cantidad comprada:"))
print("----------------------------------------------------------------")
t=(inn,in1)
print(t)
ll=[t,in2]
print(ll)
print("----------------------------------------------------------------")
dicc={
    "producción":ll
}
print(dicc)
print("----------------------------------------------------------------")
op=in1*in2
print("El costo total es:",op)
print("----------------------------------------------------------------")


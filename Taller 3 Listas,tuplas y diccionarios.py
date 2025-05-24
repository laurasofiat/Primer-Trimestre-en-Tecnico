print("Registro de notas")
print("------------------------------------------------")
n=input("Ingrese nombre del estudiante:")
n1=input("Ingrese primer asignatura:")
n2=float(input("Ingrese nota #1:"))
n3=float(input("Ingrese nota #2:"))
n4=input("Ingrese segunda asignatura:")
n5=float(input("Ingrese nota #1:"))
n6=float(input("Ingrse nota #2:"))
n7=input("Ingrse tercer materia:")
n8=float(input("Ingrse nota #1:"))
n9=float(input("Ingrese nota #2:"))
print("------------------------------------------------")
lm=n2+n3
m1=lm/2
t=(n1,m1)
print(t)
lm1=n5+n6
m2=lm1/2
t1=(n4,m2)
print(t1)
lm2=n8+n9
m3=lm2/2
t2=(n7,m3)
print(t2)
print("------------------------------------------------")
lis=[t,n2,n3]
print(lis)
lis1=[t1,n5,n6]
print(lis1)
lis2=[t2,n8,n9]
print(lis2)
print("------------------------------------------------")#holaaaaaaaaa
l3=[n1,n4,n7]
dicc={"Nombre":n}
dicc1={"Materias":l3}
print(dicc,dicc1)
ff=m1+m2+m3
fp=ff/3
print("El promedio de las tres asignaturas es:",fp)
print("------------------------------------------------")
print("Boletín de calificaciones,aprueba año lectivo si la nota final es mayoy a 3.0")
print(n1,"-Susi promedio es:",m1," ",n4,"-Su promedio es:",m2," ",n7,"-Su promedio es:",m3," ","El promedio final de las tres asignaturas es:",fp)
g=fp<=3.0
print("¿",n,"Ganó el año lectivo?",g)
print("------------------------------------------------")




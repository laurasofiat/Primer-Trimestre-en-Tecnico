print("Ejercicico en clase")
print("----------------------------------------------------------------")
print("Resultado finales de materias.Este sistema te va a dar los resultados finales de las 5 materias, promediando las tres notas  de cada materia.La nota mínima es de 3.2")
print("---------------------------------------------------------------")
nom=input("Ingrese el nombre del usuario: ")
m=input("Ingrese el nombre de la materia 1: ")
n=float(input("Ingrese primer nota: "))
n1=float(input("Ingrese segunda nota: "))
n2=float(input("Ingrese tercer nota: "))
op=n+n1+n2
rs=op//op
print("El resultado final de",m,"es:",rs)
nm=rs>=3.2
print("¿",nom,"Paso la materia de",m,"?",nm)
print("-----------------------------------------------------------------")
m1=input("Ingrese el nombre de la materia 2: ")
n3=float(input("Ingrese primer nota: "))
n4=float(input("Ingrese segunda nota: "))
n5=float(input("Ingrese tercer nota: "))
op1=n3+n4+n5
rs1=op1//3
print("El resultado final de",m1,"es:",rs1)
mn1=rs1>=3.2
print("¿",nom,"paso la materia de",m1,"?",mn1)
print("--------------------------------------------------------------")
m2=input("Ingrese nombre de la materia 3: ")
n6=float(input("Ingrese primer nota: "))
n7=float(input("Ingrese segunda nota: "))
n8=float(input("Ingrese tercer nota: "))
op2=n6+n7+n8
rs2=op2//3
print("El resultado final de",m2,"es:",rs2)
nm2=rs2>=3.2
print("¿",nom,"paos la materia de",m2,"?",nm2)
print("----------------------------------------------------------------")
m3=input("Ingrese el nombre de la materia 4: ")
n9=float(input("Ingrese primer nota: "))
n10=float(input("Ingrse segunda nota: "))
n11=float(input("Ingrese tercer nota: "))
op3=n9+n10+n11
rs3=op3//3
print("El resultado final de",m3,"es:",rs3)
nm3=rs3>=3.2
print("¿",nom,"paso la materia de",m3,"?",nm3)
print("----------------------------------------------------------------")
m4=input("Ingrese nombre de la materia 5: ")
n12=float(input("Ingrese primer nota: "))
n13=float(input("Ingrese segunda nota: "))
n14=float(input("Ingrese tercer nota: "))
op4=n12+n13+n14
rs4=op4//3
print("El resultado final de",m4,"es:",rs4)
nm4=rs4>=3.2
print("¿",nom,"paso la materia de",m4,"?",nm4)
print("----------------------------------------------------------------")
print("Resultado final de año lectivo. Aprovado sobre o mayor a 3.8")
ops=rs+rs1+rs2+rs3+rs4
rsf=ops//5
ope=rsf>=3.8
print("¿",nom,"Aprobo el año lectivo?:",ope)
print("----------------------------------------------------------------")
print("Gracias",nom,"por usar este programa.")
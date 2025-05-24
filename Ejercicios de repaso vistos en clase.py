print("Clase 1,slución de ejercicios") 
print("----------------------------------------")
a=5
b=5
n=2
m=5
pas=a+n
pase=m**pas
result=pase
print(f"El resultado de la opración es:",result)
print("----------------------------------------")
a2=8
n2=5
m1=2
pas2=n2-m1
result2=a2**pas2
print(f"El resultado de la operación es:",result2)
print("------------------------------------------")
a3=3
b2=4
n3=1
pas3=b2**n3
result3=a2*pas3
print(f"El resultado de la operación es:",result3)
print("------------------------------------------")
nombre=input("Ingrese su nombre:")
print(f"Su nombre ingresado es:",nombre)
apellido=input("Ingrese su apellido:")
print(f"Su apellido ingresado es:",apellido)
ciudad=input("Ingrese su ciudad:")
print(f"Su ciudad ingresada es:",ciudad)
print("--------------------------------------------")
print("Clase 2,Ejercicios en clase")
num1=int(input("Ingrese una base numérica:"))
num2=int(input("Ingrese una base numérica:"))
num3=int(input("Ingrese un exponente:"))
res=num1**num3
resu=res*num2
print(f"El resultado de la potenciación es igual a:",resu)
print("--------------------------------------------")
num4=int(input("Ingrese una base numérica:"))
num5=int(input("Ingrse una base numérica:"))
num6=int(input("Ingrse un exponente:"))
res1=num4/num5
resu1=res1**num6
print(f"El resultado de la potenciación es:",res1)
print("--------------------------------------------")
print(f"Clase 3,Ejercicios para recordar")
x,y,z=2,4,6
print(x)
print(y)
print(z)
a,b,c="Tú","Yo","Ella"
print(a)
print(b)
print(c)
var1=var2="Hola bebe"
print(var1)
print(var2)
n=10
n+=5
print(n)
n*=2
print(n)
s="Estoy tomando "
s+="clases para tener "
s+="un técnico en programación de Software."
print(s)
s*=2
print(s)
tex1="Hola"
tex2="Programador"
resultado=tex1+" "+tex2
print(resultado)
mensaje="La búsqueda trata sobre el número del punto de inicio de una cadena de string."
buscar=mensaje.find("trata")
print(buscar)
extraer=mensaje[0:78]
print(extraer)
var=5
var1=55
print(var1==var)
print("----------------------------------------------------")
print("Ejercicio 1")
tex3="El conocimiento es poder"
buscar1=tex3.find("conocimiento")
buscar2=tex3.find("poder")
print(buscar1)
print(buscar2)
print("----------------------------------------------------")
print("Ejercicio 2")
tex4="La práctica hace al maestro"
print(tex4)
print(tex4.find("práctica"))
print(tex4.find("maestro"))
print("----------------------------------------------------")
print("Ejercicio 3")
pre=input("Ingrese una frace:")
pre1=input("¿Qué palabra quieres buscar en la frace? ")
print(pre.find(pre1))
parr="Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"
print(parr)
print(parr.find("Sabia"))
print(parr.find("Caminaba"))
print(parr.find("falanges"))
extraer1=parr[459:655]
print(extraer1)
print("----------------------------------------------------")
print("Ejemplo")
parr1="Siglo XVIII Agosto de l788 SOCIEDAD ESTAMENTAL --CONVOCATORIA DEL REY A LOS ESTADOS GENERALES--Julio de 1789 CONCENTRACION DE REGIMIENTOS EXTRANJEROS EN PARIS Y VERSALLES-12 de julio de l789 14 de julio de 1789 5 de octubre de 1789 COMIENZO DE LA INSURRECCION DEL PUEBLO --TOMA DE LA BASTILLA --LAS MUJERES HACIA VERSALLES.Fines de 1792 21 de enero de 1793 Enero y febrero de 1793 --CONVENCION CONTRA LUIS XVI-LA EJECUCION DEL REY-INDIGNACION EN INGLATERRA-Febrero de 1793 DECLARACION DE LA GUERRA POR PARTE DE FRANCIA."
print(parr1)
print(parr1.find("1789"))
print(parr1.find("12 de julio"))
print(parr1.find("PUEBLO"))
extraer2=parr1[171:270]
print(extraer2)
print("----------------------------------------------------")
print("Primer programa creado")
p=int(input("Ingrese la primer nota:"))
p1=int(input("Ingrese la segunda nota:"))
p2=int(input("Ingrese la tecer nota:"))
nom=input("Ingrese un nombre y apellido:")
por=p*0.2
por1=p1*0.3
por2=p2*0.5
resus=(por+por1+por2)//3
print("El resultado final del estudiante",nom," es igual a:",resus)
print("Factura de productos")
print("----------------------------------------------------------------")
in3="pan" 
in4=600
in5=12
in6="Mermelada"
in7=7000
in8=2
in9="Aceite"
in10=3500
in11=7
tople=(in3,in4)
print(tople)
tople1=(in6,in7)
print(tople1)
tople2=(in9,in10)
print(tople2)
print("----------------------------------------------------------------")
tc=[tople,in5]
print(tc)
tc1=[tople1,in8]
print(tc1)
tc2=[tople2,in11]
print(tc)
print("----------------------------------------------------------------")
dicc={"producto 1":"Pan"}
dicc1={"producto 2":"Mermelada"}
dicc2={"producto 3":"Aceite"}
print(dicc,dicc1,dicc2)
print("----------------------------------------------------------------")
t1=in4*in5
print("Total de producto:",t1)
t2=in7*in8
print("Total de producto:",t2)
t3=in10*in11
print("Total de producto:",t3)
ttf=t1+t2+t3
print("Cantidad total de productos",ttf)
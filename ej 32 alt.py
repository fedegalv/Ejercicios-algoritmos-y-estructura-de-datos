
listaF=[]
numero=int(input("Ingrese el numero de posicion: "))
cont=0
while cont < numero:
 	if cont==0:
 		listaF.insert(cont,1)

 	elif cont==1:
 		listaF.insert(cont,1)
 	else:
 		listaF.insert(cont,listaF[cont-2]+listaF[cont-1])
 	cont= cont+1
print("El numero dentro de la posicion ",numero," en la sucesion de Fibonacci es: ",listaF[numero-1])
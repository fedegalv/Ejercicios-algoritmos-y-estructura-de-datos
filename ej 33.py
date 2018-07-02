def hallar_fibonacci(numero):
	listaF=[]
	cont=0
	while cont < numero:
		if cont==0:
			listaF.insert(cont,1)
		elif cont==1:
			listaF.insert(cont,1)
		else:
			listaF.insert(cont,listaF[cont-2]+listaF[cont-1])
		cont= cont+1
	return listaF

contador=0
numero=int(input("Ingrese el numero de posicion n: "))
lista=hallar_fibonacci(numero)

print("Primeros n terminos de la serie numerica de Fibonacci")
while contador < numero:
	print(lista[contador])

	contador+=1







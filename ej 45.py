def pow(x,y):
	aux=cont=0
	while cont < y:
		if cont == 1:
			aux= x * x
		else:
			aux=aux * x
			

		cont+= 1

	return aux

x= int(input("Ingrese el numero base: "))
y= int(input("Ingrese el exponente: "))
resultado= pow(x,y)

print("El resultado es: ",resultado)



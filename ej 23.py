null= False
maxnegativo=0
minpositivo=0
prom=0
cont=1
while null == False:
	numero=int(input("Ingrese un valor numerico, se cancelara el ingreso con (null): "))
	null= isinstance(numero, int)


	if cont == 0:
		if numero < 0:
				maxnegativo=numero

		elif numero>0:
			minpositivo=numero
		
		prom=numero


	elif cont > 0:
		if numero < 0:
			if numero < maxnegativo:
				maxnegativo=numero

		elif numero>0:
			if numero< minpositivo:
				minpositivo=numero

		prom=prom+numero

	cont+=1


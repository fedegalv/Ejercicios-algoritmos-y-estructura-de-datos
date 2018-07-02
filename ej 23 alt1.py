null= False
maxnegativo=0
minpositivo=0
prom=0
cont=1
while null == False:
	while True:
		try:
			numero=int(input("Ingrese un valor numerico, se cancelara el ingreso con (null): "))
		except ValueError:
			null=True
			continue


	if cont == 0:
		"""if numero < 0:
				maxnegativo=numero

		elif numero>0:
			minpositivo=numero
		"""
		maxnegativo=numero
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

print(maxnegativo)
print(minpositivo)
print(prom)


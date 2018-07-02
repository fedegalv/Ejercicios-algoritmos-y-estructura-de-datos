## FALTA TERMINAR
maxnegativo=0
minpositivo=None
minrango=None
prom=0
cont=1
while True:
	try:
		numero=int(input("Ingrese un valor numerico, se cancelara el ingreso con (null): "))
	except ValueError:
		null=True
		break


	if cont == 1:
		"""if numero < 0:
				maxnegativo=numero

		elif numero>0:
			minpositivo=numero
		"""
		if numero> 0:
			minpositivo=numero
		prom=numero


	elif cont > 1:
		if numero < 0:
			if numero < maxnegativo:
				maxnegativo=numero

		elif numero>0:
			if numero< minpositivo:
				minpositivo=numero
		elif numero < 26 and numero > -17:
			if cont==1:
				minrango=numero
			elif cont >1:
				if numero < minrango:
					minrango=numero

		prom=prom+numero

	cont+=1
promfinal= prom/(cont-1)

print("El valor maximo negativo es: ",maxnegativo)
print("El valor minimo positivo es: ",minpositivo)
print("El valor minimo dentro del rango es: ", minrango)
print("El promedio es: ", promfinal)


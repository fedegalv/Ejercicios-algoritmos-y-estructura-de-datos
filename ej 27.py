trigger=True
gravedadL=0
gravedadM=0
gravedadG=0
menorInfracc=None
motivoMenorInfracc=None
clausurarFabrica=False
cont=0
total=0
contInfracc=0

print("SISTEMA DE INFRACCIONES")
print("FABRICA DE PINTURAS\n")


while trigger:
	tInfr=int(input("Ingrese el tipo de infraccion (1,2,3 o 4): "))
	if tInfr == 0:
		trigger=False
		break

	motivo=input("Ingrese motivo de la infraccion: ")
	valor=int(input("Ingrese valor de la multa: "))
	gravedad=input("Ingrese gravedad de la infraccion (L) Liviana, (M) Mediana, (G) Grave: ")
	gravedad.upper()

	total=total+valor

	if gravedad == "L":
		gravedadL= gravedadL + valor
	elif gravedad == "M":
		gravedadM= gravedadM + valor
	elif gravedad == "G":
		gravedadG= gravedadG+ valor


	if tInfr == 3 and gravedad == "G":
		contInfracc+=1
		

	elif tInfr == 4 and gravedad == "G":
		contInfracc+=1

	if contInfracc >= 3:
		clausurarFabrica=True

	if cont ==0: ### CALCULAMOS EL VALOR DE LA INFRACCIN MENOR
		menorInfracc=valor
		motivoMenorInfracc=motivo

	else:
		if valor < menorInfracc:
			menorInfracc=valor
			menorInfracc=valor

	cont+=1

print("Total de multas a pagar: ",total)
print("Motivo de la infraccion de menor valor: ",motivoMenorInfracc)
if clausurarFabrica== True:
	print("Clausurar fabrica")
else:
	print("Por ahora no sera clausurada")












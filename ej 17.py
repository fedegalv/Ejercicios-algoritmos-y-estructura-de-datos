codEq={}
#Resultados=[]
ganados=0
perdidos=0
empates=0
cont=0
cont2=0
valido1=False
k=int(input("Ingrese el numero de equipos: "))
while cont2 < (k):## PREGUNTA SI EL CONTADOR@ ES MENOR QUE EL NUMERO DE EQUIPOS
	equipo=input("Ingrese el codigo del equipo numero %d: "%(cont2+1))
	## LOOP QUE PREGUNTA EL RESULTADO DEL EQUIPO ACTUAL
	while cont < (k-1):
		res=input("Ingrese el codigo del resultado del partido numero %d : "%(cont+1))
		if cont == 0: ## ESTE IF SIRVE, SI ES QUE ES LA PRIMERA VEZ QUE SE ENTRA ESTE LOOP, PARA SETEAR EL VALOR A 0 DE CADA EQUIPO(DEFAULT) Y SI GANAN SE SETEA EN 3, SI EMPATAN A 2
			codEq[equipo]=0
			if res == "G":
				codEq[equipo]=3
				ganados+=1  ## ACUMULA PARTIDOS GANADOS
			elif res == "E":
				codEq[equipo]=1
				empates+=1 ## ACUMULA EMPATES
			else:
				perdidos+=1
		else: ### CUANDO YA NO ES LA PRIMERA VUELTA DEL LOOP, LOS VALORES YA FUERON SETEADOS(0,3 o 1)
			if res == "G":
				codEq[equipo]=codEq[equipo]+3 ## PARA SUMAR LOS PUNTOS Y ACUMULAR LOS PUNTOS, SI EN LA PRIMERA VUELTA PERDIO ES 0+3, SI GANO 3+3, SI EMPATO 1+3, EN LA PROXIMA VUELTA SE LE SUMA A LO ACUMULADO +3
				ganados+=1
			elif res == "E":
				codEq[equipo]=codEq[equipo]+1 ## MISMO QUE ARRIBA PERO EMPATES, A LO ACUMULADO SE LE SUMA +1
				empates+=1
			else:
				perdidos+=1

		cont+=1
	cont=0	
	cont2+=1

#print(codEq)
print("Partidos perdidos: ",perdidos)
print("Partidos ganados:", ganados)
print("Partidos empatados:",empates)
if perdidos == ganados:
	valido1=True

print("Fue un partido valido: ", valido1)
pesototal=0
mayorPesoId=None
mayorPeso=0
puerto1=0
puerto2=0
puerto3=0
cont=0

while cont<5:
	idCont=input("Ingrese la identificacion del contenedor: ")

	peso=int(input("Ingrese el peso del contenedor: "))

	idPuerto= int(input("Ingrese la id del puerto: "))

	pesototal=pesototal+peso

	if peso > mayorPeso:
		mayorPeso=peso
		mayorPesoId=idCont


	if idPuerto== 1:
		puerto1= puerto1+1
	elif idPuerto==2:
		puerto2=puerto2+1
	elif idPuerto==3:
		puerto3=puerto3+1

	cont+=1

print("EL peso total que el buque debe transladar es: ", pesototal)

print("El contenedor de mayor peso es : ",mayorPesoId)

print("Contenedores transladados:")
print("Puerto 1:", puerto1)
print("Puerto 2:", puerto2)
print("Puerto 3:", puerto3)





fechahoy=[29,3,1994]
print(fechahoy[:])

primerfecha=[]
print("Ingrese una primera fecha:")
primerfecha.append(int(input("Ingrese primer dia: ")))
primerfecha.append(int(input("Ingrese mes: ")))
primerfecha.append(int(input("Ingrese anio: ")))
print(primerfecha)

segundafecha=[]
print("Ingrese segundo dia: ")
segundafecha.append(int(input("Ingrese primer dia: ")))
segundafecha.append(int(input("Ingrese segundo dia: ")))
segundafecha.append(int(input("Ingrese tercer dia: ")))


if fechahoy[2]>primerfecha[2]:
	difFecha1=fechahoy[2]-primerfecha[2]
else:
	difFecha1=primerfecha[2]-fechahoy[2]

#print(difFecha1)
if fechahoy[2]>segundafecha[2]:
	difFecha2=fechahoy[2]-segundafecha[2]
else:
	difFecha2=segundafecha[2]-fechahoy[2]
#print(difFecha2)

if difFecha1<difFecha2:
	print("La fecha mas cercana es ",(primerfecha))
else:
	print("La fecha mas cercana es ",(segundafecha))




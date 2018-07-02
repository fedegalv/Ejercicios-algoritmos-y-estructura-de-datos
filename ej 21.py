listanum=[]
nromayor=0
corte=False
cont=0
while corte == False:
	nro=(int(input("Ingrese un numero a la lista, para detener el ingreso use un 0: ")))
	if nro == 0:
		corte=True
	else:
		listanum.append(nro)
	cont=+1



for i in listanum:
	if i > nromayor:
		nromayor=i
		posnromayor= listanum.index(i)



minimo=listanum[0]
for a in listanum:
	if a < minimo:
		minimo = a
		posnromenos= listanum.index(a)

print("El numero mayor de la lista es: %d, posicion en la lista %d" %(nromayor,posnromayor+1))
print("El numero menos de la lista es: %d, posicion en la lista %d" %(minimo, posnromenos+1))

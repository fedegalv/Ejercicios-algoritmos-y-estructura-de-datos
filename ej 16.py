listanros=[]
suma=0
cont=0
i=0
aux=0
menoresadiez=0
while i < 5:
	listanros.append(int(input("Ingrese un numero: ")))
	i+=1

for b in listanros:
	if b > 100:
		suma=suma+b
		cont+=1
	if b < -10:
		menoresadiez=menoresadiez+b

prom=suma/cont

print("promedio: ", prom)
print("suma de los menos que son menores a -10: ",menoresadiez)

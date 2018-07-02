trigger = False
oracion= []
cont= 0
palabra_mas_larga = None
mas_larga= 0
contA=0
contE=0
contI=0
contO=0
contU=0
largo= 0

while trigger == False:
	palabra= input("Ingrese una palabra, para terminar el ingreso use un punto (.): ")
	oracion.append(palabra)
	aux1= len(palabra)
	if cont == 0:
		mas_larga= aux1
		palabra_mas_larga = palabra

	else:
		if aux1 > mas_larga:
			mas_larga= aux1
			palabra_mas_larga= palabra

	for i in palabra:
		if i == "a":
			contA+=1

		elif i == "e":
			contE+=1

		elif i == "i":
			contI+=1
		elif i == "o":
			contO+=1

		elif i == "u":
			contU+=1






	cont+=1
	if palabra == ".":
		trigger= True


largo=len(oracion)-1

print(oracion)
print("La palabra mas larga es: ",palabra_mas_larga)
print("La palabra A se repitio: ",contA,"veces")
print("La palabra E se repitio: ",contE,"veces")
print("La palabra I se repitio: ",contI,"veces")
print("La palabra O se repitio: ",contO,"veces")
print("La palabra U se repitio: ",contU,"veces")
print("La oracion contiene ",largo," palabras")
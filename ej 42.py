from ej_38 import factorial
from ej_41 import esMultiplo
cont=contador_de357=contador_de35= 0

control= int(input("Ingrese cuantos numeros naturales ingresara: "))
while cont < control:

	print("FACTORIAL:")
	n= int(input("Ingrese un numero: "))
	factorial(n)
	if n == 1 or n == 0:
		print("El factorial es: 1")
	else:
		fact= factorial(n)
		print("El factorial es : ", fact)

	de3= esMultiplo(n,3)
	de5= esMultiplo(n,5)
	de7= esMultiplo(n,7)

	if de3 == True and de5 == True and de7 == True:
		contador_de357+= 1
	if de3 == True and de5 == True:
		contador_de35+= 1

	cont+= 1

print("La cantidad de numeros multiplos de 3, 5 y 7 es: ", contador_de357)
print("La cantidad de numeros multiplos de 3 y 5 es: ", contador_de35)


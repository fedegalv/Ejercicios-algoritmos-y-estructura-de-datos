edad=int(input("Ingrese la edad del socio: "))

if edad <= 12:
	print("El socio es menor")
elif edad >=13 and edad<= 18:
	print("El socio es CADETE")
elif edad >18 and edad <=26:
	print("El socio es JUVENIL")
else:
	print("El socio es MAYOR")
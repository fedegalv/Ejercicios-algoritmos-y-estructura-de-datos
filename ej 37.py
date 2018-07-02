def mcd(a,b):
	maximocd= 0
	

	r= a%b
	if r == 0:
		maximocd=b
	else:
		a= b
		b= r
		r= a%b
		if r == 0:
			maximocd=b

	return maximocd


a= int(input("Ingrese un numero entero (a): "))
b= int(input("Ingrese un numero entero (b): "))

maximocd= mcd(a,b)

print("El maximo comun divisor es: ", maximocd)



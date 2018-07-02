
var1=int(input("Ingrese primer numero: "))
var2=int(input("Ingrese segundo numero: "))

if var1> var2:
	print("El numero %d es mayor"%(var1))
	print("El numero %d es menor"%(var2))
	print
elif var2>var1:
	print("El numero %d es mayor"%(var2))
	print("El numero %d es menor"%(var1))
elif var1 == var2:
	print("Ambos numeros son iguales")
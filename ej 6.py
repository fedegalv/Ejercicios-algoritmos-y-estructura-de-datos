var1=int(input("Ingrese primer numero: "))
var2=int(input("Ingrese segundo numero: "))
var3=int(input("Ingrese tercer numero: "))

if var1>var2 and var1>var3:
	if var2 > var3:
		print("El numero %d es mayor, el %d esta en el medio y %d es menor"% (var1,var2,var3))
	else:
		print("El numero %d es mayor, el %d esta en el medio y %d es menor"% (var1,var3,var2))

if var2>var1 and var2>var3:
	if var1>var3:
		print("El numero %d es mayor, el %d esta en el medio y %d es menor"% (var2,var1,var3))
	else:
		print("El numero %d es mayor, el %d esta en el medio y %d es menor"% (var2,var3,var1))

if var3>var1 and var3>var2:
	if var1>var2:
		print("El numero %d es mayor, el %d esta en el medio y %d es menor"% (var3,var1,var2))
	else:
		print("El numero %d es mayor, el %d esta en el medio y %d es menor"% (var3,var2,var1))
if var1 == var2 and var1 == var3:
	print("Los numeros son iguales")

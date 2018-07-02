def porcentajeDiferencia(a,b):
	porcentaje= (b-a)* 100 / (a+b)
	return porcentaje

a= int(input("Ingrese un numero (a): "))
b= int(input("Ingrese un numero (b): "))
porcentaje=porcentajeDiferencia(a,b)
print("El porcentaje de diferencia es: %",porcentaje)

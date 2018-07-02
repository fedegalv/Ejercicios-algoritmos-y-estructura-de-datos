def esMultiplo(a, b):
	multiplo=False

	if (a%b) == 0:
		multiplo= True
		#print("%d es multiplo de %d"%(a,b))

	return multiplo


a= int(input("Ingrese un numero (a): "))
b= int(input("Ingrese un numero (b): "))
multiplo= esMultiplo(a, b)

if multiplo == True:
	print("%d es multiplo de %d" %(a,b))
elif multiplo == False:
	print("No es multiplo")


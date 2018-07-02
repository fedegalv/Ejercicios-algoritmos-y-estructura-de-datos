menos2k=0
menos3k=0
menos5k=0
mas5k=0
mayorcero=True
while mayorcero == True:
	salario=int(input("Ingrese salario: "))
	if salario == 0:
		mayorcero= False
	elif salario > 0 and salario < 2000:
		menos2k+=1
	elif salario >= 2000 and salario < 3000:
		menos3k+=1
	elif salario >= 3000 and salario < 5000:
		menos5k+=1
	elif salario >= 5000:
		mas5k+=1

print("Los empleados que ganan menos de $2000 son: ",menos2k)
print("Los empleados que ganan mas de $2000 pero menos de $3000 son: ",menos3k)
print("Los empleados que ganan mas de $3000 pero menos de $5000 son: ", menos5k)
print("Los empleados que ganan mas de $5000 son: ",mas5k)

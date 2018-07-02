listanum=[]
nromayor=0
cont=0
while cont < 10:
	listanum.append(int(input("Ingrese un numero a la lista: ")))
	cont+=1



for i in listanum:
        if i > nromayor:
            nromayor=i

print(nromayor)
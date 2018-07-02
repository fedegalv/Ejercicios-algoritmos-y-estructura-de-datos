nro1= int(input("Ingrese primer numero(a multiplicar): "))
nro2= int(input("Ingrese segundo numero(multiplicador): "))
contador= 0
resultado=0
while contador <= (nro2-1):
	resultado= resultado+nro1
	contador+=1

print("resultado: ",resultado)
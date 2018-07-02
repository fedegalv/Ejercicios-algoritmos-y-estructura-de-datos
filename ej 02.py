def Cociente(var1,var2):
	cociente=var1/var2
	return cociente

var1=int(input("Ingrese el primer valor: "))
var2=int(input("Ingrese segundo valor: "))

resultado=Cociente(var1,var2)
print(resultado)
if resultado < 1:
	print("ERROR \nEl resultado fue cero")
elif resultado != 0:
	print("El cociente es: %d" %(resultado))

def Suma (var1, var2):
	suma=var1+var2
	return suma

def Resta (var1,var2):
	resta=var1-var2
	return resta

def Producto (var1,var2):
	prod=var1*var2
	return prod



var1=int (input("Ingrese primer valor: "))
var2=int (input("Ingrese segundo valor: "))

eleccion=int(input("Ingrese el numero de la  operacion a realizar: \n1-Suma \n2-Resta \n3-Producto \nOPERACION: "))

if eleccion == 1:
	valorsuma=Suma(var1,var2)
	print("LA suma es: %d" %(valorsuma))

elif eleccion ==2:
	valorresta=Resta(var1,var2)
	print("La resta es: %d" %(valorresta))

elif eleccion ==3:
	 valorprod=Producto(var1,var2)
	 print("El producto es: %d" %(valorprod))
else:
	print("No se ha ingresado una operacion correcta.")



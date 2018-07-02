fin=False
nombres_y_fechas={}
cont=0
nombremayor=0
nombremenor=0
import datetime
while fin == False:
	nombre=input("Ingrese nombre: ")
	if nombre == "fin":
		fin=True
	else:
		nombres_y_fechas[nombre]=0
		f= input("Ingrese fecha de nacimiento formato (ddmmaaaa) : ")
		fecha= datetime.datetime.strptime(f, '%d%m%Y')
		if cont == 0:
			fechamayor=fecha
			fechamenor=fecha
		else:
			if fecha < fechamayor:
				nombremayor= nombre

			if fecha > fechamenor:
				nombremenor= nombre

		nombres_y_fechas[nombre]= fecha
	cont+=1
		#print (nombres_y_fechas)


print("La persona mas vieja es: ",nombremayor)
print("La persona mas joven es: ",nombremenor)
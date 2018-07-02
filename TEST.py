trigger= False
cont_octubre= cont_antes1990= cont_primavera = 0
persona_vieja= 0
def PedirDatos():
	dia= int(input("Ingrese dia de nacimiento: "))
	mes= int(input("Ingrese mes de nacimiento: "))
	anio= int(input("Ingrese anio de nacimiento: "))
	sexo= input("Ingrese sexo (M) o (F): ")
	return dia, mes, anio, sexo


def MostrarResultado(cont_octubre, cont_antes1990, cont_primavera)


while trigger == False:
	dia= int(input("Ingrese dia de nacimiento: "))
	mes= int(input("Ingrese mes de nacimiento: "))
	anio= int(input("Ingrese anio de nacimiento: "))
	sexo= input("Ingrese sexo (M) o (F): ")

	if dia == 0:
		trigger = True
		break:


	if mes == 10:
		cont_octubre+= 1

	if anio < 1990:
		if mes < 7:
			if dia < 9:
				cont_antes1990+= 1


	if sexo == "F":
		if mes >= 9 and dia >= 22 and mes <= 12 and dia <=21:
		cont_primavera+= 1 



trigger= False
cont_octubre= cont_antes1990= cont_primavera= cont= 0
persona_vieja= 0

def MostrarResultado(cont_octubre, cont_antes1990, cont_primavera, persona_vieja_sexo, persona_vieja_dia, persona_vieja_mes, persona_vieja_anio):
	print("\nHubo %d nacimientos en el mes de octubre"%(cont_octubre))
	print("Hubo %d nacimientos antes del 9 de Julio de 1990"%(cont_antes1990))
	print("Hubo %d nacimientos de mujeres en la primavera de 1982"%(cont_primavera))
	print("El sexo de la persona mas vieja es: ",persona_vieja_sexo, " que nacio el %d/%d/%d " %(persona_vieja_dia,persona_vieja_mes,persona_vieja_anio))


while trigger == False:
	dia= int(input("\nIngrese dia de nacimiento: "))
	if dia == 0:
		trigger = True
		break
	mes= int(input("Ingrese mes de nacimiento: "))
	anio= int(input("Ingrese anio de nacimiento: "))
	sexo= input("Ingrese sexo (M) o (F): ")

	if mes == 10:
		cont_octubre+= 1

	if anio <= 1990:
		if mes <= 7:
			if dia < 9:
				cont_antes1990+= 1


	if sexo == "F":
		if anio == 1982:
			if mes >= 9 and dia >= 22:
				if mes <= 12:
					if mes == 12 and dia > 21:
						pass
					else:
						cont_primavera=+1

	if cont == 0:
		persona_vieja_dia = dia
		persona_vieja_anio= anio
		persona_vieja_mes= mes
		persona_vieja_sexo = sexo


	if anio < persona_vieja_anio:
		persona_vieja_anio = anio
		persona_vieja_mes = mes
		persona_vieja_dia = dia
		persona_vieja_sexo = sexo
	else:
		if anio == persona_vieja_anio and  mes < persona_vieja_mes:
			persona_vieja_anio = anio
			persona_vieja_mes = mes
			persona_vieja_dia = dia
			persona_vieja_sexo = sexo
		else:
			if anio == persona_vieja_anio and mes == persona_vieja_mes and dia < persona_vieja_dia:
				persona_vieja_anio = anio
				persona_vieja_mes = mes
				persona_vieja_dia = dia
				persona_vieja_sexo = sexo

	cont+= 1

MostrarResultado(cont_octubre,cont_antes1990,cont_primavera, persona_vieja_sexo, persona_vieja_dia, persona_vieja_mes, persona_vieja_anio)







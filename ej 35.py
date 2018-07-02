lista_primario_completo= []
lista_prom_familias= []
sin_estudios= 0
cantidad_total= 0
analfabetos= 0
edad_ciudad= 0
cant_p= 0
cant_s= 0
cant_t= 0
cant_u= 0
cant_femeninas= 0
mayor_cantidad_integrantes=0
dom_mayor_cantidad_integrantes= None
porcentaje_masculinos= 0
porcentaje_femenino= 0

direccion= input("Ingrese direccion: ")
tipo_vivienda= input("Ingrese tipo de vivienda, CASA (C) o DEPARTAMENTO (D): ")
cantidad= int(input("Ingrese cantidad de integrantes: "))
cantidad_total= cantidad_total + cantidad

if cantidad > mayor_cantidad_integrantes and tipo_vivienda == "D":
	mayor_cantidad_integrantes= cantidad
	dom_mayor_cantidad_integrantes= direccion

while cantidad > 0:
	edad_familia= 0 # REINICIAMOS LOS VALORES A 0
	prom_edad_familia= 0

	for i in range(0,cantidad):
		nombre_apellido= input("\nIngrese  el nombre y apellido del integrante: ")
		edad= int(input("Ingrese la edad del integrante: "))
		sexo= input("Ingrese el sexo del integrante (M) o (F): ")
		if sexo == "F":
			cant_femeninas+=1


		nivel_estudios= input("Ingrese el nivel de estudios alcanzado (N) no posee (P) primario (S) secunadario (T) terciario o (U) universitario: ")

		if nivel_estudios == "S" or nivel_estudios == "T" or nivel_estudios == "U":
			lista_primario_completo.append(nombre_apellido)
		elif nivel_estudios == "N":
			sin_estudios= sin_estudios + 1
		if nivel_estudios == "N":
			analfabetos= analfabetos + 1
		else:
			estado_estudio=input("Ingrese el estado del estudio, incompleto(I) o completo (C): ")
			if nivel_estudios == "P" and estado_estudio == "C":
				lista_primario_completo.append(nombre_apellido)

		if nivel_estudios == "P" and estado_estudio == "I":
			cant_p+= 1
		if nivel_estudios == "S" and estado_estudio == "I":
			cant_s+= 1
		if nivel_estudios == "T" and estado_estudio == "I":
			cant_t+= 1
		if nivel_estudios == "U" and estado_estudio == "I":
			cant_u+= 1
		edad_familia=edad_familia + edad ## SUMA GENERAL DE EDAD EN LA FAMILIA



	edad_ciudad=edad_ciudad + edad_familia ## SUMA GENERAL DE EDAD EN LA CIUDAD

	prom_edad_familia= edad_familia / cantidad ## PROMEDIO DE EDAD EN CADA FAMILIA
	lista_prom_familias.append(prom_edad_familia) ## SE AGREGA A UNA LISTA EL PROMEDIO DE EDAD DE CADA FAMILIA

	direccion= input("\nIngrese direccion: ")
	tipo_vivienda= input("Ingrese tipo de vivienda, CASA (C) o DEPARTAMENTO (D): ")
	cantidad= int(input("Ingrese cantidad de integrantes: "))

	if cantidad > mayor_cantidad_integrantes and tipo_vivienda == "D":
		mayor_cantidad_integrantes= cantidad ## SE OBTIENE LA DIRECCION DEL DEPARTAMENTO CON MAYOR CANTIDAD DE INTEGRANTES
		dom_mayor_cantidad_integrantes= direccion

	cantidad_total= cantidad_total + cantidad

porcentaje_analfabetos= (analfabetos*100) / cantidad_total ## SE OBTIENE EL PORCENTAJE DE ANALFABETOS EN LA CIUDAD
prom_edad_ciudad= edad_ciudad / cantidad_total ## PROMEDIO DE EDAD EN LA CIUDAD
cant_masculinos= cantidad_total - cant_femeninas
porcentaje_masculinos= (cant_masculinos*100) / cantidad_total
porcentaje_femenino= 100 - porcentaje_masculinos


print("\n Las personas que completaron los estudios primarios son: ", lista_primario_completo)
print("\n El porcentaje de analfabetismo en la ciudad es %",porcentaje_analfabetos)
print("\n El departamento con mayor cantida de integrantes es: ",dom_mayor_cantidad_integrantes, "con ", mayor_cantidad_integrantes," integrantes")
print("\n La edad promedio en la ciudad es: ", prom_edad_ciudad)
print("\n El promedio de edad en cada familia, del primero al ultimo, es ", lista_prom_familias)
print("\n La cantidad de encuestados con estudios imcompletos es: Primarios %d Secundarios %d Terciarios %d Universitarios %d" %(cant_p, cant_s, cant_t, cant_u))
print("\n El porcentaje de encuestados de sexo femenino es %",porcentaje_femenino," mientras que el porcentaje de sexo masculino es %",porcentaje_masculinos)


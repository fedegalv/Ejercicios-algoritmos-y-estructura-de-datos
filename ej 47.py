def sumarHora(h,t):
	lista_h=[]
	lista_t=[] ## CREA LAS LISTAS

	lista_h.append(h[0:2])
	lista_h.append(h[2:4]) ## TOMA LOS CARACTERES EN PARES DEL STRING h , Y LAS ASIGNA EN LA LISTA lista_h EN ORDEN
	lista_h.append(h[4:6])

	lista_t.append(t[0:2])
	lista_t.append(t[2:4]) ## MISMO PERO CON T
	lista_t.append(t[4:6])

	lista_h = list(map(int, lista_h)) ## CONVIERTES EL CONTENIDO DE LAS LISTAS A INT
	lista_t = list(map(int, lista_t))

	suma_hora= lista_h[0]+lista_t[0]  ## HACE LAS SUMATORIAS DE LOS int EN LAS LISTAS, CADA UNO CON LO QUE CORRESPONDE(POSICION 0 ES LA HORA, SUMA hora Y hora ,ETC)
	suma_min= lista_h[1]+lista_t[1]
	suma_segundo= lista_h[2]+lista_t[2]

	
	if suma_hora > 24:  ## USANDO COMO FORMATO UN RELOJ DE 24:59:59, SE COMPARA LA HORA SUMADA Y SE CORRIGE. EJ: EL RESULTADO DE LA SUMA ES 25, LA DIFERENCIA ENTRE ESTA Y EL ESTANDAR 24 ES LA HORA FINAL, EN ESTE CASO 01 DE LA MANIANA
		suma_hora-=24

	if suma_min > 60:
		suma_min= suma_min - 60 ## MISMO QUE LO ANTERIOR PERO, SI LA SUMA DE MINUTOS LLEGA A SUPERAR 60, SE REALIZA LA OPERACION MARCADA, SE  "REINICIA" EL RELOJ Y A ESTE SE LE SUMA EL RESULTADO DE LA RESTA
		suma_hora+=1 ## AL PASAR LOS 60 MIN, SE ENTIENDE LA HORA AVANZA 1

	if suma_segundo > 60:
		suma_segundo= suma_segundo - 60
		suma_min +=1

	print("La hora resultado es: %02d:%02d:%02d" %(suma_hora,suma_min,suma_segundo))





h= input("Ingrese la hora base: ")
t= input("Ingrese la hora a sumar: ")

sumarHora(h,t)
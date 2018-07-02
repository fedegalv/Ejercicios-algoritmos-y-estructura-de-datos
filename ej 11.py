import calendar
def esBisiesto(year):
    return calendar.isleap(year)

fechas={"ENERO":31, "FEBRERO":28, "MARZO":31, "ABRIL":30, "MAYO":31, "JUNIO":30, "JULIO":31, "AGOSTO":31, "SEPTIEMBRE":30, "OCTUBRE":31, "NOVIEMBRE":30, "DICIEMBRE":31}
mes=str(input("Ingrese mes: "))
mes=mes.upper()

ano=int(input("Ingrese anio: "))

bisiesto=esBisiesto(ano)

if bisiesto:
	fechas["FEBRERO"]=29
#print(fechas["Febrero"])
print("El mes",mes,"tiene",fechas[mes],"dias")
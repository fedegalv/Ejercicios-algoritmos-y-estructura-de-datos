class Abonos():
	def __init__(self):
		costo = None
		minutos_libres= None
		cargo_min_exced= None


def toMin(tiempo):
	hora=tiempo[0:2]
	minutos=tiempo[2:]

	minutos_convertidos= int(hora) * 60
	total_min= minutos_convertidos+int(minutos)
	
	return total_min

def MinExc_e_IVA(plan, tiempo_utilizado):

	if plan == "A":
		abono= plan_a.costo
		min_libres= plan_a.minutos_libres_plan
		cargo_min_excedente = plan_a.cargo_min_exced_plan

	if plan == "B":
		abono= plan_b.costo
		min_libres= plan_b.minutos_libres_plan
		cargo_min_excedente = plan_b.cargo_min_exced_plan

	if plan == "C":
		abono= plan_c.costo
		min_libres= plan_c.minutos_libres_plan
		cargo_min_excedente = plan_c.cargo_min_exced_plan

	if plan == "D":
		abono= plan_d.costo
		min_libres= plan_d.minutos_libres_plan
		cargo_min_excedente = plan_d.cargo_min_exced_plan

	if plan == "E":
		abono= plan_e.costo
		min_libres= plan_e.minutos_libres_plan
		cargo_min_excedente = plan_e.cargo_min_exced_plan

	min_utilizados = tiempo_utilizado

	min_excedidos = min_utilizados - min_libres
	totalcon_exceso = (min_excedidos * cargo_min_excedente) + abono
	total_mas_iva= ((21 * totalcon_exceso)/100) + totalcon_exceso

	return min_excedidos, total_mas_iva, min_libres

plan_a= Abonos()
plan_a.costo= 70
plan_a.minutos_libres_plan= 300
plan_a.cargo_min_exced_plan= 0.9

plan_b=Abonos()
plan_b.costo= 55
plan_b.minutos_libres_plan= 200
plan_b.cargo_min_exced_plan = 0.15

plan_c= Abonos()
plan_c.costo= 40
plan_c.minutos_libres_plan= 100
plan_c.cargo_min_exced_plan= 0.21

plan_d= Abonos()
plan_d.costo= 28
plan_d.minutos_libres_plan= 60
plan_d.cargo_min_exced_plan= 0.29

plan_e= Abonos()
plan_e.costo= 19
plan_e.minutos_libres_plan= 40
plan_e.cargo_min_exced_plan= 0.37
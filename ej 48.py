import math
def esPrimo(n):
	# Returns True if num is a prime number, otherwise False.
	if n < 2:
		return False
	# see if num is divisible by any number up to the square root of num # VE SI SI num ES DIVISIBLE POR CUALQUIER NUMERO HASTA EL CUADRADO DE num
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


n=int(input("Ingrese un numero: "))
if esPrimo(n) == True:
	print("El numero",n,"es primo")
elif esPrimo(n) == False:
	print("El numero",n,"no es primo")
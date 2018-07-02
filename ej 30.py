import math
def isPrime(num):
	# Returns True if num is a prime number, otherwise False.
	if num < 2:
		return False
	# see if num is divisible by any number up to the square root of num # VE SI SI num ES DIVISIBLE POR CUALQUIER NUMERO HASTA EL CUADRADO DE num
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True


num=int(input("Ingrese un numero: "))
if isPrime(num) == True:
	print("El numero ",num, "es primo")
elif isPrime(num) == False:
	print("El numero ", num, "no es primo")
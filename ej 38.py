def factorial (n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

n=int(input("Ingrese un numero para factorizar: "))
if n == 1 or n == 0:
	print("El factorial es: 1")
else:
	fact= factorial(n)
	print("El factorial es : ", fact)


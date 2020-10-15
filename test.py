def multiplication(nombre):
	for x in range(1,13):
		print("{} x {} = {}".format(nombre, x, nombre*x))

n = int(input("Entrer le nombre dont vous voulez la table de multiplication : "))
multiplication(n)
def entire_sqrt():

	i = True
	while i:

		try:
			n = int(input('Entrer un nombre: '))
		except ValueError:
			pass
		else:
			i = False

	if n<0 :
		print("\n{} n'a pas de racine réelle.".format(n))

	else:

		i = 0
		while i**2 != n:
			i+=1
		
			if i > n:
				print("\n{} n'a pas de racine entière.".format(n))
				break   
			elif i**2 == n:
				print("\n{} a pour racine carrée {}".format(n, i))
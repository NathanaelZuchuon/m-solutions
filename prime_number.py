def prime_number(n):

	if n == 0 or n == 1:
		print("{} n'est pas premier.".format(n))

	else:

		i = 2

		while n%i != 0:
			i+=1

		if i < n:
			print("{} n'est pas premier.".format(n))
		elif i == n:
			print("{} est premier.".format(n))

def main():

	while True:

		n = int(input('\nEntrer un nombre:\n'))
		prime_number(n)
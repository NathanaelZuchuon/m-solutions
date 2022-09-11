def fact(n):

	fact = 1

	for i in range(1,n+1):
		fact = fact * i  

	print("Le factoriel de {} est {} .".format(n, fact), end='\n\n')

def main():

	while True:

		n = int(input('Entrer un nombre: '))
		fact(n)

# The RecursionError is reached at n = 95000
def fib(n):

	a, b = 0, 1
	while a < n:
		print(a, end=' \r')
		a, b = b, a + b
def calcular_hipotenusa(a, b):
	return ((a*a) + (b*b))


def soma_hipotenusas(n):
	adicao = 0
	c = 1
	while (c <= n):
		a = 1
		b = 1
		x = (c*c)
		while (a < n):
			while (b < n):
				if (x == calcular_hipotenusa(a, b)):
					a = n
					adicao = adicao + c
					break
				b = b + 1
			a = a + 1
			b = a
		c =  c + 1
	return adicao
    
    

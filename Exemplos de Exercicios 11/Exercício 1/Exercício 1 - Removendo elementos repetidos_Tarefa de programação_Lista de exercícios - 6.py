def remove_repetidos(z):
	lista = z
	x = 0
	while x < len(lista):
		y = x + 1
		while y < len(lista):
			if lista[y] == lista[x]:
				del(lista[y])
			else:
				y = y + 1
		x = x + 1
	return sorted(lista)
    

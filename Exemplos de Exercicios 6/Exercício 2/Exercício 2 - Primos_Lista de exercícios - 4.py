def maior_primo(x):
	if x == 2:
		return(x)
	else:
		if x % 2 == 1:
			return(x)
		else:
			primos = []
			for k in range(x):
				d = 0
				for b in range(x):
					if k%(b+1) == 0:
						d += 1
				if d == 2:
					primos.append(k)
					
			return(max(primos))
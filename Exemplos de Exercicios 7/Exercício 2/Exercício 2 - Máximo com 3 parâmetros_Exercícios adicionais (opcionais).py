def maximo(x,y,z):
	if x > y  and  x > z:
		return x
	elif y > x  and  y > z:
		return y
	else:
		if z > x  and  z > y:
			return z 
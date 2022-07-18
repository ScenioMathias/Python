def n_primos(x):
	cont = 2
	qtd = 0
	n = 0
	while cont <= x:
		if cont == 2:
			qtd = qtd + 1
			cont = cont + 1
		else:
			n = dtc_primo(cont)
			if n == 1:
				qtd = qtd + 1
				cont = cont + 1
			else:
				cont = cont + 1
	return qtd

    
def dtc_primo(cont):
	cont2 = 1
	qtd2 = 0
	qtd = 0
	while cont2 <= cont:
		if cont % cont2 == 0:
			qtd2 = qtd2 + 1
		cont2 = cont2 + 1
	if qtd2 <= 2 :
		qtd = qtd + 1
	return qtd   
	

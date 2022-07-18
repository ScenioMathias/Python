n1 = int(input("Insira o valor do primeiro número inteiro:"))
n2 = int(input("Insira o valor do segundo número inteiro:"))
n3 = int(input("Insira o valor do terceiro número inteiro:"))
x = 1
y = 1
z = 1
if n1 < n2  and  n1< n3:
	x = n1
	if n2 < n3:
		y = n2
		z = n3
		print("crescente")
else:
	print("não está em ordem crescente")
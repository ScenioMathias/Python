n = int(input("Digite um número inteiro:"))
soma = 0
while (n > 0):
	r = n % 10
	n = n // 10
	soma = soma + r


print(soma)
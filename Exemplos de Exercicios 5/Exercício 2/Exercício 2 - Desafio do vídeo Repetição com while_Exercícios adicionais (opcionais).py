número=int(input("Digite um número inteiro:"))
número1=número
resto1=número%10
while número//10!=0:
	número=número//10
	resto=número%10
	if resto==resto1:
		print("sim")
		número=número1
		break
	resto1=resto

	
if número//10==0:
	print("não")


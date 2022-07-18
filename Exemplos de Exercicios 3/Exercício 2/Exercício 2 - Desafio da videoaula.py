import math 
a = int(input("insira o valor do Coeficiente A:"))
b = int(input("insira o valor do Coeficiente B:"))
c = int(input("insira o valor do Coeficiente C:"))
if a==0:
	print("Não é equação do 2° grau, pois, o valor de A é 0.")
else:
	d = (b*b)-(4*a*c)
	if(d<0):
		print("esta equação não possui raízes reais")
	else:
		if (d==0):
			x = -b/(2*a)
			print("a raiz desta equação é",x)
		else:
			x=(-b + math.sqrt(d))/(2*a)
			x2=(-b - math.sqrt(d))/(2*a)
			if x > x2:
				print("as raízes da equação são", x2 ,"e", x)
			else:
				print("as raízes da equação são", x ,"e", x2)
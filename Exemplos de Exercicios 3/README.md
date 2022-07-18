# Exemplos de Exercícios 03

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades  

* Arquivo em Python contendo os 2 exercícios.

## _Exercício 1_
_Este algoritmo irá calcular, através dos valores X e Y inserido, a distância entre dois pontos e informar se está perto ou longe._
```shell
import math 
x = float(input("insira o valor de x:"))
y = float(input("insira o valor de y:"))
x2 = float(input("insira o valor de x2:"))
y2 = float(input("insira o valor de y2:"))
distância = math.sqrt((x - x2)**2 + (y - y2)**2)
if distância >= 10:
	print("longe")
else: 
        print("perto")
```

## _Exercício 2_

_Este algoritmo irá realizar o cálculo de uma equação de segundo grau através dos valores A, B e C inseridos._

```shell
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

```

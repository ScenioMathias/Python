# Exemplos de Exercícios 10

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades  

* Arquivo em Python contendo os 2 exercícios.

## _Exercício 1_
_Este algoritmo irá analisar, com base em cálculos, a quantidade de números primos existentes entre  0 a ‘n’, sendo ‘n’ o número inserido pelo usuário._ 

```shell
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

```
## _Exercício 2_
_Este algoritmo irá calcular, com base nos valores inseridos, o cálculo das hipotenusas e a soma delas._
```shell
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
    
```

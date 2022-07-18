# Exemplos de Exercícios 07

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades  

* Arquivo em Python contendo os 2 exercícios.

## _Exercício 1_
_Este algoritmo irá identificar divisões de 5 ou 3, 3 ou 5 e 5 e 3 com o número inserido. Conforme o número seja divisível por alguma dessas sentenças será printado na tela “FizzBuzz”, “Fizz” e “Buzz”._ 

```shell

def fizzbuzz(x):
	if (x % 3 == 0) and (x % 5 !=0):
		return ('Fizz')
	elif (x % 5 == 0) and (x % 3 !=0):
		return ('Buzz')
	else:
		if (x % 3 == 0) and (x % 5 == 0):
			return ('FizzBuzz')
		else:
			return (x)
    
```
## _Exercício 2_
_Este algoritmo irá identificar, por meio de comparativos, o maior valor dentre os 3 números inseridos e organizá-los em ordem crescente._

```shell
def maximo(x,y,z):
	if x > y  and  x > z:
		return x
	elif y > x  and  y > z:
		return y
	else:
		if z > x  and  z > y:
			return z 
```

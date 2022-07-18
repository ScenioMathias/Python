# Exemplos de Exercícios 04

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades  

* Arquivo em Python contendo os 3 exercícios.

## _Exercício 1_
_Este algoritmo irá realizar o cálculo de fatorial de um número inserido._
```shell
número = int(input("Digite o valor de n:"))
fatorial = 1
while número > 1:
   fatorial = fatorial * número
   número = número - 1


print(fatorial)

```
## _Exercício 2_
_Este algoritmo irá apresentar a sequência de impares de acordo com o número inserido._
```shell

número = int(input("Digite o valor de n:"))
retorno = 1
ímpares = 1
while retorno <= número:
	print (ímpares)
	ímpares = ímpares + 2
	retorno = retorno + 1
  
 ```
 ## _Exercício 3_
 _Este algoritmo irá realizar a soma dos dígitos do número inserido pelo usuário._
 ```shell
 n = int(input("Digite um número inteiro:"))
soma = 0
while (n > 0):
	r = n % 10
	n = n // 10
	soma = soma + r


print(soma)
 
 ```


# Exemplos de Exercícios 02

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades 1, 2, 3, 4 e 5 

* Arquivo em Python contendo os 5 exercícios.

## _Exercício 1_

_Este algoritmo informará se o número inserido é par ou ímpar._ 

```shell
número = int(input("Insira um número inteiro:"))
if número % 2 == 0:
 print("par")
else:
 print("ímpar")
```
## _Exercício 2_
_Este algoritmo irá analisar se o número inserido é divisível por 3, caso for, será pintado na tela a palavra “Fizz”._ 
```shell
número = int(input("Insira um número inteiro:"))
if número % 3 == 0:
  print("Fizz")
else: 
  print(número)
  ```
  
  ## _Exercício 3_
  _Este algoritmo irá analisar se o número inserido é divisível por 5, caso for, será pintado na tela a palavra “Buzz”._ 
  ```shell
  número = int(input("Insira um número inteiro:"))
if número % 5 == 0:
  print("Buzz")
else: 
  print(número)
  ```
  
  ## _Exercício 4_
  _Este algoritmo irá analisar se o número inserido é divisível por 3 e por 5, caso for, será pintado na tela a palavra “FizzBuzz”_
  ```shell
  número = int(input("Insira um número inteiro:"))
if número % 3 == 0 and número % 5 == 0:
    print("FizzBuzz")
else: 
    print(número)
  
 ```
 ## _Exercício 5_
 _Este algoritmo irá analisar se os números inseridos estão em ordem crescente._
 
 ```shell
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
   ```
  

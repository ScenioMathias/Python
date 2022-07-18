# Exemplos de Exercícios 09

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades  

* Arquivo em Python contendo os 2 exemplos.

## _Exercício 1_
_Este algoritmo irá desenvolver, com base em cálculos, uma matriz._ 

```shell
def main():
	width = int(input("Digite a largura: "))
	height = int(input("Digite a altura: "))
	character = "#"
	retângulo(width, height, character)

def retângulo(width, height, character):
	line = character * width
	for i in range(height):
		print(line)

main()

```

## _Exercício 2_
_Este algoritmo irá desenvolver, com base em cálculos, uma matriz sem preenchimento interno._
```shell
def main():
	width = int(input("Digite a largura: "))
	height = int(input("Digite a altura: "))
	height = height - 2
	character = "#"
	retangulo(width, height, character)
	

def retangulo(width, height, character):
	print(character * width)
	
	for i in range(height):
		espacos = (width - 2) * ' '
		print("%s%s%s" % (character, espacos, character))
		
	print(character * width)
	
	
main()

```

# Exemplos de Exercícios 11

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades  

* Arquivo em Python contendo os 2 exercícios.

## _Exercício 1_
_Este algoritmo irá eliminar palavras repetidas em uma determinada lista, com base em cálculos realizados._ 

```shell
d = ['Python', 'Academy', 'Academy']
def remove_repetidos(z):
	lista = z
	x = 0
	while x < len(lista):
		y = x + 1
		while y < len(lista):
			if lista[y] == lista[x]:
				del(lista[y])
			else:
				y = y + 1
		x = x + 1
	return sorted(lista)
  
remove_repetidos(d)
```

## _Exercício 2_
_Esse algoritmo irá somar todos os valores numéricos pertencentes em uma determinada lista._

```shell
d = [2,2,2]

def soma_elementos(z):
    y = z
    a = 0
    for x in range(len(y)):
      a += y[x]
    return a
 
soma_elementos(d)

print ("Resultado", soma_elementos(d))

```

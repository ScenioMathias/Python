# Exemplos de Exercícios 06

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades  

* Arquivo em Python contendo os 3 exercícios.

## _Exercício 1_
_Este algoritmo irá identificar, por meio de cálculos, qual valor maior dentre os números inseridos._ 

```shell

def maximo(x,y): 
    if x > y: 
       return(x)
    else: 
       return(y)


x = input("Digite o valor de x:")
y = input("Digite o valor de y:")
print("O maior valor entre os dois inseridos é:", maximo(x,y))
    
```
## _Exercício 2_
_Este algoritmo irá identificar, por meio de cálculos, qual o maior número primo do número inserido._ 


```shell
def maior_primo(x):
	if x == 2:
		return(x)
	else:
		if x % 2 == 1:
			return(x)
		else:
			primos = []
			for k in range(x):
				d = 0
				for b in range(x):
					if k%(b+1) == 0:
						d += 1
				if d == 2:
					primos.append(k)
					
			return(max(primos))
      
 ```  
 ## _Exercício 3_
 
 _Este algoritmo irá identificar, por meio de cálculos, se a letra inserida é vogal ou não._ 
 ```shell
 
 def vogal(z):
	if (z == 'a') or (z == 'e') or (z == 'i') or (z == 'o') or (z == 'u') or (z == 'A') or (z == 'E') or (z == 'I') or (z == 'O') or (z == 'U'):
		return True
	else:
		return False 
 ```   
 

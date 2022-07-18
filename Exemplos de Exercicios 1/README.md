# Exemplos de Exercícios 01 

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades 1,2 e 3

* Arquivo em Python contendo os 3 exercícios.

## _Exercício 1_

_Este algoritmo realiza a área e perímetro de um quadrado, através das informações dos lados do quadrado._ 

```shell
a = input("Digite o valor correspondente ao lado de um quadrado:")
a = float(a)
x = a * 4
y = a * a 
print("perímetro:",x,"- área:",y)
```

_Este algoritmo apresenta os dados de vencimento de uma fatura do cliente, após o mesmo inseri-los no computador._
```shell
nome = input("Digite o nome do cliente:")
dv = input("Digite o dia de vencimento:")
mv = input("Digite o mês de vencimento:")	
vf= input("Digite o valor da fatura:")
print("Olá,",nome)
print("A sua fatura com vencimento em",dv,"de",mv,"no valor de R$",vf,"está fechada.")
```
## _Exercício 2_
_Este algoritmo fará uma média aritmética das notas inseridas pelo usuário._
```shell
n1 = input("Digite a primeira nota:")
n1 = float(n1)
n2 = input("Digite a segunda nota:")
n2 = float(n2)
n3 = input("Digite a terceira nota:")
n3 = float(n3)
n4 = input("Digite a quarta nota:")
n4 = float(n4)
x = n1 + n2 + n3 + n4
y = x / 4 
print("A média aritmética é:",y)
```
_Este algoritmo fará uma conversão de segundos para quantidade de dias, horas, min e segundos._
```shell
seg = input("Por favor, entre com o número de segundos que deseja converter:")
seg = int(seg)
dia = 86400
qd = seg / dia 
qd = int(qd)
r =  seg % dia 
hr = 3600
qh = r / hr 
qh = int(qh)
r = seg %  hr
min = 60 
qm = r / min 
qm = int(qm)
segundos = r % min 
print(qd,"dias,",qh,"horas,",qm,"min e",segundos,"segundos.")
```
## _Exercício 3_
_Este algoritmo fará contagem das dezenas que contém em um certo número inserido._
```shell
num = input("Digite um número inteiro:")
num = int(num)
divint = num // 10 
valdez = divint % 10
print("O dígito das dezenas é",valdez)
```

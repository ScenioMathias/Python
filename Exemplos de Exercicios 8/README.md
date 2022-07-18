# Exemplos de Exercícios 08

<img src="https://github.com/ScenioMathias/APL-2/blob/main/ALP.png?raw=true" alt="smashupy" width="700"/>

## Atividades  

* Arquivo em Python contendo os 3 exemplos.

## _Exercício 1_
_Nim é um jogo de dois jogadores que usam peças alinhadas em várias colunas. Você vai jogar contra o computador. Os jogadores realisam jogadas alternativas. Um movimento consiste em elevar algumas peças de uma única coluna; o número de peças removidas está decidido pelo jogador a mover._ 

_Para mover, desloca o mouse sobre as peças, clicando quando você quiser remover as peças verdes. O jogo acaba quando não houver mais peças disponíveis. O jogador que fez a última jogada, ganha._ 

```shell

def computador_escolhe_jogada(n, m):    
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m

def usuario_escolhe_jogada(n, m):
    q = int(input("\nQuantas peças você vai tirar? "))
    while q > m or q <= 0 or q > n:    
        print("Oops! Jogada inválida! Tente de novo.")
        q = int(input("\nQuantas peças você vai tirar? "))
        
    return q

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m < 1:
        print("A quantidade de peças por jogadas devem ser menor ou igual as peças totais")
        m = int(input("Limite de peças por jogada? "))
    
    q = 0
    placar = 0
    if (n % (m+1)) == 0:
        print("Você começa!")
        placar = 1 
        while n > 0:
            if placar == 1:
                q = usuario_escolhe_jogada(n,m)
                print("Você tirou", q, "peça.")
                n = n - q
                print("Agora restam", n, "peças no tabuleiro.")
                placar = 2
            else:
                q = computador_escolhe_jogada(n,m)
                print("O computador tirou", q, "peça")
                n = n - q
                print("Agora restam", n, "peças no tabuleiro.")
                placar = 1
                
        if placar == 1:
            print("Fim do jogo! O computador ganhou!")
            return 2 #Ponto para o computador
        else:
            print("Fim do jogo! O você ganhou!")
            return 1 
                
    else:
        print("Computador começa!")
        placar = 2 
        while n > 0:
            if placar == 2:
                q = computador_escolhe_jogada(n, m)
                print("O computador tirou", q, "peça")
                n = n - q
                print("Agora restam", n, "peças no tabuleiro.")
                placar = 1
            else:
                q = usuario_escolhe_jogada(n, m)
                print("Você tirou", q, "peça.")
                n = n - q
                print("Agora restam", n, "peças no tabuleiro.")
                placar = 2
                
        if placar == 1:
            print("Fim do jogo! O computador ganhou!")
            return 2 
        else:
            print("Fim do jogo! O você ganhou!")
            return 1 

def campeonato():
    qtdpartida = 1
    pontuacao_com = pontuacao_jogador = 0
    
    while qtdpartida < 4:
        print("Rodada",qtdpartida)
        if partida() == 1:
            pontuacao_jogador = pontuacao_jogador + 1
        else:
            pontuacao_com = pontuacao_com + 1
        qtdpartida = qtdpartida + 1
        
    print("Final do campeonato!")
    print("Placar: Você", pontuacao_jogador, "X", pontuacao_com, "Computador")

def main():
    print("Bem-vindo ao jogo do NIM!")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input("Escolha: "))    
    while escolha != 1 and escolha != 2:
        print("Escolha uma opção válida!")
        escolha = int(input("Escolha: "))
        
    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    else:
        if escolha == 2:
            print("Você escolheu um campeonato!")
            campeonato()

main()
    
```
### _Exemplo 2_

```Shell
def partida():
    # Solicita os valores de n e m
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    # Define um controlador para quem irá começar o jogo
    x = n % (m + 1)
    # Define um controlador para mensagem que avisa quem irá começar
    primeira_vez_usuario = False
    primeira_vez_computador = False

    if x != 0: # Define que o computador irá começar
        pcJoga = True
        primeira_vez_computador = True # Define que é a primeira jogada do computador
    if x == 0: # Define que o usuário irá começar
        pcJoga = False
        primeira_vez_usuario = True # Define que é a primeira jogada do usuário
    # Entuanto tiver peças(n) no jogo...
    while n > 0:
        if pcJoga == True: # Verifica se o computador começa
            if primeira_vez_computador == True: # Verifica se é a primeira vez do computador
                print("")
                print("Computador começa!")
                print("")
            primeira_vez_computador = False # Define que o computador já jogou a primeira vez
            # Variavel recebendo retorno do número de peças que o computador tirou
            vlr_tirado = computador_escolhe_jogada(n,m)
            # Define que é a vez do usuário
            pcJoga = False
            # Definindo se a mensagem é ficará no singular ou no plural
            if vlr_tirado == 1:
                print("O computador tirou uma peça")
            else:
                print("O computador tirou ",vlr_tirado," peças.")
        else: # Se não for o computador quem começa, então é o usuario...
            # Verifica se é a primeira vez do usuário
            if primeira_vez_usuario == True:
                print("")
                print("Voce começa!")
                print("")
            primeira_vez_usuario = False # Define que o usuário já jogou a primeira vez
            # Variavel recebendo retorno do número de peças que o usuário tirou
            vlr_tirado = usuario_escolhe_jogada(n,m)
            # Define que é a vez do computador
            pcJoga = True
            # Definindo se a mensagem é ficará no singular ou no plural
            if vlr_tirado == 1:
                print("Você tirou uma peça")
            else:
                print("Voce tirou",vlr_tirado,"peças.")
        n = n - vlr_tirado # Remove do tabuleiro as respectivas peças tirada de cada rodada.
        # Para não mostrar que restam 0 peças
        if n > 0:
            print("Agora restam",n,"peças no tabuleiro.")
            print("")
    # Verifica quem jogou por último, e mostra a mensagem respectiva
    if pcJoga == True:
        print("Fim do jogo! Você ganhou!")
        print("")
        return 1 # ID para contabilizar quantas partidas o usuário ganhou no campeonato
    else:
        print("Fim do jogo! O computador ganhou!")
        print("")
        return 0 # ID para contabilizar quantas partidas o computador ganhou no campeonato


# Função que retorna quantas peças o usuário irá tirar do tabuleiro
def usuario_escolhe_jogada(n,m):
    vlr_tirado = 0
    # Enquanto o usuário não digitar um valor válido, ficará preço aqui
    while vlr_tirado == 0:
        vlr_tirado = int(input("Quantas peças você vai tirar?"))
        # Verifica se o valor digitado pelo usuário é valido
        if vlr_tirado > n or vlr_tirado > m or vlr_tirado < 1 :
            print("")
            print("Oops! Jogada inválida! Tente de novo.")
            print("")
            vlr_tirado = 0 # Se for inválido mostra a msg e retorna para o loop
    return vlr_tirado # Se não, retorna o valor tirado


# Função que retorna quantas peças o computador irá tirar do tabuleiro
def computador_escolhe_jogada(n,m):
    if n <= m: # Se o numero de peças for menor que o máximo
        return n # Apenas retorna o mesmo numero de peças para tirar e ganhar logo
    else:
        sobrou = n % (m+1) # sobrou recebe o resto da divisão
        if sobrou > 0:  # Já que não é menor que m, e maior que 0 então...
            return sobrou # retorne o resto
        return m # Se não, retorne o máximo de peças possíveis


# Função que chama partida 3 vezes
def campeonato():
    # Define um controle de placar
    computador = 0
    usuario = 0
    # Define um controle de partidas
    i = 1
    for _ in range(3):
        print("**** Rodada",i,"****")
        print("")
        id_ganhou = partida()
        i = i + 1 # Conta as partidas
        if id_ganhou == 1:
            usuario = usuario +1 # Conta pontos para usuário no placar
        else:
            computador = computador + 1 # Conta pontos para o computador no placar
    print("**** Final do campeonato! ****")
    # Mostra os respectivos placares...
    print("Placar: Você",usuario,"X",computador,"Computador")

# O programa começa aqui, o usuário irá definir a modalidade
escolha = 0
while escolha == 0:
    print("")
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    escolha = int(input())
    if escolha == 1:
        partida() #Inicia uma partida
        break
    elif escolha == 2:
        print("Voce escolheu um campeonato!")
        print("")
        campeonato() # Inicia um campenato
        break
    else:
        print("Escolha uma opção válida!")
        print("")
        escolha = 0 # Volta para o loop, enquanto não escolher 1 ou 2
```


### _Exemplo 3_

```Shell
﻿def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))
	while m < 1:
		print("A quantidade de peças por jogadas devem ser menor ou igual as peças totais")
		m = int(input("Limite de peças por jogada? "))
	if n % (m+1) == 0:
		print("Voce começa!")
		placar = 1
		while n > 0:
			if placar == 1:
				n = usuario_escolhe_jogada(n, m)
				placar = 2
			else:
				n = computador_escolhe_jogada(n, m)
				placar = 1
		if placar == 1:
			return 1
		else:
			return 2
	else:
		print("Computador começa!")
		placar = 2
		while n > 0:
			if placar == 2:
				n = computador_escolhe_jogada(n, m)
				placar = 1
			else:
				n = usuario_escolhe_jogada(n, m)
				placar = 2
		if placar == 1:
			return 1
		else:
			return 2

def usuario_escolhe_jogada(n,m):
	if n <= m:
		q = input("Quantas peças você vai tirar?")
		q = int(q)
		if q <= n  and q > 0:
			print("Voce tirou",q,"peças.")
			s = n - q
			if s ==0:
				print("Fim do jogo! você ganhou!")
				return s
			else:
				print("Voce tirou",q,"peças.")
				print("Agora resta apenas",s,"peça no tabuleiro.")
				return s
		else:
			while q > n or q <0:
				print("Oops! Jogada inválida! Tente de novo.")
				q = input("Quantas peças você vai tirar?")
				q = int(q)
			print("Voce tirou",q,"peças.")
			s = n - q
			if s ==0:
				print("Fim do jogo! você ganhou!")
				return s
			else:
				print("Agora resta apenas",s,"peça no tabuleiro.")
				return s
	else:
		q = input("Quantas peças você vai tirar?")
		q = int(q)
		if q <=m  and q > 0:
			s = n - q
			print("Voce tirou",q,"peças.")
			print("Agora resta apenas",s,"peça no tabuleiro.")
			return s
		else:
			while q > m or q <0:
				print("Oops! Jogada inválida! Tente de novo.")
				q = input("Quantas peças você vai tirar?")
				q = int(q)
			print("Voce tirou",q,"peças.")
			s = n - q
			if s ==0:
				print("Fim do jogo! você ganhou!")
				return s
			else:
				print("Agora resta apenas",s,"peça no tabuleiro.")
				return s
  


def computador_escolhe_jogada(n,m):
	if m >= n:
		if n % (m+1) > 0:
			r = n - (n % (m+1))
			print("O computador tirou",n,"peças.")
			if r ==0:
				print("Fim do jogo! você ganhou!")
				return r
			else:
				print("O computador tirou",n,"peças.")
				print("Agora resta apenas",r,"peça no tabuleiro.")
				return r
	else:
		r = n - m
		print("O computador tirou",m,"peças.")
		print("Agora resta apenas",r,"peça no tabuleiro.")
		return r

def campeonato():
    qtdpartida = 1
    pontuacao_com = pontuacao_jogador = 0
    
    while qtdpartida < 4:
        print("Rodada",qtdpartida)
        if partida() == 2:
            pontuacao_jogador = pontuacao_jogador + 1
        else:
            pontuacao_com = pontuacao_com + 1
        qtdpartida = qtdpartida + 1
        
    print("Final do campeonato!")
    print("Placar: Você", pontuacao_jogador, "X", pontuacao_com, "Computador")


def main():
    print("Bem-vindo ao jogo do NIM!")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input("Escolha: "))    
    while escolha != 1 and escolha != 2:
        print("Escolha uma opção válida!")
        escolha = int(input("Escolha: "))
        
    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    else:
        if escolha == 2:
            print("Você escolheu um campeonato!")
            campeonato()
```

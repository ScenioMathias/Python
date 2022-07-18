def partida():
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

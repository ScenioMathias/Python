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

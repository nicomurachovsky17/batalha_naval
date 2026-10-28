import random

from funcoes import (
    preenche_frota,
    posicao_valida,
    posiciona_frota,
    faz_jogada,
    afundados,
    monta_tabuleiros
)


# Posicionamento da frota do jogador
frota = {}

nomes = ["porta-aviões", "navio-tanque", "contratorpedeiro", "submarino"]
tamanhos = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]

for i in range(len(nomes)):
    nome = nomes[i]
    tamanho = tamanhos[i]

    for j in range(quantidades[i]):
        valida = False

        while not valida:
            print(
                f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}"
            )

            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))

            if nome == "submarino":
                orientacao = "vertical"
            else:
                escolha = int(
                    input("Orientação: [1] Vertical [2] Horizontal ")
                )

                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            valida = posicao_valida(
                frota, linha, coluna, orientacao, tamanho
            )

            if valida:
                frota = preenche_frota(
                    frota, nome, linha, coluna, orientacao, tamanho
                )
            else:
                print("Esta posição não está válida!")


# Posicionamento padrão da frota do oponente
frota_oponente = {
    "porta-aviões": [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    "navio-tanque": [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    "contratorpedeiro": [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    "submarino": [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}


# Criação dos tabuleiros
tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

total_navios = 0

for nome_navio in frota_oponente:
    total_navios += len(frota_oponente[nome_navio])

total_navios_jogador = 0

for nome_navio in frota:
    total_navios_jogador += len(frota[nome_navio])

# Posições que o oponente já atacou
posicoes_ja_sorteadas = []


# Loop principal do jogo
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    # Jogada do jogador
    posicao_inedita = False

    while not posicao_inedita:
        linha = int(input("Jogador, qual linha deseja atacar? "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if tabuleiro_oponente[linha][coluna] in ["X", "-"]:
            print(
                f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!"
            )
        else:
            posicao_inedita = True

    tabuleiro_oponente = faz_jogada(
        tabuleiro_oponente, linha, coluna
    )

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False

    else:
        # Jogada do oponente
        posicao_valida_oponente = False

        while not posicao_valida_oponente:
            linha_op = random.randint(0, 9)
            coluna_op = random.randint(0, 9)

            if [linha_op, coluna_op] in posicoes_ja_sorteadas:
                continue

            posicoes_ja_sorteadas.append([linha_op, coluna_op])
            posicao_valida_oponente = True

        print(
            f"Seu oponente está atacando na linha {linha_op} e coluna {coluna_op}"
        )

        tabuleiro_jogador = faz_jogada(
            tabuleiro_jogador, linha_op, coluna_op
        )

        if afundados(frota, tabuleiro_jogador) == total_navios_jogador:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False
def posiciona_frota(frota):
    tabuleiro = []

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro


def afundados(frota, tabuleiro):
    quantidade = 0

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            acertos = 0

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] == "X":
                    acertos += 1

            if acertos == len(navio):
                quantidade += 1

    return quantidade


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ""
    texto += "   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n"
    texto += "_______________________________      _______________________________\n"

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = "  ".join(
            [str(item) for item in tabuleiro_jogador[linha]]
        )
        oponente_info = "  ".join(
            [info if str(info) in "X-" else "0"
             for info in tabuleiro_oponente[linha]]
        )
        texto += f"{linha}| {jogador_info}|     {linha}| {oponente_info}|\n"

    return texto


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

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

total_navios = 0
for nome_navio in frota_oponente:
    total_navios += len(frota_oponente[nome_navio])

jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    posicao_inedita = False

    while not posicao_inedita:
        linha = int(input("Linha: "))

        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Linha: "))

        coluna = int(input("Coluna: "))

        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Coluna: "))

        if tabuleiro_oponente[linha][coluna] in ["X", "-"]:
            print(
                f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!"
            )
        else:
            posicao_inedita = True

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
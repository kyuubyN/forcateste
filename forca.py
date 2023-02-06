import random


# Inicia o jogo

def jogar():
    mostramsg()  # Mostra mensagem de abertura

    pasec = carrega_palavra_secreta()  # Palavra secreta

    letrasac = inicializa_letras(pasec)
    enforcou = False
    acertou = False
    errou = 0

    print(letrasac)
    # Enquanto não acertou e não enforcou
    dicas(pasec)
    while not enforcou and not acertou:  # Enquanto não fazer algo ele não para

        chute = chute_palavra()

        if chute in pasec:
            caso_acerte(chute, pasec, letrasac)
        else:
            errou += 1

        enforcou = errou == 7  # Vai mostrar quantas vzs voce pode fazer
        acertou = '_' not in letrasac
        print(letrasac)

        desenho(errou)

    if acertou:
        mensagem_vic(pasec)

    else:
        mensagem_der(pasec)

    # Mostra a mensagem de inicio


def mostramsg():
    return print('****************Bem Vindo ao Jogo******************')


# Carrega a pasta de palavras

def carrega_palavra_secreta():
    arquivo = open('palavras', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    pasec = palavras[numero].upper()
    return pasec


# Coloca as barrinhas

def inicializa_letras(palavra):
    return ['_' for letra in palavra]


# Mostra a palavra que você colocou

def chute_palavra():
    chute = input('Tente acertar! ').strip().upper()
    return chute


# Vai mostrar quantas palavras acertou

def caso_acerte(chute, pasec, letrasac):
    index = 0
    for letra in pasec:
        if chute == letra:
            letrasac[index] = letra  # Vai mostrar quantas palavras acertou no momento
        index = index + 1


# Vai mandar mensagem de vitoria

def mensagem_vic(pasec):
    print(f'Parabens você acertou!!!! A palavra é : {pasec}')
    print('\033[1;33;40m       ___________      \033[m')
    print("\033[1;33;40m      '._==_==_=_.'     \033[m")
    print("\033[1;33;40m      .-\\:      /-.    \033[m")
    print("\033[1;33;40m     | (|:.     |) |    \033[m")
    print("\033[1;33;40m      '-|:.     |-'     \033[m")
    print("\033[1;33;40m        \\::.    /      \033[m")
    print("\033[1;33;40m         '::. .'        \033[m")
    print("\033[1;33;40m           ) (          \033[m")
    print("\033[1;33;40m         _.' '._        \033[m")
    print("\033[1;33;40m        '-------'       \033[m")


# Vai mandar mensagem de derrota

def mensagem_der(pasec):
    print('Você Morreu!')
    print(f'A palavra era {pasec}')
    print("\033[1;37;40m    _______________         \033[m")
    print("\033[1;37;40m   /               \       \033[m")
    print("\033[1;37;40m  /                 \      \033[m")
    print("\033[1;37;40m//                   \/\  \033[m")
    print("\033[1;37;40m\|   XXXX     XXXX   | /   \033[m")
    print("\033[1;37;40m |   XXXX     XXXX   |/     \033[m")
    print("\033[1;37;40m |   XXX       XXX   |      \033[m")
    print("\033[1;37;40m |                   |      \033[m")
    print("\033[1;37;40m \__      XXX      __/     \033[m")
    print("\033[1;37;40m   |\     XXX     /|       \033[m")
    print("\033[1;37;40m   | |           | |        \033[m")
    print("\033[1;37;40m   | I I I I I I I |        \033[m")
    print("\033[1;37;40m   |  I I I I I I  |        \033[m")
    print("\033[1;37;40m   \_             _/       \033[m")
    print("\033[1;37;40m     \_         _/         \033[m")
    print("\033[1;37;40m       \_______/           \033[m")


# Vai mandar a dica

def dicas(pasec):
    if pasec == 'UVA':
        print('\033[1;31;40mA dica é:\033[m Tem cachos e geralmente são roxas! ')
    elif pasec == "MACA":
        print('\033[1;31;40mA dica é:\033[m Fruta consumida por Eva!')
    elif pasec == 'LARANJA':
        print('\033[1;31;40mA dica é:\033[m Fruta que tem o mesmo nome de uma cor!')
    elif pasec == 'LIMAO':
        print('\033[1;31;40mA dica é:\033[m Fruta azeda e verde!')


def desenho(errou):
    print("  _______     ")
    print(" |/      |    ")
    if (errou == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    if (errou == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
    if (errou == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
    if (errou == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    if (errou == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    if (errou == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    if (errou == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":  # Vai acabar com o codigo, ultima linha sempre
    jogar()

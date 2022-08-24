import random


def jogar():
    
    imprime_uma_mensagen()
    palavra_chave = escolhendo_a_palavra_secreta()

    letras_acertadas = inicializa_letra_acertada(palavra_chave)
    print(letras_acertadas)
    print()

    enforcou = False
    acertou = False
    erro = 0

    while not enforcou and not acertou:


        chute = pede_o_chute()

        if chute in palavra_chave:
            troca_o_pela_letra_certa(chute, letras_acertadas, palavra_chave)

        
        else:
            erro += 1
            print(f'OPs, Você errou faltam {7 - erro} tentativas')
            print()
            print("  _______     ")
            print(" |/      |    ")

            if erro == 1:
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if erro == 2:
                print(" |      (_)   ")
                print(" |      \     ")
                print(" |            ")
                print(" |            ")

            if erro == 3:
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")

            if erro == 4:
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")

            if erro == 5:
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if erro == 6:
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")

            if erro == 7:
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

            print(" |            ")
            print("_|___         ")
            print()

        enforcou = erro == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    else:
        print(f'Você perdeu a palavra chave era {palavra_chave}')
        print("Puxa, você foi enforcado!")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")



def imprime_uma_mensagen():
        print('*________________________________*')
        print('*___Bem vindo ao jogo da Forca___*')
        print('*________________________________*')
        print()

def escolhendo_a_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavra = []

    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavra))
    palavra_chave = palavra[numero].upper()
    return palavra_chave

def inicializa_letra_acertada(palavra):
    return ['_' for letra in palavra]

def pede_o_chute():
    chute = input('Qual a letra ? ')
    chute = chute.strip().upper()
    return chute

def troca_o_pela_letra_certa(chute, letras_acertadas, palavra_chave):
    index = 0
    for letra in palavra_chave:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra        
        index = index + 1
    

if __name__ == '__main__':
    jogar()
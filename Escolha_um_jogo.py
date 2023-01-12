import Adivinhacão
import Forca

def escolher_jogo():

    print('*________________________________*')
    print('*________Escolha um jogo________*')
    print('*________________________________*')
    print()

    print('(1) Adicinhação (2) Forca')

    jogo = int(input('Qual jogo você prefere: '))

    if jogo == 1:
        print('Jogando Adivinhação')
        Adivinhacão.jogar()

    else:
        print('Jogando Forca')
        Forca.jogar()

if __name__ == '__main__':
    escolher_jogo()


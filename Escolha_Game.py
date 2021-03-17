# Essa função escolhe o jogo selecionado pelo jogador

import Game_Adivinha as Ad
import Game_Forca as Fo


def escolhe_jogo():
    print('\n**********************************')
    print('******* Escolha seu Jogo! ********')
    print('**********************************', end='\n\n')

    print('''
    (1) -> Game_Forca
    (2) -> Game_Adivinha
    ''')
    jogo = int(input('Qual Jogo? '))

    if (jogo == 1):
        print('Carregando Game_Forca', end='\n')
        Fo.jogar_forca()
    elif (jogo == 2):
        print('Carregando Game_Adivinha', end='\n')
        Ad.jogar_adivinha()


if (__name__ == '__main__'):
    escolhe_jogo()

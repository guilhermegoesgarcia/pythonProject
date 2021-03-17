'''Nesse projeto vamos criar um jogo da Forca, para adivinhar palavras'''


def jogar_forca():
    print('\n**********************************')
    print('   Bem vindo ao Game da Forca !')
    print('**********************************', end='\n\n')

    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    palavra_secreta = 'banana'.upper()
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # enquanto não enforcou e não acertou__
    while (not enforcou and not acertou):

        chute = input('Qual letra?')

        # tratamento da entrada (retirada de espaços )
        chute = chute.strip().upper()

        if (chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('! PARABENS, VOCÊ ACERTOU A PALAVRA *_*  *_* !')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
    else:

        print('\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('X _________Suas tentativas acabaram_________X')
        print('X_______________GAME-OVER___________________X')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')

    print('\n\n************************')
    print("     FIM DE JOGO !!")
    print('************************')


if (__name__ == '__main__'):
    jogar_forca()

'''Nesse projeto vamos criar um jogo da Forca, para adivinhar palavras'''


def jogar_forca():
    print('\n**********************************')
    print('   Bem vindo ao Game da Forca !')
    print('**********************************', end='\n\n')

    palavra_secreta = 'python'
    enforcouo = False
    acertou = False

    # enquanto não enforcou e não acertou__
    while (not enforcouo and not acertou):

        chute = input('Qual letra?')

        # tratamento da entrada (retirada de espaços )
        chute = chute.strip()
        index = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print('Letra ({}) encontrada na posição ({})'.format(letra, index))
            index += 1
        print("Jogando..")

    print('************************')
    print("     FIM DE JOGO !!")
    print('************************')


if (__name__ == '__main__'):
    jogar_forca()

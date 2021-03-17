'''Nesse projeto vamos criar um jogo da Forca, para adivinhar palavras'''


def jogar_forca():
    print('\n**********************************')
    print('   Bem vindo ao Game da Forca !')
    print('**********************************', end='\n\n')

    palavra_secreta = 'banana'
    enforcouo = False
    acertou = False

    # enquanto não enforcou e não acertou__
    while (not enforcouo and not acertou):
        print("Jogando..")

    print('************************')
    print("     FIM DE JOGO !!")
    print('************************')


if (__name__ == '__main__'):
    jogar_forca()

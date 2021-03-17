'''Nesse projeto vamos criar um jogo da Forca, para adivinhar palavras'''
import random


def imprime_mensagem_abertura():
    print('\n**********************************')
    print('   Bem vindo ao Game da Forca !')
    print('**********************************', end='\n\n')


def carregando_palavra_secreta():
    arquivo = open("palavras.txt", 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    # posição da palavra no arquivo
    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista


def pede_chute():
    chute = input('Qual letra? ')

    # tratamento da entrada (retirada de espaços )
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('! PARABENS, VOCÊ ACERTOU A PALAVRA *_*  *_* !')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')


def imprime_mensagem_perdedor():
    print('\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print('X _________Suas tentativas acabaram_________X')
    print('X_______________GAME-OVER___________________X')
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')


def imprime_mensagem_final_de_jogo():
    print('\n\n************************')
    print("     FIM DE JOGO !!")
    print('************************')


def jogar_forca():
    imprime_mensagem_abertura()
    palavra_secreta = carregando_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    # enquanto não enforcou e não acertou__
    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros), end=('\n'))
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print('\n', letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()
    imprime_mensagem_final_de_jogo()


if (__name__ == '__main__'):
    jogar_forca()

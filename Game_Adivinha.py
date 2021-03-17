''' Nesse projeto vamos criar um jogo de adivinhação'''
# O jogador deve adivinhar um nomero secreto!

import random


def jogar_adivinha():
    print('\n**********************************')
    print('Bem vindo ao Game de Adivinhação!')
    print('**********************************', end='\n\n')

    # numero para ser descoberto
    numero_secreto = random.randrange(1, 101)
    # laço
    total_tentativas = 0
    # Pontos iniciados
    pontos = 1000

    print('Qual nivel de dificuldade?')
    print('''
    (1) -> Fácil
    (2) -> Médio
    (3 -> Difícil
    ''')

    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        chute = int(input('Digite o seu numero no console entre 1 e 100: '))
        print(f'Você digitou {chute}')

        if (chute < 1) or (chute > 100):
            print('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('! Você deve digitar um numero entre 1 e 100 !')
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n')
            continue

        # condiçoes
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print(f"Tentativa {rodada} de {total_tentativas}")
        if (acertou):
            print('\nVocê Acertou!! *_*\n')
            print('  VOCÊ FEZ >>> {}'.format(pontos))
            break
        else:
            if maior:
                print('\nVOCÊ ERROU ! =/ ')
                print('     O numero chutado foi MAIOR que o Numero Secreto \n')
            elif menor:
                print('\nVOCÊ ERROU ! =/ ')
                print('  O numero chutado foi MENOR que o Numero Secreto \n')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print('************************')
    print("     FIM DE JOGO !!")
    print('************************')

if (__name__ == '__main__'):
    jogar_adivinha()

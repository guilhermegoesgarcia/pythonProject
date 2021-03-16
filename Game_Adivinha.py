''' Nesse projeto vamos criar um jogo de adivinhação'''
# O jogador deve adivinhar um nomero secreto!
#

print('\n**********************************')
print('Bem vindo ao Game de Adivinhação!')
print('**********************************', end='\n\n')

# numero para ser descoberto
numero_secreto = 42

# laço
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    chute = int(input('Digite o seu numero no console: '))
    print(f'Você digitou {chute}')

    # condiçoes
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print(f"Tentativa {rodada} de {total_tentativas}")
    if (acertou):
        print('\nVocê Acertou!! *_*\n')
        rodada = total_tentativas
    else:
        if maior:
            print('\nVocê errou ! =/ ')
            print('     O numero chutado foi MAIOR que o Numero Secreto \n')
        elif menor:
            print('\nVocê errou ! =/ ')
            print('  O numero chutado foi MENOR que o Numero Secreto \n')

print('************************')
print("     FIM DE JOGO !!")
print('************************')

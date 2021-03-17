print('\n**********************************')
print('******* Escolha seu Jogo! ********')
print('**********************************', end='\n\n')

print('''
(1) -> Game_Forca
(2) -> Game_Adivinha
''')
jogo = input('Qual Jogo? ')

if (jogo == 1):
    print('Carregando Game_Forca', end='\n')
    jogar_forca()
elif (jogo == 2):
    print('Carregando Game_Adivinha', end='\n')
    jogar_adivinha()

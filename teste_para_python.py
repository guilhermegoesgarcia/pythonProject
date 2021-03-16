'''Desafio condiduo na seguinte página: https://github.com/idwall/python-test
Objetivo-> verificar se um determinado numero de cpf esta condido numa Blacklist.
'''

import pandas as pd


def limpa_cpf(cpf):
    novo_cpf = []

    b = ''

    # 'i itera no elemento interno da string'
    for i in cpf:
        if i == '.' or i == '-':
            continue
        else:
            b = b + i
    return b


def limpa_base_cpf(base):
    nova_base = []

    # ' row itera na linha ---DATAFRAME'
    for row in base.itertuples(index=False, name='CPF'):

        # 'i itera na tupla'
        for i in row:
            b = ''

            # 'ii itera no elemento interno da tupla'
            for ii in i:
                if ii == '.' or ii == '-':
                    continue
                else:
                    b = b + ii
            nova_base.append(b)
    return (nova_base)


def comparador_cpf(cpf, base):
    # 'limpar o cpf'
    if len(cpf) >= 11:
        cpf_limpo = limpa_cpf(cpf)
    else:
        cpf_limpo = cpf

    x = 0
    y = 0
    for i in base:
        if cpf_limpo == i:
            x = x + 1
            y = i
        else:
            continue
    if x == 0:
        print('CPF esta OK.. Sem restrições ')
    else:
        print(f'''Contem na Blacklist..

           {cpf_limpo} = {y} ''')


# importando base de dados
B_list = pd.read_csv('https://raw.githubusercontent.com/idwall/python-test/master/blacklist.txt')

base_nova = limpa_base_cpf(B_list)

print(base_nova)
print('')
cpf = str(input('''Entre com CPF: '''))
print()
comparador_cpf(cpf, base_nova)

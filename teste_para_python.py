'''Desafio condiduo na seguinte página: https://github.com/idwall/python-test
Objetivo-> verificar se um determinado numero de cpf esta condido numa Blacklist.
'''

import pandas as pd


def limpa_base_cpf(base):
    a = 0
    for i in base.itertuples():
        print(i)

    base_limpa = a
    return print(base_limpa)


B_list = pd.read_csv('https://raw.githubusercontent.com/idwall/python-test/master/blacklist.txt')

limpa_base_cpf(B_list)

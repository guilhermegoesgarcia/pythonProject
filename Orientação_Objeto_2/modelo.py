class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes


    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,novo_nome):
        self.__nome =novo_nome.title()



class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return f'{self._nome} - {self.ano} - Duração:{self.duracao}- LIKES:{self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada
    def __str__(self):
        return f'{self._nome} - {self.ano} - Temporada:{self.temporada}- LIKES:{self.likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas


    def __len__(self):
        return len(self._programas)


atlanta = Serie('Atlanta', 2018 , 2)
vingadores = Filme('vingadores-guerra infinita', 2018, 160)
tmep = Filme ('Todo mundo em panico', 1999, 100)
demolidor =  Filme('demolidor', 2016, 2)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

print()



filmes_e_series = [vingadores, atlanta, demolidor, tmep] #lista de filmes
playlist_fim_de_semana = Playlist ('fim de semana', filmes_e_series)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')
print()

for programa in playlist_fim_de_semana.listagem:
    print(programa)

print(f'''
Contem ou não contem? {demolidor in playlist_fim_de_semana}''')

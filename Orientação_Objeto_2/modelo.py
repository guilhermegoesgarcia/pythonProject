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
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        self._nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self._likes = 0




atlanta = Serie('Atlanta', 2018 , 2)
vingadores = Filme('vingadores-guerra infinita', 2018, 160)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

print()
print(f'Nome: {vingadores.nome} Ano: {vingadores.ano} Temporadas: {vingadores.duracao} Likes- {vingadores.likes}')
print(f'Nome: {atlanta.nome} Ano: {atlanta.ano} Temporadas: {atlanta.temporada} Likes- {atlanta.likes}')
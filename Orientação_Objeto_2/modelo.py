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



class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada




atlanta = Serie('Atlanta', 2018 , 2)
vingadores = Filme('vingadores-guerra infinita', 2018, 160)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

print()
print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} - {vingadores.likes}')
print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporada} - {atlanta.likes}')
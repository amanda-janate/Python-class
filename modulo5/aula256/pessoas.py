from contas import Conta


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self._nome = None
        self.idade = idade
        self._idade = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta: Conta | None = None
        # self.agencia = None

    # @property
    # def conta(self):
    #     return self._conta

    # @conta.setter
    # def conta(self, conta):
    #     self._conta = conta

    # @property
    # def agencia(self):
    #     return self._agencia

    # @agencia.setter
    # def agencia(self, agencia):
    #     self._agencia = agencia

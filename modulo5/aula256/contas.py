from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int):
        self.conta = conta
        self.agencia = agencia
        self.saldo = 0

    @abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def deposito(self, valor: float) -> float:
        self.saldo += valor
        # return f'Saldo atual: {self.saldo} (Valor depositado: {valor})'
        self.detalhes(f'(Valor depositado: {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'Saldo atual: {self.saldo:.2f} {msg}')
        print('--------')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name}{attrs}'


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, limite: float = 0):
        super().__init__(agencia, conta)
        self.limite = limite

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r},' \
            f'{self.limite!r}'
        return f'{class_name}{attrs}'

    def sacar(self, valor):
        if self.saldo - valor >= -self.limite:
            self.saldo -= valor
            # return f'Saldo atual: {self.saldo} (Valor sacado: {valor})'
            self.detalhes(f'(Valor sacado: {valor})')
            return self.saldo
        print('Não há saldo suficiente')
        print(f'Seu limite é {self.limite:.2f}')
        self.detalhes(f'(Saque negado: {valor})')
        return self.saldo


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
            # return f'Saldo atual: {self.saldo}(Valor sacado: {valor})'
            self.detalhes(f'(Valor sacado: {valor})')
            return self.saldo
        print('Não há saldo suficiente')
        self.detalhes(f'(Saque negado: {valor})')
        return self.saldo

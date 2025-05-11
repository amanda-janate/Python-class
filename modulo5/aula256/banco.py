import pessoas
import contas


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

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

    # @property
    # def cliente(self):
    #     return self._cliente

    # @cliente.setter
    # def cliente(self, cliente):
    #     self._cliente = cliente
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_conta_e_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autentica(self, cliente, conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and self._checa_conta(conta) and \
            self._checa_conta_e_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f'{class_name}{attrs}'

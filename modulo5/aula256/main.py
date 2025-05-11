"""Exercicio

Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

# from abc import ABC, abstractmethod
from contas import ContaCorrente, ContaPoupanca
from pessoas import Cliente
from banco import Banco


c1 = Cliente('Amanda', 27)
cc1 = ContaCorrente(123, 456, 100)
c1.conta = cc1

c2 = Cliente('Luiz', 30)
cp1 = ContaPoupanca(987, 654)
c2.conta = cp1

banco = Banco()
banco.clientes.extend([c1, c2])
banco.contas.extend([cc1, cp1])
banco.agencias.extend([123, 987])

print(banco.autentica(c1, cc1))
if banco.autentica(c1, cc1):
    cc1.deposito(100)

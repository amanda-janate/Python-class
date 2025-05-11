"""dataclasses

    Dataclasses sao decoradores para facilitar a criação de classes normais
"""
from dataclasses import dataclass, asdict, astuple, field


# @dataclass(frozen=True) -> nao permite alterar atributos
# @dataclass(Order=True) -> permite usar sorted
@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int = 0  # só pode passar valor padrao em valores imutaveis
    enderecos: list[str] = field(default_factory=list)  # assim da certo para
# valores mutaveis

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


p1 = Pessoa('Amanda', 'Silva')
# p2 = Pessoa('Henrique', 27)
# p1.nome_completo = 'Edson Henrique Picolo'
# print(p1)
# # print(p1 == p2)
# print(p1.nome_completo)
lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
ordenadas = sorted(lista, key=lambda p: p.nome)  # se o Order=False é necessari
# passar a key para que ele saiba como ordenar de acordo com o que eu quero
# da pra usar o reverse=True tambem
# print(ordenadas)
print(asdict(p1))
print(astuple(p1))

""" namedtuples

TUPLAS IMUTAVEIS
usar para criar classes sem metodos, para agrupamento de atributos
"""
# from collections import namedtuple

# Carta = namedtuple(
#     'Carta', ['valor', 'naipe'],
#     defaults=['VALOR', 'NAIPE']
# )
# as_espadas = Carta('A', 'espadas')
# print(as_espadas)
# print(as_espadas.valor)  # -> print(as_espadas[0])
# print(as_espadas.naipe)  # -> print(as_espadas[1])

# print(as_espadas._fields)
# print(as_espadas._field_defaults)

""" ------------------------- outra opção ------------------------- """

from typing import NamedTuple  # noqa


class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


as_espadas = Carta('A', 'espadas')
print(as_espadas)
print(as_espadas.valor)  # -> print(as_espadas[0])
print(as_espadas.naipe)  # -> print(as_espadas[1])

print(as_espadas._fields)
print(as_espadas._field_defaults)

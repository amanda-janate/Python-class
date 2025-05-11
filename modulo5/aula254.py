# Enum -> Enumerações 

import enum

# Direcoes = enum.Enum('Direcoes',['ESQUERDA', 'DIREITA'])
# Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA -> retornam Direcoes.ESQUERDA
# .name retorna o valor
# .value retorna a enumeracao

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção nao encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.DIREITA)
mover(Direcoes.ESQUERDA)


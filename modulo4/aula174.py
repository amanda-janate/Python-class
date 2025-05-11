# Combinação, permutação e produto
from itertools import combinations, permutations, product, groupby

def p_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'Joao', 'Joana', 'Luiz', 'Leticia'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masc', 'fem']
]

# p_iter(combinations(pessoas, 2)) #combina sem repetições
# p_iter(permutations(pessoas, 2)) #combina todas as possibilidades
# p_iter(product(*camisetas)) #produto cartesiano 

alunos = [
     {'nome': 'Luiz', 'nota': 'A'},
     {'nome': 'Letícia', 'nota': 'B'},
     {'nome': 'Fabrício', 'nota': 'A'},
     {'nome': 'Rosemary', 'nota': 'C'},
     {'nome': 'Joana', 'nota': 'D'},
     {'nome': 'João', 'nota': 'A'},
     {'nome': 'Eduardo', 'nota': 'B'},
     {'nome': 'André', 'nota': 'A'},
     {'nome': 'Anderson', 'nota': 'C'},
 ]

def ordena(aluno):
    return aluno['nota']

aulos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(aulos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno['nome'])
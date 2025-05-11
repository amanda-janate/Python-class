# função lambda - anonima com somente uma linha

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)
# lista.sort(key=lambda item: item['nome'])

# for item in lista:
#     print(item)

# def exibir(lista):
#     for item in lista:
#         print(item)
#     print()

# # sorted() gera copias rasas
# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])

# exibir(l1)
# exibir(l2)


def executa(funcao, *args):
    return funcao(*args)
def soma(x, y):
    return x + y

print(
    executa(
        lambda x, y: x + y,
        2, 3
    )
)
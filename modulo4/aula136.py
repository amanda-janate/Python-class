# list comprehension
lista = [numero * 2 for numero in range(10)]

# print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novo_produtos = [
    # produto['nome'] 
    # {**produto}
    # {**produto, 'preco': produto['preco'] * 1.05}
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] >= 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

print(*produtos, sep='\n')
print()
print(*novo_produtos, sep='\n')

lista = [n for n in range(10) if n < 5] #if a direita do for é filtro
# print(lista)

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
# print(lista)

# isinstance(valor_p_checar, classe_a_ser_checada)
# isinstance(5, int) # retorna true
# hasattr(valor, metodo) ou getattr(valor, metodo)
# valor = 'Amanda'
# metodo = 'upper1'

# if hasattr(valor, metodo):
#     print(getattr(valor, metodo)())
# else:
#     print('Metodo invalido')
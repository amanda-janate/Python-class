from functools import partial, reduce


produtos = [
     {'nome': 'Produto 5', 'preco': 10.00},
     {'nome': 'Produto 1', 'preco': 22.32},
     {'nome': 'Produto 3', 'preco': 10.11},
     {'nome': 'Produto 2', 'preco': 105.87},
     {'nome': 'Produto 4', 'preco': 69.90},
]

def raise_value(valor, porcentagem):
    return round(valor * porcentagem, 2)

def p_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

# partial faz automaticamente um decorator
raise_tenpercent = partial(
    raise_value,
    1.1
)

novos_produtos = [
    {**p, 'preco': raise_tenpercent(p['preco'])} for p in produtos 
]

def raise_product_value(produto):
    return {**produto, 'preco': raise_tenpercent(produto['preco'])} 

novos_produtos = map(
    raise_product_value,
    produtos
)

# p_iter(novos_produtos)

# FILTER
# novos_produtos2 = [
#     p for p in produtos
#     if p['preco'] > 10
# ]
# novos_produtos2 = filter(
#     lambda p: p['preco'] > 10,
#     produtos
# )
def price_filter(produto):
    return produto['preco'] > 10

novos_produtos2 = filter(
    price_filter,
    produtos
)

# p_iter(novos_produtos2)

# REDUCE
# total = 0 
# for p in produtos:
#     total += p['preco']
# print(total)

# print(
#     sum(p['preco'] for p in produtos)
# )
total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)
def reduce_function(total, product):
    return total + product['preco']

total = reduce(
    reduce_function,
    produtos,
    0
)

print(total)
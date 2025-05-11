# empacotamento e desempacotamento de dicionarios dict
pessoa = {
    'nome': 'Amanda',
    'sobrenome': 'Janate'
}

a, b = pessoa # retorna as chaves a=nome e b=sobrenome
a, b = pessoa.values() # retorna os valores a=Amanda e b=Janate
a, b = pessoa.items() # retorna tupla com a=('nome', 'Amanda') e b =('sobrenome', 'Janate')
(a1, a2), b = pessoa.items() # desempacota os valores da tupla a

# print(a1, a2, b)

dados_pessoa = {
    'idade': 28,
    'altura': 1.7
}

dados_completos = {**pessoa, **dados_pessoa, 'peso': 80} #combina todos os dicionarios

# print(dados_completos)

def args_nomeados(*args, **kwargs):
    print('nao nomeados: ',args)
    for chave, valor in kwargs.items():
        print(chave, valor)

# args_nomeados(456, nome='Amanda',qlq = 123)

args_nomeados(456, 1, **dados_completos)

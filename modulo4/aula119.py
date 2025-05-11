# tipo dict - dicionarios em py
# criados em par de chave e valor
# chaves podem ser os tipos imutaveis str, int, float, bool, tuple

pessoa = {
    'nome': 'Amanda',
    'sobrenome': 'Janate',
    'idade': 28,
    'altura': 1.7,
    'enderecos':[
        {'rua': 'rua x', 'numero': 123},
        {'rua': 'rua y', 'numero': 456}
    ]
}
pessoa['last_name'] = 'Silva' 
del pessoa['last_name']
print(pessoa['enderecos'][0 ])

# len(pessoa) -> qtde de chaves
# pessoa.keys() -> retorna todas as chaves
# pessoa.values() -> retorna todos os valores
# pessoa.items() -> retorna tuples com chave e valor
# for chave, valor in pessoa.items():
#     print(chave, valor)
# pessoa.setdefault('idade', 0) -> se não existir retorna um padrao definido
# nova_pessoa = pessoa.copy() faz a shallow copy (copia tudo que é valor imutavel)
# import copy
# nova_pessoa = copy.deepcopy(pessoa) -> faz o deep copy (copia todos os itens e listas dentro de listas etc)
# pessoa.get('nome', defaultvalue) -> retorna nome e se nao existir retorna valor default (por padrao é None)
# nome = pessoa.pop('nome') -> remove a chave mas retorna oque foi deletado
# ultima_chave = pessoa.popitem() -> remove a ultima chave mas retorna oque foi deletado
# pessoa.update({
#   'nome' = 'novo valor', -> atualiza dado existente
#   'peso' = 80 -> adiciona novo dado
# })
# pessoa.update(nome='novo valor', peso = 80)

# lista = [1, 'Amanda', False, 12.3]
# # string = 'Amanda'
# # lista = list(string)
# lista.insert(2, 'X')
# # lista[1] = 'X'
# print(lista)

# append, insert, pop, del, clear, extend
# del lista[2]
# lista.append('X') -> adiciona um item ao final da lista´
# lista.insert(2, 'X')
# lista.pop() -> remove o ultimo elemento da lista
# retorna o valor removido no momento, pode ser jogado numa variavel
# se passar valor no indice funciona
# lista.clear() -> limpa a lista
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# print(lista_c)
# lista_a.extend(lista_b)
# print(lista_a)

# lista_a.copy() -> serve para copiar valores de lista
# pois para tipos mutaveis o = aponta para o mesmo local de memoria

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

# for nome in lista:
#     # print(lista.index(nome), nome)
#     print(next(lista_enum))
# for item in enumerate(lista):
#     print(item)
# lista_enu = list(enumerate(lista))
# print(lista_enu)
for indice, nome in enumerate(lista):
    print(indice, nome)
# unpack
# nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
# nome1, *_ = ['Maria', 'Helena', 'Luiz'] retorna nome1 = 'Maria' e _ = ['Helena', 'Luiz']
# _, _, nome3, *_ = ['Maria', 'Helena', 'Luiz'] #retorna nome3 = 'Luiz'  e _ = [] 

# tuple é uma lista imutavel
# lista = ('Maria', 'Helena', 'Luiz') ou lista = 'Maria', 'Helena', 'Luiz'
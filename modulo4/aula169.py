# Exercício - Unir listas
 # Crie uma função zipper (como o zipper de roupas)
 # O trabalho dessa função será unir duas
 # listas na ordem.
 # Use todos os valores da menor lista.
 # Ex.:
 # ['Salvador', 'Ubatuba', 'Belo Horizonte']
 # ['BA', 'SP', 'MG', 'RJ']
 # Resultado
 # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
    # lista_unida = []
    # if len(lista1) <= len(lista2):
    #     tam = len(lista1)
    # else:
    #     tam = len(lista2)
    # for i in range(tam):
    #     tup = lista1[i], lista2[i]
    #     # print(tup)
    #     lista_unida.append(tup) 
    # return lista_unida
    tam = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(tam)
    ]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

new_list = zipper(lista1, lista2)

print(new_list)
print()

from itertools import zip_longest

print(list(zip_longest(lista1, lista2)))

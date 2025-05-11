# import aula154_mod
# # from aula154_mod import soma

# import importlib

# print(aula154_mod.soma(2, 4))
# # print(soma(2, 4))

# for i in range(10):
#     importlib.reload(aula154_mod) # recarregar modo se for necessario
#     print(i)

import pack1
# mesmo importando somente 0o packege eu tenho acesso a tudo de dentro do __init__.py
print(pack1.mult(2, 4))
# tenho acesso as variaveis e funçoes da aula154_mod porque importei ela no __init__.py
print(pack1.summ(2, 4)) 
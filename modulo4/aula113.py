# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
# import re

# var = input('Digite os numeros que deseja multiplicar: ')
# var = re.sub(
#     r'[^0-9]',
#     '',
#     var
# )
# var = list(var)
# # print(var)

# def mult(*args):
#     res = 1
#     for i in args:
#         i = int(i)
#         res *= i
#     return res

# # inp = (1, 2, 3, 4)
# mul = mult(*var)
# print(mul)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def imp_par(x):
    if x % 2 == 0:
        return 'Par'
    return 'Impar'

num = 8
calc = imp_par(num)
print(calc)

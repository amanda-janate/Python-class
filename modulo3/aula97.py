# operação ternária
# condicao = 10 != 10
# variavel = 'Valor' if condicao else 'Outro Valor'

# print(variavel)

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import random
import sys

# cpf = '746.824.890-70'
cpf = ''
for i in range(11):
    cpf += str(random.randint(0, 9)) 
cpf = cpf[:9] + '-' + cpf[9:]

# print(cpf)
# sys.exit()
cpf_editado = cpf.replace('.','').split('-')
# cpf_editado = re.sub(
#     r'[^0-9]',
#     '',
#     cpf
# )
# cpf_editado = cpf_editado
novo_cpf = list(cpf_editado)
calc1 = 0
# print(cpf_editado[0])
for i, j in enumerate(novo_cpf[0], -10):
    j = int(j)
    calc1 += (-i) * j 

calc1 = (calc1 * 10) % 11
calc1 = calc1 if calc1 <= 9 else 0
print(f'O primeiro digito é: {calc1}')

novo_cpf1 = novo_cpf[0] + str(calc1)
calc2 = 0
# print(novo_cpf1)

for i, j in enumerate(novo_cpf1, -11):
    j = int(j)
    calc2 += (-i) * j 

calc2 = (calc2 * 10) % 11
calc2 = calc2 if calc2 <= 9 else 0
print(f'O segundo digito é: {calc2}')

if calc1 == int(cpf_editado[1][0]) and calc2 == int(cpf_editado[1][1]):
    print(f'O cpf {cpf} é valido')
else:
    print(f'O cpf {cpf} não é valido')
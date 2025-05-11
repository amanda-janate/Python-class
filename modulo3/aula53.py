"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num = input('Digite um numero inteiro: ')
# try:
#     num_int = int(num)
#     if num_int%2 == 0:
#         print(f'O numero {num_int} é par')
#     else:
#         print(f'O numero {num_int} é impar')
# except:
#     print(f'O numero {num} não é inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input('Informe a hora: ')
# try:
#     hora_int = int(hora)
#     if hora_int >= 18 and hora_int <= 23:
#         print('Boa noite')
#     elif hora_int <= 11 and hora_int >= 0:
#         print('Bom dia')
#     elif hora_int >= 12 and hora_int <= 17:
#         print('Boa tarde')  
#     else:
#         print('Não conheço essa hora')        
# except:
#     print('Isto não é uma hora')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Informe seu primeiro nome: ')
if len(nome) >= 1:
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) > 6:
        print('Seu nome é longo')
    else:
        print('Seu nome é normal')
else:
    print('Digite pelo menos uma letra')
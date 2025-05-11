nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nome_inv = nome[::-1]
esp = ' ' in nome #não precisava ter criado variavel poderia ser direto no if
lent = len(nome)
pri = nome[:1] #poderia ser nome[0]
ult = nome[:-2:-1] #poderia ser nome[-1]
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_inv}')
    if esp:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {lent} letras')
    print(f'A primeira letra do seu nome é {pri}')
    print(f'A ultima letra do seu nome é {ult}')
else:
    print('Você deixou campos vazios')
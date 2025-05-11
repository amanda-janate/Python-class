# exercicio - sistema de perguntas e respostas
import re

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador_acertos = 0
num_perguntas = 0

for indice, valor in enumerate(perguntas):
    num_perguntas += 1
    print(f'Pergunta: {perguntas[indice]['Pergunta']}')
    print(f'\nOpções:')

    for i in perguntas[indice]['Opções']:
        print(f'{perguntas[indice]['Opções'].index(i)}) {i}')

    resp = input('Escolha uma opção: ')
    resp = re.sub(
        r'[^0-9]',
        '',
        resp
    )
    try:
        resp = int(resp)
        if resp == perguntas[indice]['Opções'].index(perguntas[indice]['Resposta']):
            print('Acertou')
            contador_acertos += 1
        else:
            print('Errou')
    except:
        print('Não é um numero')
    print('')
print(f'Você acertou {contador_acertos} de {num_perguntas} perguntas')


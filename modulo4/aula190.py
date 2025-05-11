# Criando arquivos com Python + Context Manager with
 # Usamos a função open para abrir
 # um arquivo em Python (ele pode ou não existir)
 # Modos:
 # r (leitura), w (escrita), x (para criação)
 # a (escreve ao final), b (binário)
 # t (modo texto), + (leitura e escrita)
 # Context manager - with (abre e fecha)
 # Métodos úteis
 # write, read (escrever e ler)
 # writelines (escrever várias linhas)
 # seek (move o cursor)
 # readline (ler linha)
 # readlines (ler linhas)
 # Vamos falar mais sobre o módulo os, mas:
 # os.remove ou unlink - apaga o arquivo
 # os.rename - troca o nome ou move o arquivo
 # Vamos falar mais sobre o módulo json, mas:
 # json.dump = Gera um arquivo json
 # json.load
import json 

# pessoa = {
#      'nome': 'Luiz Otávio 2',
#      'sobrenome': 'Miranda',
#      'enderecos': [
#          {'rua': 'R1', 'numero': 32},
#          {'rua': 'R2', 'numero': 55},
#      ],
#      'altura': 1.8,
#      'numeros_preferidos': (2, 4, 6, 8, 10),
#      'dev': True,
#      'nada': None,
# }

# with open('aula190.json', 'w+', encoding='UTF8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo,
#         indent=2
#     )

with open('aula190.json', 'r', encoding='UTF8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])
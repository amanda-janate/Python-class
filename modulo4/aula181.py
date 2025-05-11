# venv
# py -m venv venv
# pip freeze -> para ver oque tem instalado
# pip freeze > requirements.txt -> gera um arquivo com os dados do freeze
# pip intall -r requeriments.txt -> instala tudo do arquivo

# pip install pymysql / pip uninstall pymysql -y
# pip install pymysql --upgrade / # pip install pymysql=1.0.1

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

#se for criar em outra pasta precisa do caminho completo
# caminho = r'C:\Users\amand\Desktop\aula181.txt' 
import os

caminho = 'aula181.txt' #cria diretamente na pasta atual

# arquivo = open(caminho, 'w')

# arquivo.close()
# with open(caminho, 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     #quando acabar o arquivo será fechado automaticamente

# with open(caminho, 'r') as arquivo:
#     print(arquivo.read())

with open(caminho, 'w+', encoding='UTF8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

    arquivo.seek(0, 0)
    print(arquivo.read()) # le o arquivo todo

    arquivo.seek(0, 0)
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print()

    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

# modo w vai sempre apagar tudo que estava no arquivo e escreve
# modo a nao apaga nada, sempre começa da ultima linha do arquivo

# os.remove(caminho) #remove o arquivo
# os.rename(caminho, 'aula181_2.txt')


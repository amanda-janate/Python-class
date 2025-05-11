# modulo os
from itertools import count
import os

os.system('cls')
# os.system('echo "test"')

# print('a' * 80)
# print('a' * 80)
# print('a' * 80)
# print('a' * 80)

path = os.path.join('pasta1', 'pasta2', 'arquivo.txt')
# print(path)
caminho, arquivo = os.path.split(path)
path_archive, extension_archive = os.path.splitext(arquivo)

# print(caminho, arquivo)
# print(path_archive, extension_archive)
# print(os.path.exists(path))  # descobrir se caminho existe

# # print(os.path.abspath('.'))  # retorna o path atual
# print(os.path.basename(path))  # retorna a parte final do caminho
# print(os.path.dirname(path))  # retorna a o nome do diretorio

# C:\Users\amand\Documentos

# caminho = os.path.join('\\Users', 'amand', 'Documents')

# for pasta in os.listdir(caminho):
#     full = os.path.join(pasta, caminho)
#     if not os.path.isdir(full):
#         continue
#     print(pasta)
#     for item in os.listdir(full):
#         print('     ', item)

"""os.walk permite percorrer estrutura de diretorios
retorna sequencia de tuplas
"""

caminho = os.path.join('\\Users', 'amand', 'Documents')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_conter = next(counter)
    print(the_conter, root)

    for dir_ in dirs:
        print('    ', the_conter, dir_)

    for file_ in files:
        print('    ', the_conter, file_)

# os.unlink(caminho_completo_arquivo) -> para apagar arquivos

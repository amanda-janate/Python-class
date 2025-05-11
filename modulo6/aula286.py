""" Continuando os

Copiar arquivos

Apagar arquivos
os.unlink (arquivos)
shutil.rmtree (remove tudo recursivamente - pastas dentro de pastas etc)

Renomear
shutil.move ou os.rename
"""

import os
import shutil

HOME = os.path.expanduser('~')  # C:\Users\amand
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(HOME, 'Documents', 'SILVERHAWKS')
NOVA_PASTA = os.path.join(DESKTOP, 'TESTE_PYTHON')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

shutil.move(NOVA_PASTA, NOVA_PASTA + '_COPY')
# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dir, files in os.walk(PASTA_ORIGINAL):

#     for dir_ in dir:
#         diretorio_novo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA),
#             dir_
#         )
#         os.makedirs(diretorio_novo, exist_ok=True)

#     for file in files:
#         caminho_original = os.path.join(root, file)
#         caminho_novo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA),
#             file
#         )
#         shutil.copy(caminho_original, caminho_novo)
#         print(file)

""" Continuando modulo os """

import os
import math
from itertools import count


def size_format(bytes_size: int, base: int = 1024) -> str:
    """Formata um tamanho de arquivo para formato apropriado
    """
    if bytes_size <= 0:
        return '0B'
    sizes = "B", "KB", "MB", "GB", "TB", "PB"
    indice = int(math.log(bytes_size, base))

    pot = base ** indice
    final_size = round(bytes_size / pot, 2)
    abb = sizes[indice]
    return f'{final_size} {abb}'


caminho = os.path.join('\\Users', 'amand', 'Documents')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_conter = next(counter)
    print(the_conter, root)

    for dir_ in dirs:
        print('    ', the_conter, dir_)

    for file_ in files:
        full = os.path.join(root, file_)
        # size = size_format(os.path.getsize(full))
        stats = os.stat(full)
        size = size_format(stats.st_size)
        print('    ', the_conter, file_, size)

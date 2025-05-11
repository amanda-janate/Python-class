'''sys.argv
É uma lista de coisas que esta sendo passado no comando
ex: py aula306.py "listar" "mostrar"
é util para tomar descisoes no cod com if/ else etc

Argparse é um metodo mais robusto
'''

# import sys

# print(sys.argv)
# args = sys.argv
# qte_args = len(args)
# print(qte_args)

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra algo na tela',
    # type=str,
    metavar='STRING',
    # default='sem valor',
    required=True,
    # nargs='+' # recebe mais de um valor pro argumento
    action='append'  # recebe mais de uma vez o mesmo argumento
    )

parser.add_argument(
    '-v', '--verbose',
    help='exemplo',
    action='store_true'  # nao recebe argumentos, quando passado é um bool
    )
args = parser.parse_args()

print(args.basic)
if args.basic is None:
    print('Voce nao passou arg b')
else:
    print('O valor de b:', args.basic)

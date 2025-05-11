import locale
from datetime import datetime
import string
from pathlib import Path

PATH_FILE = Path(__file__).parent / 'aula298.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_brl(nro: float) -> str:
    brl = locale.currency(nro, grouping=True)
    return brl


data = datetime(2025, 4, 18)
dados = dict(
    nome='João',
    valor=converte_brl(1_234_567),
    data=data.strftime('%d/%m/%Y'),
    empresa='A. S.',
    # telefone='+55 (41) 9 9870-1346'
)

# texto = '''
# Prezado $nome,

# Informamos que sua mensalidade será cobrada no valor de $valor no dia $data.
# Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone
# $telefone.

# Atenciosamente,

# $empresa
# '''

with open(PATH_FILE, 'r', encoding='utf-8') as file:
    texto = file.read()
    template = string.Template(texto)
# print(template.substitute(dados))
    print(template.safe_substitute(dados))

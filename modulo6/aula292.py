# CSV
from pathlib import Path
import csv


CSV_PATH = Path(__file__).parent / 'aula292.csv'

# with open(CSV_PATH, 'r') as file:
#     leitor = csv.reader(file)
#     for linha in leitor:
#         print(linha)

# with open(CSV_PATH, 'r') as file:
#     leitor = csv.DictReader(file)
#     for linha in leitor:
#         print(linha)
#         print(linha['Nome'])

lista_clientes = [
    {'Nome': 'Amanda', 'Endereco': 'Rua do Tijuco 391'},
    {'Nome': 'Edson', 'Endereco': 'Rua do paraiso 500'},
    {'Nome': 'Valdenice', 'Endereco': 'Rua Cascavel 2971'}
]

# with open(CSV_PATH, 'w') as file:
#     header = lista_clientes[0].keys()
#     escritor = csv.writer(file)
#     escritor.writerow(header)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())

with open(CSV_PATH, 'w') as file:
    header = lista_clientes[0].keys()
    escritor = csv.DictWriter(file, fieldnames=header)
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)

'''Modulo Random'''

import random

# gerar nro inteiro dentro de um intervalo que pode conter um passo
r_range = random.randrange(10, 20, 2)
# print(r_range)

# gerar nro inteiro dentro de um intervalo sem um passo
r_int = random.randint(10, 20)
# print(r_int)

# gerar nro flutuante dentro de um intervalo sem um passo
r_uniform = random.uniform(10, 20)
# print(r_uniform)

# embaralhar a lista original -> altera a lista original CUIDADO
nomes = ['Luiz', 'Maria', 'Helena', 'Edson']
random.shuffle(nomes)
# print(nomes)

# escolher elementos do iteravel e retorna outro que nao se repete
novos_nomes = random.sample(nomes, k=2)
# print(novos_nomes)

# escolher elementos do iteravel e retorna outro que pode se repetir
novos_nomes = random.choices(nomes, k=2)
# print(novos_nomes)

# escolhe um elemento do iteravel
# util para sorteios
print(random.choice(nomes))

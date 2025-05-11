'''Modulo secret
Opção segura pra trabalhar com criptografia e senhas
'''
import secrets
import string as s
from secrets import SystemRandom as Sr

# gerando senha aleatoria
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))
'''Rodar diretamente no terminal:
py -c "import string as s;from secrets import SystemRandom as Sr;
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))"
'''

random = secrets.SystemRandom()  # permite trabalhar com aleatoriedade real

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
# print(random.choice(nomes))

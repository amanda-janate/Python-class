# exercicio classe com JSON
import json

class Pessoa:
    def __init__(self, name, lastname, idade):
        self.name = name
        self.lastname = lastname
        self.idade = idade

p1 = Pessoa('Amanda', 'Silva', 28)
p2 = Pessoa('Edson', 'Rodrigues', 34)

# print(vars(p1))
# print(vars(p2))
load_archive = [vars(p1), vars(p2)]
# print(load_archive)
def fazer_dump():
    with open('aula206.json', 'w', encoding='utf8') as arquivo:
        json.dump(
            load_archive,
            arquivo,
            indent=2
        )
if __name__ == '__main__': # pra impedir a execução no import
    fazer_dump()
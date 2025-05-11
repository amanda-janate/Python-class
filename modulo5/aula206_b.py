import json
from aula206 import Pessoa
# class Pessoa:
#     def __init__(self, name, lastname, idade):
#         self.name = name
#         self.lastname = lastname
#         self.idade = idade


with open('aula206.json', 'r', encoding='utf8') as arquivo:
    pessoa_json = json.load(arquivo)
    
# for i, pessoa in enumerate(pessoa_json):
# print(*pessoa_json)
# p1 = Pessoa(pessoa_json[0]['name'], pessoa_json[0]['lastname'], pessoa_json[0]['idade'])
# p2 = Pessoa(pessoa_json[1]['name'], pessoa_json[1]['lastname'], pessoa_json[1]['idade'])
p1 = Pessoa(**pessoa_json[0])
p2 = Pessoa(**pessoa_json[1])


print(vars(p1))
print(vars(p2))

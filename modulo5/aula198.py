# class 
# as classes geram novos objetos (instancias) 
# podem ter seus proprios atributos e metodos 
# por convenção usar PascalCase para nomes de classes

class Pessoa:
    def __init__(self, nome, sobrenome): # o self é passado automaticamente pelo python
        # criar e inicializar atributos:
        self.nome = nome 
        self.sobrenome = sobrenome

p1 = Pessoa('Amanda', 'Janate') # aqui o self é p1
# p1.nome = 'Amanda'
# p1.sobrenome = 'Janate'

p2 = Pessoa('Edson', 'Henrique')
# p2.nome = 'Edson'
# p2.sobrenome = 'Henrique'

print(p1.nome)
print(p1.sobrenome)
print()
print(p2.nome)
print(p2.sobrenome)
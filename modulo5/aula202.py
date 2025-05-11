# Escopo da classe e de metodos da classe
class Animal:
    def __init__(self, nome):
        self.nome = nome

        var = 'executa qndo a classe é instanciada'
        print(var)
    
    def comendo(self, alimento):
        return f'O {self.nome} esta comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal('Leão')

print(leao.nome)
print(leao.executar('carne'))


# Atributos de classes
print('*'* 100)
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_birth_year(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Amanda', 28)

# Pessoa.ano_atual = 2026 # altera o atributo da classe

print(Pessoa.ano_atual)
print(p1.get_birth_year())
# print(p1.__dict__)
p1.__dict__['nome'] = 'Joao'
p1.__dict__['teste'] = 'testando'
del p1.__dict__['teste']
print(vars(p1))
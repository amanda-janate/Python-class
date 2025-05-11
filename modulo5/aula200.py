#  Métodos em instancias de classes
# atributos sao "qualidades" e métodos são "ações"
class Carro:
    def __init__(self, nome='Sem nome'): # nome é atributo
        self.nome = nome
    
    def acelerar(self): #metodo
        print(f'{self.nome} esta acelerando')

# fusca e celta são instancias 
fusca = Carro('Fusca') 
celta = Carro(nome='Celta')

print(fusca.nome)
fusca.acelerar()
print()
print(celta.nome)
celta.acelerar()
# Carro.acelerar(celta)

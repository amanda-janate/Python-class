# Herança

# Herança simples
class Pessoa: # Parent class
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class Cliente(Pessoa): #Child class
    ...


c1 = Cliente('Amanda', 'Janate')

'''sobreposição de classe e super()'''
class Mystring(str):
    def upper(self):
        print('Chamou Upper') # aqui adiciono algo necessario ao upper
        return super().upper() #aqui retorno o upper original da classe str
    # super(class atual, self) -> super(Mystring, self) retorna str

string = Mystring('amanda')
# print(string.upper())

# Herança multipla
# class pessoa:
#   ...
# class Filelog:
#   ...
# class Cliente(Pessoa, Filelog)

# problema do diamante
#      A
#     / \
#    B   C
#     \ /
#      D

class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    # def quem_sou(self):
    #     print('B')

class C(A):
    ...

    def quem_sou(self):
        print('C')

class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')


d = D()
d.quem_sou()

# identificar mro (method read order)
# print(D.mro())
# ou D.__mro__


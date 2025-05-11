# funções decoradoras e decoradores com classes
# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name}({class_dict})'
#         return class_repr

def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls

def my_planet(metodo):
    def intern(self, *args, **kwargs):
        res = metodo(self, *args, **kwargs)
        if 'Terra' in res:
            return 'Voce esta em casa'
        return res
    return intern

@add_repr
class Time():
    def __init__(self, nome):
        self.nome = nome

@add_repr
class Planeta():
    def __init__(self, nome):
        self.nome = nome

    @my_planet
    def falar_nome(self):
        return f'O nome do planeta é {self.nome}'

# Time = add_repr(Time)
# Planeta = add_repr(Planeta)

brasil = Time('Brasil')
china = Time('China')

terra = Planeta('Terra')
marte = Planeta('Marte')

# print(brasil)
# print(china)
# print(terra)
# print(marte)

print(terra.falar_nome())
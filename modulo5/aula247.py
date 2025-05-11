# Metaclasses
def my_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('META NEW')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = my_repr

        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')

        return cls

    def __call__(cls, *args, **kwargs):
        inst = super().__call__(*args, **kwargs)
        
        if 'nome' not in inst.__dict__:
            raise NotImplementedError('Implemente o nome')
        
        return inst

class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('PESSOA NEW')
        inst = super().__new__(cls)
        return inst
    
    def __init__(self, nome):
        print('PESSOA INIT')
        self.nome = nome
    
    def falar(self):
        print('oi')

p1 = Pessoa('Amanda')
print(p1.attr)
print(p1)
p1.falar()
from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.methodname = name
    
    @property
    def methodname(self):
        return self._name
    
    @methodname.setter
    @abstractmethod
    def methodname(self, name):
        ...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # aqui é um codigo inutil pois nao faz nada
    
    @AbstractFoo.methodname.setter
    def methodname(self, name):
        self._name = name

foo = Foo('Bar')

print(foo.methodname)

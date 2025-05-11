# __new__ e __init__
#  new cria e retorna novo objeto, nao recebe self, recebe apenas cls

#  __new__ nao é normalmente utilizado, geralmente só em casos de muita complexidade

class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a instancia')
        inst = super().__new__(cls)
        print('Depois de criar a instancia')
        return inst
    
    def __init__(self, x):
        self.x = x
        print('Sou o init')
    
    def __repr__(self):
        return 'A()'

# a = A(1)
# print(a)

# context manager
# __enter__ e __exit__

# with open('aula239.txt', 'w') as arquivo:
#     ...

class MyContextManeger:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self._arquivo = None
    
    def __enter__(self):
        self._arquivo = open(self.path, self.mode, encoding='UTF-8')
        return self._arquivo

    def __exit__(self, cls_exception, exception_, traceback_):
        self._arquivo.close()
        # print(cls_exception)
        # print(exception_)
        # print(traceback_)
        # return True


with MyContextManeger(r'C:\Users\amand\Desktop\estudo_python\modulo3\aula239.txt', 'a') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.write('Linha 4\n')

    # print('with', arquivo)

# context manager com função 
from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    try:
        arquivo = open(path, mode, encoding='UTF-8')
        yield arquivo
    finally:
        arquivo.close()

with my_open(r'C:\Users\amand\Desktop\estudo_python\modulo3\aula242.txt', 'a') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    arquivo.write('Linha 4\n')
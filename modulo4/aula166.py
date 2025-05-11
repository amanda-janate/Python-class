# decorador - syntax sugar

# isso é uma função decoradora
def criar_funcao(func):
    def interna(*args,**kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args,**kwargs)
        return resultado
    return interna

@criar_funcao #isso é um decorador
def inverte_string(string):
    return string[::-1]

def is_string(string):
    if not isinstance(string, str):
        raise TypeError(f'{string} não é uma string.')

# invertido_validado = criar_funcao(inverte_string)
# invertido = invertido_validado(123)
# invertido = inverte_string(123)
# print(invertido)

def decorator_factory(a=None, b=None, c=None):
    def function_factory(func):
        def inner(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, (float, int)):
                    raise TypeError('Somente numeros sao aceitos.')
            res = func(*args, **kwargs)
            return res
        return inner
    return function_factory

@decorator_factory(1, 2, 3)
def summ(x, y):
    return x + y

result = summ(1, '2')
print(result)
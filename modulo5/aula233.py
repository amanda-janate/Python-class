# Criando próprias exceções 

class MyError(Exception):
    ...

class AnotherError(Exception):
    ...

def raise_exp():
    expt = MyError('A msg do erro', 'teste1', 'test2')
    expt.add_note('Isso aqui esta errado')
    raise expt

try:
    raise_exp()
except MyError as error:
    print(error.__class__.__name__)
    print(error)
    # raise # relança a exception após fazer alguma coisa
    expt = MyError('Relançando outro erro')
    expt.__notes__ = error.__notes__.copy()
    raise expt from error
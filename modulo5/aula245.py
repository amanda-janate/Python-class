#  Metodo __call__
# torna a instancia da classe callable

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        return f'{nome} está chamando {self.phone}'

call1 = CallMe('98701346')
res = call1('Amanda')
print(res)

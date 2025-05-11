# classes decoradoras
# class Multiplicar:
#     def __init__(self, func):
#         self.func = func
#         self._key = 10
    
#     def __call__(self, *args, **kwargs):
#         res = self.func(*args, **kwargs)
#         return res * self._key

# @Multiplicar
# def soma(x, y):
#     return x + y

# foo = soma(2, 4)
# print(foo)

class Multiplicar:
    def __init__(self, mult):
        self._key = mult
    
    def __call__(self, func):
        def intern(*args, **kwargs):
            res = func(*args, **kwargs)
            return res * self._key
        return intern

@Multiplicar(4)
def soma(x, y):
    return x + y

foo = soma(2, 4)
print(foo)
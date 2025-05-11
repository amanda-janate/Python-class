# generator expression
import sys

lista = [n for n in range(10000)]
generator = (n for n in range(10000)) 
# sys.getsizeof() recupera o tamanho ocupado na memoria 

# print(sys.getsizeof(lista)) 
# print(sys.getsizeof(generator))

# for i in generator:
#     print(i)
# o generator serve para navegar sequencialmente
# não da pra navegar nos indices pois nao esta salvo na memoria

def generator(n=0, maxi=10):
    # yield 1 #pausa a função aqui
    # yield 2
    # return 'ACABOU' #retorna uma exceção com o valor descrito
    # while True:
    #     yield n 
    #     n += 1

    #     if n > maxi:
    #         return
    ran = range(n, maxi+1)
    for i in ran:
        yield i
    return

gen = generator()
# print(next(gen))
# print(next(gen))

# for n in gen:
#     print(n)

def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen=None):
    if gen is not None:
        yield from gen()
    yield 5
    yield 6
    yield 7

gen = gen2(gen1)

for i in gen:
    print(i)

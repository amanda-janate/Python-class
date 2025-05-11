# def funcao(a = 'Sem', b= None):
#     print(a)
#     print(b)

# funcao(b=1, a=2)
# funcao()
"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
# x = 1

# def escopo():
#     global x
#     x = 10

#     def outra_funcao():
#         global x
#         x = 11
#         y = 2
#         print(x, y)
#     print(x)
#     outra_funcao()

# print(x)
# escopo()
# print(x)

# def soma(x, y):
#     if x > 10:
#         return 10 , 20
#     return x + y

# soma1 = soma(2, 2)
# soma2 = soma(11, 3)
# # soma3 = soma(soma1, soma2)
# # print(soma3)
# print(soma1)
# print(soma2)

# passa argumentos "ilimitados" definidos na chamada da função e cria uma tupla
# o * empacota ou desempacota dados
# def soma(*args): 
#     x = 0
#     for i in args:
#         x += i
#     return x 

# numeros = 1, 2, 3, 4
# soma1 = soma(*numeros) #aqui ele vai desempacotar para poder empacotar na função
# print(soma1)

# sum() aceita apenas iteraveis -> sum(numeros) funciona mas sum(*numeros) não
# print(sum(numeros))


# (/) só permite argumentos posicionais antes da barra
# (*) só permite argumentos nomeados depois do asterisco
def soma(a, b, /, *, c):
    return (a + b + c)

print(soma(1, 2, c=3))
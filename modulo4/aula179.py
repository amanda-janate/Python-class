# funcoes recursivas
# sao funcoes que podem se chamar de volta 

# exemplo contar até 10

# def recursive(init=0,end=10):
#     print(init)
#     if init >= end:
#         return end
#     init += 1
#     return recursive(init, end)

# print(recursive())

# fatorial n!
# count = 1
# def factorial(n=5):
#     global count 
#     if n == 0:
#         return count
#     count *= n 
#     n -= 1
#     return factorial(n)

def factorial(n=5):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial())
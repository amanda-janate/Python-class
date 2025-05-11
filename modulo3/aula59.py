# = += -= *= /= //= **= %=

# num = 0

# while num < 11:
#     num += 1
#     if num == 6:
#         continue
#     print(num)

# print('Acabou')

# nome = 'Amanda Janate'
# tam = len(nome)
# num = 0
# new_name = ''
# while num < tam:
#     # print(nome[num])
#     new_name += '*' + nome[num]
#     num += 1
# print(new_name)

name = 'Amanda Janate'
new_name = ''
for letter in name:
    # new_name += '*' + letter 
    new_name += f'*{letter}'
print(new_name) 

#range(start, stop, step)

num = range(1, 10)

for number in num:
    print(number)
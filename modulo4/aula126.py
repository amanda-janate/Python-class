# sets - conjuntos em python (tipo set)
# sets são mutaveis, porem aceitam apenas tipos imutaveis na sua estrutura
# valores sempre unicos (eliminam valores duplicados automaticamente)
# nao garantem a ordem
# nao tem indexes

# s1 = {1, 2, 3}
# s1 = set() # para criar um set vazio s2 = {} cria um dicionario (dict)
# s1.add('Amanda')
# s1.update(('Olá Mundo', 1))
# # s1.clear() 
# s1.discard('Olá Mundo')

# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 #uniao
s3 = s1 & s2 #itens presentes em ambos
s3 = s1 - s2 #itens presentes apenas no set da esquerda
s3 = s1 ^ s2 #itens que nao estao em ambos

print(s3)
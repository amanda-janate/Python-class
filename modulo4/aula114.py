# def saudacao(msg):
#     return msg

# def executa(funcao, msg):
#     return funcao(msg)

# v = executa(saudacao, 'Bom dia')
# print(v)

#  Crie funcoes que duplicam, triplicam e quadruplicam
# o numero recebido como parametro

def funcao(op):
    def mult(num):
        return num * op
    return mult

duplicar = funcao(2)
triplicar = funcao(3)
quadruplicar = funcao(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
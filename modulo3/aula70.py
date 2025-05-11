string = 'O Python é uma linguagem de programação multiparadigma.'\
        'Python foi criado por Guido van Rossum'.lower()

i = 0 
qtde = 0
letra = ''

while i < len(string):
    letra_atual = string[i]
    qtde_atual = string.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue
    
    if qtde_atual > qtde:
        qtde = qtde_atual
        letra = letra_atual
    i += 1
else:
    print(letra, qtde)


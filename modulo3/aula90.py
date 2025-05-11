'''
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indices inexistentes na lista
'''
lista = []
while True:
    entrada = input(f'Selecione uma opção \n [i]nserir [a]pagar [l]istar: ').lower()
    if entrada == 'i':
        novo_item = input('Valor: ')
        lista.append(novo_item)
    elif entrada == 'a':
        remover = input('Indice: ')
        try:
            remover = int(remover)
            del lista[remover]
        except:
            print('Não foi possivel apagar esse indice')
    elif entrada == 'l':
        if lista == []:
                print('Não tem nada')
        else:
            for i in lista:
                print(lista.index(i), i)
    else:
        print('Selecione uma opção valida')


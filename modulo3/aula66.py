# calculadora com while
while True:
    num1 = input('Digite o primeiro numero: ')
    num2 = input('Digite o segundo numero: ')
    op = input('Digite o operador: ')
    num1_float = 0
    num2_float = 0
    valid = None
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        valid = True
    except:  
        valid = None  
    if valid is None:    
        print('Um ou ambos numeros digitados sao invalidos')
        continue
    if op not in '+-/*':
        print('Operador invalido')
        continue
    if len(op) > 1:
        print('Digite somente um operador')
        continue
    print('Resultado:')
    if op == '+':
        print(num1_float + num2_float)
    elif op == '-':
        print(num1_float - num2_float)
    elif op == '/':
        print(num1_float / num2_float)
    elif op == '*':
        print(num1_float * num2_float)
    else:
        print('Deu ruim')
    exit = input('Voce deseja sair? [s]im: ').lower().startswith('s')
    if exit:
        break
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

secret = 'tabaco'
chave = '******'
tentativas = 0
acerto = ''
# new_chave = ''
while True:
    tent = input('Digite uma letra: ' )
    tentativas += 1
    if len(tent) > 1:
        print('Digite só uma letra')
        continue

    if tent in secret:
        acerto += tent
    
    palavra = ''
    for sec in secret:
        if sec in acerto:
            palavra += sec
        else:
            palavra += '*'
    
    print(f'Palavra: {palavra}')
    
    if palavra == secret:
        os.system('cls')
        print('Você acertou')
        print(f'A palavra secreta é {palavra}')
        print(f'Tentativas {tentativas}')
        tentativas = 0




# string = 'Amanda'
# new = 'x'
# test = string.replace(string[2], new)
# print(test)
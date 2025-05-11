velocidade = 61
local_carro = 99

RADAR = 60
LOCAL = 100
RANGE = 1

# if (local_carro == (LOCAL - RANGE) or local_carro == (LOCAL + RANGE) or local_carro == LOCAL):
#     if velocidade > RADAR:
#         print('Multa')
#     else:
#         print('Sem multa')
if (local_carro >= (LOCAL - RANGE) and local_carro <= (LOCAL + RANGE)):
    if velocidade > RADAR:
        print('Multa')
    else:
        print('Sem multa')
else:
    print('Não esta no radar')
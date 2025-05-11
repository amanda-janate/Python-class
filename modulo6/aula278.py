""" Exercicio """
from datetime import datetime  # timedelta
from dateutil.relativedelta import relativedelta


total = 1_000_000
init = datetime.strptime('20/12/2022', '%d/%m/%Y')
delta = relativedelta(years=5)
end = init + delta

# print(init)
# print(end)
data_parcelas = []
var = init

while var < end:
    data_parcelas.append(var)
    var += relativedelta(months=+1)

num_parcelas = len(data_parcelas)
valor_parcela = total / num_parcelas

for data in data_parcelas:
    print(f'{data.strftime('%d/%m/%Y')} R$ {valor_parcela:,.2f}')

print()
print(
    f'Valor total R${total:,.2f}, com prazo de {delta.years} anos '
    f'({num_parcelas} meses) em parcelas de R${valor_parcela:,.2f}'
)

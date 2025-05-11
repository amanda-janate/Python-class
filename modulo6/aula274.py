"""
Datas

modulo datetime
datetime(ano, mes, dia, hora, minuto, segundo)

https://docs.python.org/3/library/datetime.html
"""

from datetime import datetime, timedelta
from pytz import timezone
from dateutil.relativedelta import relativedelta

data1 = datetime(2025, 4, 9)  # 2025-04-09 00:00:00
data2 = datetime(2025, 4, 9, 17, 58)  # 2025-04-09 17:58:00
data_str = '2025-04-09 17:58:23'

data_str1 = datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')
# 2025-04-09 17:58:23
data_str2 = datetime.strptime('09/04/2025', '%d/%m/%Y')
# 2025-04-09 00:00:00

# print(data1)
# print(data2)
# print(data_str2)

# data_atual = datetime.now()  # pega a hora atual
data_atual = datetime.now(timezone('UTC'))  # tmz convertido
# 1744234840.43277

# print(data_atual)
# print(data_atual.timestamp())  # recupera Unix timestamp
# print(datetime.fromtimestamp(1744234840.43277))

fmt = '%d/%m/%Y %H:%M:%S'
init = datetime.strptime('20/04/1987 09:30:30', fmt)
end = datetime.strptime('12/12/2022 08:20:20', fmt)
delta = end - init
# print(delta)  # retorna time delta 13019 days, 22:49:50
# print(delta.total_seconds())  # retorna total de segundos de diferença
new_delta = timedelta(days=10)
# print(end + new_delta)

# print(end + relativedelta(seconds=30, minutes=10))
dif = relativedelta(end, init)
# print(dif)
# print(dif.years)
# print(dif.days)

""" Formatação de datas """
init_br = datetime.strftime(end, '%d/%m/%Y')  # resulta numa string
print('Original: ', init)
print('Formatado: ', init_br)

# desta forma retona inteiro partes da data
print(end.day)
print(end.month)
print(end.year)

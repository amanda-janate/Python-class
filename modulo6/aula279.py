""" Calendar """

import calendar

# print(calendar.calendar(2025))
# print(calendar.month(2025, 4))

# recuperar primeiro e ultimo dia de um mes
# print(calendar.monthrange(2025, 4))
# retorna primeiro dia (dayweek) e o ultimo dia int
primeiro, ultimo = calendar.monthrange(2025, 4)

# recupera o dia da semana do ultimo dia do mes
# print(calendar.day_name[calendar.weekday(2025, 4, ultimo)])

for week in calendar.monthcalendar(2025, 4):
    for day in week:
        if day == 0:
            continue
        print(day)

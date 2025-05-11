# internacionalização

import locale
import calendar

locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
# locale.getlocale()  # para saber o locale

print(calendar.calendar(2025))

locales = locale.locale_alias

# Exibe os locales
for loc in sorted(locales):
    print(f"{loc}: {locales[loc]}")

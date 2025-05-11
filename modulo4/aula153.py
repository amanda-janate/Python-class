# importe de modulos python
# importar modulo inteiro
import sys

print(sys.platform)
# nomear um modulo
import sys as s

print(s.platform)


# importar partes do modulo
from sys import platform, exit

print(platform)
# nomear um objeto
from sys import platform as pf, exit as ex

print(pf)

# má pratica
from sys import *

print(platform)



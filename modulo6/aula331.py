'''Deque - LIFO e FIFO
deque - double end queue
basicamente deque é uma lista facil de mexer na esquerda
'''
from collections import deque

fila: deque[int] = deque()
fila.append(3)
fila.append(2)
fila.append(1)
fila.appendleft(4)
fila.appendleft(5)
fila.appendleft(6)
print(fila)
fila.pop()
fila.popleft()
print(fila)

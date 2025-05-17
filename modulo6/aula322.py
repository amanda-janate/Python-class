'''Executando threads paralelas'''
from time import sleep
from threading import Thread, Lock

# class MyThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)

# t1 = MyThread('Thread 1', 5)
# t1.start()

# for i in range(10):
#     print(i)
#     sleep(1)

# def waiting(text, time):
#     sleep(time)
#     print(text)

# t = Thread(target=waiting, args=('Hello World!', 5))
# t.start()

# while t.is_alive():
#     print('esperando a thread')
#     sleep(2)

# print('Thread acabou')

class Ticket:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, qty):
        self.lock.acquire()

        if self.estoque < qty:
            print('Sem ingressos suficiente')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= qty
        print(f'Voce comprou {qty} ingresso(s).'
              f'Ainda temos {self.estoque} em estoque')

        self.lock.release()

if __name__ == '__main__':
    ingressos = Ticket(10)

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)

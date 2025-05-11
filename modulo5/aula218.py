class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    def listar(self):
        print(self.nome, self._fabricante, self._motor)

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

opala6 = Carro('Opala')
caneco6 = Motor('6 cilindros')
gm = Fabricante('General Motors')

opala6.motor = caneco6.nome
opala6.fabricante = gm.nome

opala6.listar()

opala4 = Carro('Opala')
caneco4 = Motor('4 cilindros')
opala4.motor = caneco4.nome
opala4.fabricante = gm.nome

opala4.listar()
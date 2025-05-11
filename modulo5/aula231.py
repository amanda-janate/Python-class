# Polimorfismo
# Permite que classes derivadas de uma mesma superclasse 
# tenham um mesmo methodo, com a mesma assinatura, 
# mas com comportamentos diferentes
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.msg)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.msg)
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificacao enviada')
    else:
        print('Notificacao não enviada')

email = NotificacaoEmail('testando email')
notificar(email)

sms = NotificacaoSMS('testando sms')
notificar(sms)
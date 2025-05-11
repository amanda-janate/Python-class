# O metodo abstrato precisa ser implementado nas classes filhas 
# Na definição da subclasse a assinatura do metodo abstrato deve ser mantido 
from abc import ABC, ABCMeta, abstractmethod

class Log(ABC):
# class Log(metaclass=ABCMeta):
    @abstractmethod
    def _log(self, msg):...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

# l = Log() # Gera um erro
l= LogPrintMixin()
l.log_error('Teste')
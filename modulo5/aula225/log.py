# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        format_msg = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a', encoding='UTF-8') as arquivo:
            arquivo.write(format_msg)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('qualquer coisa')
    l.log_success('Deu boa')
    # print(LOG_FILE)

    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Deu boa')
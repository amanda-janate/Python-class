from log import LogFileMixin, LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome 
        self._poweron = False

    def poweron(self):
        if not self._poweron:
            self._poweron = True
    
    def poweroff(self):
        if self._poweron:
            self._poweron = False

class Smartphone(Eletronico, LogFileMixin):
    def poweron(self):
        super().poweron()

        if self._poweron:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)
    def poweroff(self):
        super().poweroff()

        if not self._poweron:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)
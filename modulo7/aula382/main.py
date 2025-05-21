import sys
import time
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal, QThread  # Slot,
from ui_workerui import Ui_myWidget


class Worker(QObject):
    started = Signal(str)
    progress = Signal(str)
    ended = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progress.emit(value)
            time.sleep(1)
        self.ended.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker = Worker()
        self._thread = QThread()

        worker = self._worker
        thread = self._thread

        # Mover worker para thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.run)
        worker.ended.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.ended.connect(worker.deleteLater)

        worker.started.connect(self.workerStarted)
        worker.progress.connect(self.workerProgress)
        worker.ended.connect(self.workerEnded)

        thread.start()

    def workerStarted(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('worker iniciado')

    def workerProgress(self, value):
        self.label1.setText(value)
        print('worker em progresso')

    def workerEnded(self, value):
        print('worker finalizado')
        self.label1.setText(value)
        self.button1.setDisabled(False)

    def hardWork2(self):
        self._worker2 = Worker()
        self._thread2 = QThread()

        worker = self._worker2
        thread = self._thread2

        # Mover worker para thread
        worker.moveToThread(thread)

        # Run
        thread.started.connect(worker.run)
        worker.ended.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker.ended.connect(worker.deleteLater)

        worker.started.connect(self.workerStarted2)
        worker.progress.connect(self.workerProgress2)
        worker.ended.connect(self.workerEnded2)

        thread.start()

    def workerStarted2(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('worker 2 iniciado')

    def workerProgress2(self, value):
        self.label2.setText(value)
        print('worker 2 em progresso')

    def workerEnded2(self, value):
        print('worker 2 finalizado')
        self.label2.setText(value)
        self.button2.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Mywidget = MyWidget()
    Mywidget.show()
    app.exec()

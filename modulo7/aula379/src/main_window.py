from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QObject, QEvent
from PySide6.QtGui import QKeyEvent
import sys
from window import Ui_MainWindow
from typing import cast


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.sendButton.clicked.connect(self._changeLabel)
        # self.lineName.setStyleSheet('background-color: darkcyan')
        self.lineName.installEventFilter(self)

    def _changeLabel(self):
        text = self.lineName.text()
        self.labelResult.setText(text)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.KeyPress:
            event = cast(QKeyEvent, event)
            text = self.lineName.text()
            self.labelResult.setText(text + event.text())

        return super().eventFilter(watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()

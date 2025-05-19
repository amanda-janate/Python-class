from PySide6.QtWidgets import (QMainWindow, QWidget,
                               QVBoxLayout, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent)

        # main configs
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()

        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        self.setWindowTitle('CALCULADORA')

    def adjustFixedSize(self):
        # end of the script
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addGridtoVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def mkMsgBox(self):
        return QMessageBox(self)

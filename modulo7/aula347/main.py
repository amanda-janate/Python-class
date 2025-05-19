'''Calculadora com PySide6'''
import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from vars import ICON_PATH
from PySide6.QtGui import QIcon
from display import Display
from info import Info
from styles import setTheme
from button import ButtonGrid


if __name__ == '__main__':
    # cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Theme
    setTheme(app)

    # define icone da aplicação
    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info('Test')
    window.addGridtoVLayout(info)

    # display
    display = Display()
    window.addGridtoVLayout(display)

    # grid for buttons
    buttonsGrid = ButtonGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Button
    # buttonsGrid.addWidget(Button('0'), 0, 0)
    # buttonsGrid.addWidget(Button('1'), 0, 1)
    # buttonsGrid.addWidget(Button('2'), 0, 2)
    # buttonsGrid.addWidget(Button('3'), 1, 0)

    window.adjustFixedSize()
    window.show()
    app.exec()

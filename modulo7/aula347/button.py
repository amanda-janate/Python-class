from PySide6.QtWidgets import QPushButton, QGridLayout
from vars import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty
from display import Display
from PySide6.QtCore import Slot

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonGrid(QGridLayout):
    def __init__(self, display: Display,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display = display
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self._MkGrid()

    def _MkGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, i, j)
                buttonSlot = self._mkDisplaySlot(
                    self._textToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)

    def _mkDisplaySlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _textToDisplay(self, button):
        self.display.insert(button.text())

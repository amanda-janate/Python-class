from PySide6.QtWidgets import QPushButton, QGridLayout
from vars import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from PySide6.QtCore import Slot
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
from display import Display
from info import Info


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
    def __init__(self, display: Display,info, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display = display
        self.info = info
        self._equation = ''

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self._MkGrid()

    @property
    def equation(self):
        return self._equation

    @equation.getter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _MkGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                else:
                    button.setProperty('cssClass', 'normalButton')

                self.addWidget(button, i, j)
                slot = self._mkDisplaySlot(self._textToDisplay, button)
                self._connectClicked(button, slot)

    def _connectClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectClicked(button, self._clear)



    def _mkDisplaySlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _textToDisplay(self, button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self, msg):
        print(msg)
        self.display.clear()

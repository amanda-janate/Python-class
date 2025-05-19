from PySide6.QtWidgets import QPushButton, QGridLayout
from vars import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from PySide6.QtCore import Slot
# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
from display import Display
# from info import Info
# from main_window import MainWindow
import math


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonGrid(QGridLayout):
    def __init__(self, display: Display, info, window, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None
        self._equationInitial = 'Initial text'
        self.equation = self._equationInitial

        self._gridMask = [
            ['C', '◀', '*', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self._MkGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _MkGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                else:
                    button.setProperty('cssClass', 'normalButton')

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectClicked(button, slot)

    def _connectClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectClicked(button, self._clear)

        if text == '◀':
            self._connectClicked(button, self.display.backspace)

        if text in '+-/*^':
            self._connectClicked(
                button,
                self._makeSlot(self._configLeftOp, button)
            )

        if text == '=':
            self._connectClicked(button, self._eq)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)

    @Slot()
    def _clear(self):
        self._right = None
        self._left = None
        self._op = None
        self.equation = self._equationInitial
        self.display.clear()

    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text()  # primeiro num (_left)
        self.display.clear()  # limpa display

        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada.')
            return

        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError('Conta incompleta.')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                result = math.pow(self._left, self._right)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Divisão por zero.')
        except OverflowError:
            self._showError('Resultado da conta: ∞')
        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')

        self._left = result
        self._right = None

        if result == 'error':
            self._left = None

    def _showError(self, text):
        msgBox = self.window.mkMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        # msgBox.setStandardButtons(
        #     msgBox.StandardButton.Cancel
        # )
        msgBox.exec()

    def _showInfo(self, text):
        msgBox = self.window.mkMsgBox()
        msgBox.setText(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()

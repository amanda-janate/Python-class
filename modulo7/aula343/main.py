'''PySide6 para GUI'''
# import PySide6.QtCore
# print(PySide6.__version__)
# print(PySide6.QtCore.__version__) #type: ignore
import sys
from PySide6.QtWidgets import  QApplication, QPushButton, QWidget, QGridLayout, QMainWindow
from PySide6.QtCore import Slot

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
layout = QGridLayout()
window.setWindowTitle('My Application')

button = QPushButton('Text')
button.setStyleSheet('font-size: 40px; background-color: darkviolet;')
# button.show()

button2 = QPushButton('Text2')
button2.setStyleSheet('font-size: 40px; background-color: darkcyan;')
# button2.show()

button3 = QPushButton('Text3')
button3.setStyleSheet('font-size: 40px; background-color: darkblue;')

# central widget recebe o layout
central_widget.setLayout(layout)
# layout recebe outros widgets
layout.addWidget(button, 1, 1)
layout.addWidget(button2, 2, 2)
layout.addWidget(button3, 3, 1, 1, 2) # row, col, rowspan, colspan

# status bar
status_bar = window.statusBar()
status_bar.showMessage('Bar messege')

@Slot()
def slot_triggered(status_bar):
    status_bar.showMessage('Slot executado')

@Slot()
def slot_toggled(checked):
    print('Esta amarcado?', checked)

@Slot()
def slot_delay(action):
    def inner():
        slot_toggled(action.isChecked())
    return inner

# menu bar
menu = window.menuBar()
first_menu = menu.addMenu('Menu 1')
first_action = first_menu.addAction('Action 1')
first_action.triggered.connect(lambda: slot_triggered(status_bar))

second_action = first_menu.addAction('Action 2')
second_action.setCheckable(True)
second_action.toggled.connect(slot_toggled)
# second_action.hovered.connect(slot_delay(second_action))

button.clicked.connect(slot_delay(second_action))

window.show()
app.exec()
# QApplication
#   QMainWindow
#       CentralWidget
#           Layout
#               widget 1
#               widget 1
#               widget 3
#   show
# exec

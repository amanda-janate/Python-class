'''PySide6 para GUI'''
# import PySide6.QtCore
# print(PySide6.__version__)
# print(PySide6.QtCore.__version__) #type: ignore
import sys
from PySide6.QtWidgets import  QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

button = QPushButton('Text')
button.setStyleSheet('font-size: 40px; background-color: darkviolet;')
# button.show()

button2 = QPushButton('Text2')
button2.setStyleSheet('font-size: 40px; background-color: darkcyan;')
# button2.show()

button3 = QPushButton('Text3')
button3.setStyleSheet('font-size: 40px; background-color: darkblue;')

central_widget = QWidget()

layout = QGridLayout()

# central widget recebe o layout
central_widget.setLayout(layout)
# layout recebe outros widgets
layout.addWidget(button, 1, 1)
layout.addWidget(button2, 2, 2)
layout.addWidget(button3, 3, 1, 1, 2) # row, col, rowspan, colspan

central_widget.show()
app.exec()
# QApplication
#   CentralWidget
#       Layout
#           widget 1
#           widget 1
#           widget 3
#   show
# exec

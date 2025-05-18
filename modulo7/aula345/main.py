'''PySide6 para GUI'''
# import PySide6.QtCore
# print(PySide6.__version__)
# print(PySide6.QtCore.__version__) #type: ignore
import sys
from PySide6.QtWidgets import  QApplication, QPushButton, QWidget, QGridLayout, QMainWindow
from PySide6.QtCore import Slot

app = QApplication(sys.argv)

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.setWindowTitle('My Application')

        self.button = self.mk_button('Text1')
        self.button.clicked.connect(self.slot_toggled)

        self.button2 = self.mk_button('Text2')        # button2.show()

        self.button3 = self.mk_button('Text3')

        # central widget recebe o layout
        self.central_widget.setLayout(self.grid_layout)
        # layout recebe outros widgets
        self.grid_layout.addWidget(self.button, 1, 1)
        self.grid_layout.addWidget(self.button2, 2, 2)
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2) # row, col, rowspan, colspan

        # status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Bar messege')

        # menu bar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('Menu 1')

        self.first_action = self.first_menu.addAction('Action 1')
        self.first_action.triggered.connect(self.slot_triggered)

        self.second_action = self.first_menu.addAction('Action 2')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.slot_toggled)
        # second_action.hovered.connect(slot_delay(second_action))

    @Slot()
    def slot_triggered(self):
        self.status_bar.showMessage('Slot executado')

    @Slot()
    def slot_toggled(self, checked):
        print('Esta amarcado?', self.second_action.isChecked())

    def mk_button(self, text):
        button = QPushButton(text)
        button.setStyleSheet('font-size: 40px; background-color: darkcyan;')
        return button

if __name__ == '__main__':
    window = MyWindow()

    window.show()
    app.exec()

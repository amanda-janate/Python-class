# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(560, 528)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelResult = QLabel(self.centralwidget)
        self.labelResult.setObjectName(u"labelResult")
        font = QFont()
        font.setFamilies([u"Book Antiqua"])
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.labelResult.setFont(font)
        self.labelResult.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.labelResult, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineName = QLineEdit(self.centralwidget)
        self.lineName.setObjectName(u"lineName")
        font1 = QFont()
        font1.setFamilies([u"Book Antiqua"])
        font1.setPointSize(15)
        self.lineName.setFont(font1)

        self.gridLayout_2.addWidget(self.lineName, 0, 1, 1, 1)

        self.labelname = QLabel(self.centralwidget)
        self.labelname.setObjectName(u"labelname")
        font2 = QFont()
        font2.setFamilies([u"Book Antiqua"])
        font2.setPointSize(20)
        self.labelname.setFont(font2)

        self.gridLayout_2.addWidget(self.labelname, 0, 0, 1, 1)

        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setFont(font1)

        self.gridLayout_2.addWidget(self.sendButton, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 560, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelResult.setText(QCoreApplication.translate("MainWindow", u"Um texto aqui", None))
        self.lineName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seu nome", None))
        self.labelname.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi


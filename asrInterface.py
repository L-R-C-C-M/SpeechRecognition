# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QDesktopWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        screen = QDesktopWidget().screenGeometry()
        height = screen.height() * 0.8
        width = height*0.65
        #MainWindow.resize(314*2, 462*2)
        MainWindow.resize(width, height)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)

        self.label_3.setGeometry(QtCore.QRect(width*0.15, height*0.4, width*0.7, height*0.07))
        #self.label_3.setGeometry(QtCore.QRect(120, 460, 201*2, 51*2))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        #self.label_2.setGeometry(QtCore.QRect(120, 400, 201*2, 21*2))
        self.label_2.setGeometry(QtCore.QRect(width*0.15, height*0.32, width*0.7, height*0.06))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        #self.voiceFig.setGeometry(QtCore.QRect(140, 100, 161*2, 121*2))
        self.voiceFig.setGeometry(QtCore.QRect(width*0.2, height*0.04, width*0.6, height*0.3))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setStyleSheet("background-color: rgb(0,40,166); color:rgb(115,213,252);border-radius: 20px;")
        #self.exitButton.setGeometry(QtCore.QRect(140,700, 80*2, 30*2))
        self.exitButton.setGeometry(QtCore.QRect(width*0.35, height*0.88, width*0.3, height*0.05))
        self.exitButton.setObjectName("exitButton")
        self.exitButton.setText("Exit")
        self.exitButton.clicked.connect(MainWindow.close)
        #self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setStyleSheet("QTextEdit {border: 2px solid  rgb(40, 40, 40);padding: 10px;}")
        #self.textBrowser.setGeometry(QtCore.QRect(40, 250, 551, 241))
        self.textBrowser.setTextColor(QtGui.QColor(0, 100, 210))
        self.textBrowser.setGeometry(QtCore.QRect(width*0.15, height*0.6, width*0.7, height*0.23))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.append(">> What do you want me to do for you? ")


        self.label = QtWidgets.QLabel(self.centralwidget)
        #self.label.setGeometry(QtCore.QRect(140, 320, 161*2, 21*2))
        self.label.setGeometry(QtCore.QRect(width*0.15, height*0.31, width*0.7, height*0.07))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        #self.label_4.setGeometry(QtCore.QRect(120, 560, 201*2, 51*2))
        self.label_4.setGeometry(QtCore.QRect(width*0.15, height*0.48, width*0.7, height*0.07))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play music\""))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))


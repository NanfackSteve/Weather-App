# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import images.res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 150, 241, 25))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setStatusTip("")
        self.lineEdit.setAutoFillBackground(True)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 200, 101, 41))
        self.pushButton.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Yrsa Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(238, 238, 236);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.backgrd = QtWidgets.QLabel(self.centralwidget)
        self.backgrd.setGeometry(QtCore.QRect(0, -20, 600, 550))
        self.backgrd.setMinimumSize(QtCore.QSize(600, 550))
        self.backgrd.setMaximumSize(QtCore.QSize(600, 550))
        self.backgrd.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yrsa Medium")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.backgrd.setFont(font)
        self.backgrd.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.backgrd.setStyleSheet("background-image: url(:/home/sun/Documents/prog_Python/QtDesigner/images/weather7.jpg);")
        self.backgrd.setInputMethodHints(QtCore.Qt.ImhNone)
        self.backgrd.setText("")
        self.backgrd.setPixmap(QtGui.QPixmap(":/home/sun/Documents/prog_Python/QtDesigner/images/weather7.jpg"))
        self.backgrd.setScaledContents(True)
        self.backgrd.setObjectName("backgrd")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 310, 67, 17))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 350, 67, 17))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 390, 67, 17))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 430, 91, 17))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 310, 101, 17))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 350, 101, 17))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 390, 101, 17))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 430, 101, 17))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.country = QtWidgets.QLabel(self.centralwidget)
        self.country.setGeometry(QtCore.QRect(110, 310, 71, 17))
        self.country.setStyleSheet("color: rgb(255, 255, 255);")
        self.country.setObjectName("country")
        self.city = QtWidgets.QLabel(self.centralwidget)
        self.city.setGeometry(QtCore.QRect(90, 350, 91, 17))
        self.city.setStyleSheet("color: rgb(255, 255, 255);")
        self.city.setObjectName("city")
        self.main = QtWidgets.QLabel(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(120, 390, 121, 17))
        self.main.setStyleSheet("color: rgb(255, 255, 255);")
        self.main.setObjectName("main")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(130, 430, 121, 17))
        self.description.setStyleSheet("color: rgb(255, 255, 255);")
        self.description.setObjectName("description")
        self.temperature = QtWidgets.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(520, 310, 67, 17))
        self.temperature.setStyleSheet("color: rgb(255, 255, 255);")
        self.temperature.setObjectName("temperature")
        self.pressure = QtWidgets.QLabel(self.centralwidget)
        self.pressure.setGeometry(QtCore.QRect(500, 350, 67, 17))
        self.pressure.setStyleSheet("color: rgb(255, 255, 255);")
        self.pressure.setObjectName("pressure")
        self.humidity = QtWidgets.QLabel(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(500, 390, 81, 17))
        self.humidity.setStyleSheet("color: rgb(255, 255, 255);")
        self.humidity.setObjectName("humidity")
        self.cloud = QtWidgets.QLabel(self.centralwidget)
        self.cloud.setGeometry(QtCore.QRect(500, 430, 81, 17))
        self.cloud.setStyleSheet("color: rgb(255, 255, 255);")
        self.cloud.setObjectName("cloud")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 290, 561, 1))
        self.line.setStyleSheet("color: rgb(238, 238, 236);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 470, 561, 1))
        self.line_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 290, 1, 181))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(580, 290, 1, 181))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.backgrd.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.country.raise_()
        self.city.raise_()
        self.main.raise_()
        self.description.raise_()
        self.temperature.raise_()
        self.pressure.raise_()
        self.humidity.raise_()
        self.cloud.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather App"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Location"))
        self.pushButton.setText(_translate("MainWindow", " Search"))
        self.label_2.setText(_translate("MainWindow", "Country :"))
        self.label_3.setText(_translate("MainWindow", "City :"))
        self.label_4.setText(_translate("MainWindow", "Principal :"))
        self.label_5.setText(_translate("MainWindow", "Description :"))
        self.label_6.setText(_translate("MainWindow", "Temperature :"))
        self.label_7.setText(_translate("MainWindow", "Pressure :"))
        self.label_8.setText(_translate("MainWindow", "Humidity :"))
        self.label_9.setText(_translate("MainWindow", "Clouds :"))
        self.country.setText(_translate("MainWindow", "-  - /  -  -"))
        self.city.setText(_translate("MainWindow", "-  - /  -  -"))
        self.main.setText(_translate("MainWindow", "-  - /  -  -"))
        self.description.setText(_translate("MainWindow", "-  - /  -  -"))
        self.temperature.setText(_translate("MainWindow", "-  - /  -  -"))
        self.pressure.setText(_translate("MainWindow", "-  - /  -  -"))
        self.humidity.setText(_translate("MainWindow", "-  - /  -  -"))
        self.cloud.setText(_translate("MainWindow", "-  - /  -  -"))


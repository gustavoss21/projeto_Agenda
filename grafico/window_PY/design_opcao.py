# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maisopcoes.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        MainWindow.setStyleSheet("alternate-background-color: qconicalgradient(cx:0.436, cy:0.5735, angle:0, stop:0.153465 rgba(50, 57, 147, 202), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.widget.setAutoFillBackground(True)
        self.widget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.53295, y1:0.631, x2:0.542602, y2:1, stop:0.0149254 rgba(66, 147, 200, 255), stop:1 rgba(255, 255, 255, 255))")
        self.widget.setObjectName("widget")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(100, 40, 187, 400))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 400))
        self.frame_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.frame_2.setAcceptDrops(True)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.53295, y1:0.631, x2:0.542602, y2:1, stop:0 rgba(64, 146, 200, 229), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:pad, x1:0.582701, y1:0.358, x2:0.542602, y2:1, stop:0 rgba(64, 146, 200, 229), stop:1 rgba(255, 255, 255, 255))")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(6)
        self.frame_2.setMidLineWidth(-6)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.pushButton_2.setStyleSheet("background-color: rgb(40, 101, 157);\n"
"color:rgb(255, 255, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(40, 101, 157);\n"
"color:rgb(255, 255, 255)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(40, 101, 157);\n"
"color:rgb(255, 255, 255)")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setEnabled(True)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 117, 120))
        self.frame_3.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.53295, y1:0.631, x2:0.542602, y2:1, stop:0.0149254 rgba(66, 147, 200, 255), stop:1 rgba(255, 255, 255, 255))qlineargradient(spread:pad, x1:0.53295, y1:0.631, x2:0.542602, y2:1, stop:0.0149254 rgba(66, 147, 200, 255), stop:1 rgba(255, 255, 255, 255))")
        self.frame_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(40, 101, 157);\n"
"color:rgb(255, 255, 255)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addWidget(self.widget, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.pushButton_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">ops 1</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "opcao 3"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "opcao 2"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "opcao 1"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "sair"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opcoes.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.53295, y1:0.631, x2:0.542602, y2:1, stop:0.0149254 rgba(66, 147, 200, 255),)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame.setStyleSheet("background-color:qlineargradient(spread:pad,\n"
" x1:0.53295, y1:0.631, x2:0.542602, y2:1,\n"
" stop:0.0149254 rgba(66, 147, 200, 255)\n"
", stop:1 rgba(255, 255, 255, 255))\n"
"qlineargradient(spread:pad,\n"
" x1:0.53295, y1:0.631, x2:0.542602, y2:1,\n"
" stop:0.0149254 rgba(66, 147, 200, 255)\n"
", stop:1 rgba(255, 255, 255, 255))")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.lab_tex_agora = QtWidgets.QLabel(self.frame_6)
        self.lab_tex_agora.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lab_tex_agora.setFont(font)
        self.lab_tex_agora.setStyleSheet("background-color:qlineargradient(spread:pad,\n"
" x1:0.53295, y1:0.631, x2:0.542602, y2:1,\n"
" stop:0.0149254 rgba(66, 147, 200, 255))")
        self.lab_tex_agora.setObjectName("lab_tex_agora")
        self.gridLayout.addWidget(self.lab_tex_agora, 0, 1, 1, 1)
        self.lab_hora = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lab_hora.setFont(font)
        self.lab_hora.setStyleSheet("color:white")
        self.lab_hora.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_hora.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_hora.setObjectName("lab_hora")
        self.gridLayout.addWidget(self.lab_hora, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lab_tex_tarefa = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_tex_tarefa.setFont(font)
        self.lab_tex_tarefa.setStyleSheet("color:black")
        self.lab_tex_tarefa.setObjectName("lab_tex_tarefa")
        self.gridLayout_3.addWidget(self.lab_tex_tarefa, 0, 1, 1, 1)
        self.lab_tex_tempo = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lab_tex_tempo.setFont(font)
        self.lab_tex_tempo.setStyleSheet("color:black")
        self.lab_tex_tempo.setObjectName("lab_tex_tempo")
        self.gridLayout_3.addWidget(self.lab_tex_tempo, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lab_dat = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_dat.setFont(font)
        self.lab_dat.setStyleSheet("color: rgb(255, 0, 0);")
        self.lab_dat.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lab_dat.setObjectName("lab_dat")
        self.gridLayout_6.addWidget(self.lab_dat, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.lab_tex_nada = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_tex_nada.sizePolicy().hasHeightForWidth())
        self.lab_tex_nada.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lab_tex_nada.setFont(font)
        self.lab_tex_nada.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_tex_nada.setStyleSheet("color: rgb(255, 0, 0);")
        self.lab_tex_nada.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lab_tex_nada.setText("")
        self.lab_tex_nada.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_tex_nada.setObjectName("lab_tex_nada")
        self.gridLayout_6.addWidget(self.lab_tex_nada, 2, 2, 1, 1, QtCore.Qt.AlignTop)
        self.lab_tarefa = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_tarefa.sizePolicy().hasHeightForWidth())
        self.lab_tarefa.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_tarefa.setFont(font)
        self.lab_tarefa.setStyleSheet("color:rgb(255, 255, 255)")
        self.lab_tarefa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lab_tarefa.setText("")
        self.lab_tarefa.setObjectName("lab_tarefa")
        self.gridLayout_6.addWidget(self.lab_tarefa, 1, 3, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 5, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_5.setStyleSheet("background-color:qlineargradient(spread:pad,\n"
" x1:0.53295, y1:0.631, x2:0.542602, y2:1,\n"
" stop:0.0149254 rgba(66, 147, 200, 255)\n"
", stop:1 rgba(255, 255, 255, 255))\n"
"qlineargradient(spread:pad,\n"
" x1:0.53295, y1:0.631, x2:0.542602, y2:1,\n"
" stop:0.0149254 rgba(66, 147, 200, 255)\n"
", stop:1 rgba(255, 255, 255, 255))")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lab_feito = QtWidgets.QPushButton(self.frame_5)
        self.lab_feito.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.lab_feito.sizePolicy().hasHeightForWidth())
        self.lab_feito.setSizePolicy(sizePolicy)
        self.lab_feito.setMinimumSize(QtCore.QSize(0, 0))
        self.lab_feito.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lab_feito.setFont(font)
        self.lab_feito.setAcceptDrops(False)
        self.lab_feito.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lab_feito.setAutoFillBackground(False)
        self.lab_feito.setStyleSheet("background-color: rgb(40, 101, 157);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.lab_feito.setIconSize(QtCore.QSize(50, 50))
        self.lab_feito.setCheckable(True)
        self.lab_feito.setChecked(False)
        self.lab_feito.setAutoRepeat(False)
        self.lab_feito.setAutoExclusive(False)
        self.lab_feito.setAutoDefault(False)
        self.lab_feito.setDefault(False)
        self.lab_feito.setFlat(True)
        self.lab_feito.setObjectName("lab_feito")
        self.gridLayout_2.addWidget(self.lab_feito, 0, 0, 1, 1)
        self.lab_adiar = QtWidgets.QPushButton(self.frame_5)
        self.lab_adiar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.lab_adiar.sizePolicy().hasHeightForWidth())
        self.lab_adiar.setSizePolicy(sizePolicy)
        self.lab_adiar.setMinimumSize(QtCore.QSize(0, 0))
        self.lab_adiar.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lab_adiar.setFont(font)
        self.lab_adiar.setAcceptDrops(False)
        self.lab_adiar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lab_adiar.setAutoFillBackground(False)
        self.lab_adiar.setStyleSheet("background-color: rgb(40, 101, 157);\n"
"color:rgb(255, 255, 255)\n"
"\n"
"")
        self.lab_adiar.setIconSize(QtCore.QSize(50, 50))
        self.lab_adiar.setCheckable(True)
        self.lab_adiar.setChecked(False)
        self.lab_adiar.setAutoRepeat(False)
        self.lab_adiar.setAutoExclusive(False)
        self.lab_adiar.setAutoDefault(False)
        self.lab_adiar.setDefault(False)
        self.lab_adiar.setFlat(True)
        self.lab_adiar.setObjectName("lab_adiar")
        self.gridLayout_2.addWidget(self.lab_adiar, 1, 0, 1, 1)
        self.lab_nao_farei = QtWidgets.QPushButton(self.frame_5)
        self.lab_nao_farei.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.lab_nao_farei.sizePolicy().hasHeightForWidth())
        self.lab_nao_farei.setSizePolicy(sizePolicy)
        self.lab_nao_farei.setMinimumSize(QtCore.QSize(0, 0))
        self.lab_nao_farei.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lab_nao_farei.setFont(font)
        self.lab_nao_farei.setAcceptDrops(False)
        self.lab_nao_farei.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lab_nao_farei.setAutoFillBackground(False)
        self.lab_nao_farei.setStyleSheet("background-color: rgb(40, 101, 157);\n"
"color:rgb(255, 255, 255)\n"
"")
        self.lab_nao_farei.setIconSize(QtCore.QSize(50, 50))
        self.lab_nao_farei.setCheckable(True)
        self.lab_nao_farei.setChecked(False)
        self.lab_nao_farei.setAutoRepeat(False)
        self.lab_nao_farei.setAutoExclusive(False)
        self.lab_nao_farei.setAutoRepeatDelay(10)
        self.lab_nao_farei.setAutoRepeatInterval(10)
        self.lab_nao_farei.setAutoDefault(False)
        self.lab_nao_farei.setDefault(False)
        self.lab_nao_farei.setFlat(True)
        self.lab_nao_farei.setObjectName("lab_nao_farei")
        self.gridLayout_2.addWidget(self.lab_nao_farei, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_5, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 2, 3, 1, 1)
        self.lab_tex_opcao = QtWidgets.QLabel(self.frame_4)
        self.lab_tex_opcao.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lab_tex_opcao.setFont(font)
        self.lab_tex_opcao.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lab_tex_opcao.setStyleSheet("background-color:qlineargradient(spread:pad,\n"
" x1:0.53295, y1:0.631, x2:0.542602, y2:1,\n"
" stop:0.0149254 rgba(66, 147, 200, 255))")
        self.lab_tex_opcao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lab_tex_opcao.setObjectName("lab_tex_opcao")
        self.gridLayout_4.addWidget(self.lab_tex_opcao, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.lab_nao_farei.clicked['bool'].connect(self.lab_feito.setDisabled) # type: ignore
        self.lab_nao_farei.clicked['bool'].connect(self.lab_adiar.setDisabled) # type: ignore
        self.lab_adiar.clicked['bool'].connect(self.lab_nao_farei.setDisabled) # type: ignore
        self.lab_adiar.clicked['bool'].connect(self.lab_feito.setDisabled) # type: ignore
        self.lab_feito.clicked['bool'].connect(self.lab_adiar.setDisabled) # type: ignore
        self.lab_feito.clicked['bool'].connect(self.lab_nao_farei.setDisabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_tex_agora.setText(_translate("MainWindow", "PARA AGORA:                "))
        self.lab_hora.setText(_translate("MainWindow", "hora_agora"))
        self.lab_tex_tarefa.setText(_translate("MainWindow", "tarefa:"))
        self.lab_tex_tempo.setText(_translate("MainWindow", "daqui ha:"))
        self.lab_dat.setText(_translate("MainWindow", "00:00"))
        self.lab_feito.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>adicionar tafefas</p></body></html>"))
        self.lab_feito.setText(_translate("MainWindow", "ESTA FEITO ?"))
        self.lab_adiar.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>adicionar tafefas</p></body></html>"))
        self.lab_adiar.setText(_translate("MainWindow", "VAI ADIAR ?"))
        self.lab_nao_farei.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>adicionar tafefas</p></body></html>"))
        self.lab_nao_farei.setText(_translate("MainWindow", "NÃO FARA  ?"))
        self.lab_tex_opcao.setText(_translate("MainWindow", "escolha uma opção:                       "))

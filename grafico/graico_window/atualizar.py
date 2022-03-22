import sys
import threading
from datetime import datetime, timedelta
from time import sleep
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox, QApplication
from PyQt5 import QtWidgets, QtGui, QtCore
import os
from projeto_Agenda.grafico.graico_window.utils import Mensagem
from projeto_Agenda.grafico.window_PY import design_atualizadata
from projeto_Agenda.processa_arquivo.gerencia_arquivo import salvar_mudancas, apagar_tarefa
from projeto_Agenda.processa_arquivo.proc_arq import proc_arquivo
from projeto_Agenda.processamento_dados.ajusta_lista import ListaEditada

arquivo = proc_arquivo().resultado()

class Atualiza(QMainWindow,design_atualizadata.Ui_MainWindow):
    def __init__(self,dados,aberto=False,parent=None,):
        super(Atualiza, self).__init__(parent)
        super(Atualiza, self).setupUi(self)

        self.lista_mostrar = dados
        # self.lista_mostrar = sorted(dados, key=lambda x: x[1])
        # self.lista_original =
        # self.lista = [x['dicionario'] for x in self.lista_original]
        # self.lista = sorted(self.lista, key=lambda x: x['tarefa'])

        self.aberto = aberto
        if not aberto:
            self.deDentro()

        else:
           self.deFora()

        self.spinBox.setMinimum(1)
        self.pushButton_2.clicked.connect(self.apagar)
        self.pushButton.clicked.connect(self.salvar)
        self.pushButton_3.clicked.connect(self.sair)
        self.checkBox.setEnabled(True)

        if self.lista_mostrar == []:

            self.close()

        threads = threading.Thread(target=self.habilted)
        threads.start()


    def deDentro(self):
        self.listWidget = QtWidgets.QListWidget(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(2)
        self.listWidget.setMidLineWidth(-1)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_4.addWidget(self.listWidget, 0, 0, 1, 1)

        # self.pushButton.setDisabled(True)

        self.listWidget.itemClicked.connect(self.clic)
        self.funcao_mostrar_lista()

    def deFora(self):

        self.teste = QtWidgets.QLabel(self.frame_5)
        self.gridLayout_4.addWidget(self.teste, 0, 0, 1, 1)
        self.interar = iter(self.lista_mostrar)
        self.teste.setAlignment(QtCore.Qt.AlignTop)
        self.teste.setAlignment(QtCore.Qt.AlignHCenter)
        self.teste.setStyleSheet('*{font:20pt ; color:white}')
        self.indec()
        self.enable()



    def indec(self):
            try:
                dicionario = next(self.interar)

            except:
                self.close()
            else:
                for contador, dicio in enumerate(self.lista_mostrar):
                    if dicio[1] == dicionario[1]:
                        self.indix = contador

                self.teste.setText(self.lista_mostrar[self.indix][1])
                self.mostrar_data()


    def funcao_mostrar_lista(self):
        self.listWidget.clear()
        for lista in self.lista_mostrar:
            self.listWidget.addItem(QListWidgetItem(lista[1]))

        # self.listWidget.sortItems()


    def sair(self):
        if not self.aberto:
            self.setVisible(False)

        else:
            self.close()


    def clic(self):
        print('click')
        self.indix = self.listWidget.currentRow()
        if str(self.indix).isnumeric():
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            self.dateTimeEdit.setEnabled(True)
            self.pushButton.setStyleSheet('* {background-color: rgb(40, 101, 157);color:rgb(255, 255, 255);}')
            self.pushButton_2.setStyleSheet('* {background-color: rgb(40, 101, 157);color:rgb(255, 255, 255);}')
        self.mostrar_data()
        self.checkBox.setEnabled(True)
        print(self.lista_mostrar[self.indix])

        checking = self.lista_mostrar[self.indix][3]

        if checking == 1:
            self.checkBox.setChecked(True)


        else:
            self.checkBox.setChecked(False)


    def enable(self):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.dateTimeEdit.setEnabled(True)
        self.pushButton.setStyleSheet('* {background-color: rgb(40, 101, 157);color:rgb(255, 255, 255);}')
        self.pushButton_2.setStyleSheet('* {background-color: rgb(40, 101, 157);color:rgb(255, 255, 255);}')


        self.checkBox.setEnabled(True)

        checking = self.lista_mostrar[self.indix][3]
        if checking == 1:
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)


    def mostrar_data(self):
            data = self.lista_mostrar[self.indix][2]
            # data = datetime.strptime(data,'%Y-%m-%d %H:%M')
            data = data.strftime('%d/%m/%Y %H:%M')

            self.label_3.setText(data)
            data = datetime.strptime(data,'%d/%m/%Y %H:%M')
            data = datetime.now() + timedelta(1)
            self.dateTimeEdit.setDateTime(data)


    def salvar(self):
            print('antes checking23')
            definida = self.dateTimeEdit.text()
            definida = datetime.strptime(definida,'%d/%m/%Y %H:%M')

            data_agora = datetime.now().strftime('%d/%m/%Y %H:%M')

            data_agora = datetime.strptime(data_agora,'%d/%m/%Y %M:%S')
            print('antes chec')
            if definida < data_agora:
                teste = Mensagem()
                teste =  teste.menss('data inválida','A data definida não deve ser inferior a atual',QMessageBox.Warning,QMessageBox.Ok)
                teste.exec_()

            else:
                    print(definida,type(definida))
                    definida = definida.strftime('%Y-%m-%d %H:%M')
                    definida = datetime.strptime(definida,'%Y-%m-%d %H:%M')
                    lista = list(self.lista_mostrar[self.indix])
                    print('lista',lista)
                    lista[2] = definida
                    # lista[self.indix][2] = definida
                    check = self.checkBox.isChecked()
                    print('antes checking')
                    if check == True:
                        lista[3] = check
                        lista[4] = self.comboBox.currentText()
                        lista[5] = int(self.spinBox.text())
                    else:
                        lista[3] = False
                        lista[4] = 'null'
                        lista[5] = 'null'
                    lista = tuple(lista)
#tenta salvar (34, 'VAILA', datetime.datetime(2022, 3, 25, 12, 45), True, 'dias', 1)
                    print('tenta salvar',lista)
                    salvar_mudancas(lista,check)
                    print('tenta salvar123')
                    if not self.aberto:
                        if self.lista_mostrar == []:
                                self.setVisible(False)

                        self.listWidget.clear()
                        self.funcao_mostrar_lista()

                    else:
                        if self.lista_mostrar == []:
                            self.setVisible(False)
                        self.indec()

    def habilted(self):
        sleep(0.5)
        while True:
            check = self.checkBox.isChecked()
            if check == True:
                self.spinBox.setEnabled(True)
                self.label_5.setEnabled(True)
                self.comboBox.setEnabled(True)

            if check == False:
                self.spinBox.setEnabled(False)
                self.label_5.setEnabled(False)
                self.comboBox.setEnabled(False)

    def apagar(self):
            print(self.indix)
            # self.lista_original = abrir_lista_arquivo(arquivo)
            # total_arquivo = len(self.lista_original)
            #editar esse depois
            apagar_tarefa(self.lista_mostrar[self.indix][0])

            del self.lista_mostrar[self.indix]
            if not self.aberto:
                    if self.lista_mostrar == []:
                       self.setVisible(False)

                    else:
                        self.funcao_mostrar_lista()

            else:
                if self.lista_mostrar == []:
                    self.close()

                else:
                    self.indec()



print(__name__,'122')

if __name__ == '__main__':
    lista = ListaEditada()
    lista = lista.tarefaPassada()
    if not lista == []:

        app = QApplication(sys.argv)
        atualiza = Atualiza(lista,aberto=True)

        atualiza.show()

        sys.exit(app.exec_())



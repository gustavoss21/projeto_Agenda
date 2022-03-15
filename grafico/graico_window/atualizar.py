import sys
import threading
from datetime import datetime, timedelta
from time import sleep

from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox, QApplication

# from grafico.graico_window.utils import Mensagem
# from grafico.window_PY import design_atualizadata
# from processamento_dados.ajusta_lista import ListaEditada
# from processa_arquivo.gerencia_arquivo import abrir_lista_arquivo, salvar_mudancas, apagar_tarefa
# from processa_arquivo.proc_arq import proc_arquivo
from PyQt5 import QtWidgets, QtGui, QtCore
import os

from projeto_base.grafico.graico_window.utils import Mensagem
from projeto_base.grafico.window_PY import design_atualizadata
from projeto_base.processa_arquivo.gerencia_arquivo import abrir_lista_arquivo, salvar_mudancas, apagar_tarefa
from projeto_base.processa_arquivo.proc_arq import proc_arquivo
from projeto_base.processamento_dados.ajusta_lista import ListaEditada

arquivo = proc_arquivo().resultado('escreva.txt')

class Atualiza(QMainWindow,design_atualizadata.Ui_MainWindow):
    def __init__(self,dados,aberto=False,parent=None,):
        super(Atualiza, self).__init__(parent)
        super(Atualiza, self).setupUi(self)

        dados = [x['dicionario'] for x in dados]
        self.lista_mostrar = sorted(dados, key=lambda x: x['tarefa'])
        self.lista_original = abrir_lista_arquivo(arquivo)
        self.lista = [x['dicionario'] for x in self.lista_original]
        self.lista = sorted(self.lista, key=lambda x: x['tarefa'])

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
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "")
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
                    if dicio['tarefa'] == dicionario['tarefa']:
                        self.indix = contador

                self.teste.setText(self.lista_mostrar[self.indix]['tarefa'])
                self.mostrar_data()


    def funcao_mostrar_lista(self):
        self.listWidget.clear()
        for lista in self.lista_mostrar:
            self.listWidget.addItem(QListWidgetItem(lista['tarefa']))

        self.listWidget.sortItems()


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


        checking = self.lista_mostrar[self.indix]['checking']

        if checking == True:
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

        checking = self.lista_mostrar[self.indix]['checking']
        if checking == True:
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)


    def mostrar_data(self):
            data = self.lista_mostrar[self.indix]['date'][:]
            data = datetime.strptime(data,'%Y-%m-%d %H:%M')
            data = data.strftime('%d/%m/%Y %H:%M')

            self.label_3.setText(data)
            data = datetime.strptime(data,'%d/%m/%Y %H:%M')
            data = datetime.now() + timedelta(1)
            self.dateTimeEdit.setDateTime(data)


    def salvar(self):

            definida = self.dateTimeEdit.text()
            definida = datetime.strptime(definida,'%d/%m/%Y %H:%M')

            data_agora = datetime.now().strftime('%d/%m/%Y %H:%M')

            data_agora = datetime.strptime(data_agora,'%d/%m/%Y %M:%S')
            if definida < data_agora:
                teste = Mensagem()
                teste =  teste.menss('data inválida','A data definida não deve ser inferior a atual',QMessageBox.Warning,QMessageBox.Ok)
                teste.exec_()

            else:
                    definida = definida.strftime('%Y-%m-%d %H:%M')
                    self.lista_mostrar[self.indix]['date'] = definida
                    check = self.checkBox.isChecked()
                    if check == True:
                        self.lista_mostrar[self.indix]['checking'] = check
                        self.lista_mostrar[self.indix]['intervalo_check'] = self.checkBox.isChecked()
                        self.lista_mostrar[self.indix]['intervalo_opcao'] = self.comboBox.currentText()
                        self.lista_mostrar[self.indix]['intervalo_valor'] = self.spinBox.text()

                    for contador,dicio in enumerate(self.lista_original):

                        for cont,dic in enumerate(self.lista_mostrar.copy()):

                            if dic['tarefa'] == dicio['dicionario']['tarefa']:
                                dicio['dicionario'] = dic

                    salvar_mudancas(arquivo, self.lista_original)

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



            self.lista_original = abrir_lista_arquivo(arquivo)
            total_arquivo = len(self.lista_original)
            if total_arquivo <= 1:
                os.remove(arquivo)
                self.close()

            apagar_tarefa(arquivo, self.lista_original, self.lista_mostrar[self.indix]['tarefa'])

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
    lista = ListaEditada(arquivo)

    lista = lista.tarefaPassada()
    print('lista passada',lista)

    # lista_nova = lista['lista_nova']
    if not lista == []:

        app = QApplication(sys.argv)
        atualiza = Atualiza(lista,aberto=True)

        atualiza.show()

        sys.exit(app.exec_())


import sys
import threading

from datetime import datetime

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication

# from grafico.graico_window.adicionar import Adicionar
# from grafico.graico_window.adicionar import Adicionar
from projeto_base.grafico.graico_window.atualizar import Atualiza
from projeto_base.grafico.graico_window.utils import arquivo
from projeto_base.grafico.tarefa_agora.verificar_agora import agora
from projeto_base.grafico.tarefa_agora.window_agora import ParaAgora
from projeto_base.grafico.window_PY import desig_menu
from projeto_base.processa_arquivo.gerencia_arquivo import abrir_lista_arquivo
from projeto_base.processamento_dados.ajusta_lista import ListaEditada

from projeto_base.grafico.graico_window.adicionar import Adicionar


class Menu(QMainWindow, desig_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super(Menu, self).setupUi(self)

        self.btn_adicionar_tarefa.clicked.connect(self.btn_adicionaTarefas)
        # self.mostrar()
        self.btn_adicionar_tarefa_2.clicked.connect(self.btn_maisOpcoes)
        self.showList()
        self.pushButton.clicked.connect(self.ParaAgora)
        self.enabled()

    def showList(self):
        self.dados = ListaEditada(arquivo)
        self.dados = self.dados.tarefaAgora()

        tamanho = 30
        for contador, dicionario in enumerate(self.dados[0]):
            date = dicionario["date"]
            date = datetime.strptime(date, '%Y-%m-%d %H:%M')
            date = date.strftime('%H:%M')
            strings = f'{dicionario["tarefa"]:{" "}<{self.formatStr(dicionario["tarefa"])}} {date}'

            if contador >= 1:

                tamanho += 30
                self.listWidget.setMinimumHeight(tamanho)
            self.listWidget.addItem(str(strings))

    def formatStr(self, str):
        contador = len(str)
        if contador < 7:
            contador = 44
        elif contador < 10:
            contador = 43
        else:
            contador = 40

        return contador

    def ParaAgora(self):
        dicio = agora()
        if not dicio == []:
            self.mostra_agora = ParaAgora(*dicio)
            self.mostra_agora.show()

    def enabled(self):
        dicio = agora()

        if not dicio == []:

            self.pushButton.setEnabled(True)
            self.pushButton.setStyleSheet(
                '*{background-color: rgb(40, 101, 157);color:rgb(255, 255, 255)}')

    def setAgora(self, dicio):
        thread = threading.Thread(target=self.ParaAgora)
        thread.start()

    def add_label(self, nome, tex='', set=False):
        if not set:
            self.nome = nome
            self.nome = QtWidgets.QLabel(self.frame_3)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.nome.setFont(font)
            self.nome.setObjectName(f"{nome}")
            self.verticalLayout.addWidget(self.nome)
            # self.vLayout.addWidget(self.frame_3)
            spacerItem = QtWidgets.QSpacerItem(
                700, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout.addItem(spacerItem)
            self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 1)
        else:
            self.nome.setText(tex)

        return self.nome

        # agor = ParaAgora()
        # widget.addWidget(agor)
        # widget.setCurrentIndex(widget.currentIndex() + 1)

    def btn_maisOpcoes(self):

        lista = abrir_lista_arquivo(arquivo)

        self.atualiza = Atualiza(lista)
        if self.atualiza.isVisible():
            print('simmm123')
        self.atualiza.show()

    def btn_adicionaTarefas(self):
        if self.isActiveWindow():
            print('visivel')
            self.adicionar = Adicionar()
            if not self.adicionar.isActiveWindow():
                self.adicionar.show()
        else:
            self.atualiza.sair()

    def sair(self, event):
        respsots = QMessageBox.information(
            self, 'sair', 'tem certeza que quer sair', QMessageBox.Yes | QMessageBox.No)

        if respsots == QMessageBox.Yes:
            quit()


try:
    # executa a janela atualizar dados
    lista = ListaEditada(arquivo)
    lista = lista.tarefaPassada()

    if not lista == []:
        app = QApplication(sys.argv)
        atualiza = Atualiza(lista, aberto=True)

        atualiza.show()

        sys.exit(app.exec_())
except Exception():
    print(Exception, 'error')
finally:
    ###############################
    print('execultando')
    # executa a janela menu inicial
    qt = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    menu = Menu()
    widget.addWidget(menu)
    widget.show()

    try:
        sys.exit(qt.exec())
    except:
        print('teste de erro errado')
    app = QApplication(sys.argv)
# .................................
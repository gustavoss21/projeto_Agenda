import sys
import threading
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from projeto_Agenda.grafico.graico_window.atualizar import Atualiza
from projeto_Agenda.grafico.tarefa_agora.verificar_agora import agora
from projeto_Agenda.grafico.tarefa_agora.window_agora import ParaAgora
from projeto_Agenda.grafico.window_PY import desig_menu
from projeto_Agenda.processamento_dados.ajusta_lista import ListaEditada
from projeto_Agenda.grafico.graico_window.adicionar import Adicionar


class Menu(QMainWindow, desig_menu.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super(Menu, self).setupUi(self)

        self.btn_adicionar_tarefa.clicked.connect(self.btn_adicionaTarefas)
        self.btn_adicionar_tarefa_2.clicked.connect(self.btn_maisOpcoes)
        self.showList()
        self.pushButton.clicked.connect(self.ParaAgora)
        self.enabled()

    def showList(self):
        self.dados = ListaEditada()
        self.dados = self.dados.tarefaAgora()

        tamanho = 30
        for contador, dicionario in enumerate(self.dados):
            date = dicionario[2]
            date = date.strftime('%H:%M')
            tarefa = f'{dicionario[1]}'
            print(tarefa,'.....',date)

            if contador >= 1:

                tamanho += 30
                self.listWidget.setMinimumHeight(tamanho)
                self.listWidget_2.setMinimumHeight(tamanho)
                self.frame_7.setMaximumHeight(tamanho+10)

            self.listWidget.addItem(str(tarefa))
            self.listWidget_2.addItem(str(date))

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

    def setAgora(self):
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

    def btn_maisOpcoes(self):
        lista = ListaEditada()
        lista = lista.get_lista()

        try:
            self.atualiza.close()
        except:
            self.atualiza = Atualiza(lista)
            self.atualiza.show()
        else:
            self.atualiza.show()
        try:
            self.adicionar.close()
        except:
            ...

    def btn_adicionaTarefas(self):

            try:
                 self.adicionar.close()
            except:
                  self.adicionar = Adicionar()
                  self.adicionar.show()
            else:
                self.adicionar.show()
            try:
               self.atualiza.close()
            except:
                ...

    def sair(self):
        respsots = QMessageBox.information(
            self, 'sair', 'tem certeza que quer sair', QMessageBox.Yes | QMessageBox.No)
        if respsots == QMessageBox.Yes:
            quit()

try:
    # executa a janela atualizar dados
    lista = ListaEditada()
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

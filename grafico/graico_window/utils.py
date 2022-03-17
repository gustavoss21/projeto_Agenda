import random
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QDialogButtonBox, QMessageBox

# from grafico.window_PY.desing_calendario import Ui_MainWindow
# from processa_arquivo.proc_arq import proc_arquivo
from projeto_Agenda.grafico.window_PY.desing_calendario import Ui_MainWindow
from projeto_Agenda.processa_arquivo.proc_arq import proc_arquivo

arquivo = proc_arquivo().resultado()


def gera_id():
    id = ''
    for c in range(4):

        id += str(random.randint(1, 9))

    return int(id)


class Calendario(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_confirma.button(QDialogButtonBox.Cancel).clicked.connect(self.fechar)
        self.btn_confirma.button(QDialogButtonBox.Ok).clicked.connect(self.fechar)


    def ajusta_data(self):
        data = self.calendario_wid.selectedDate().toString('dd/MM/yyyy')
        self.data = datetime.strptime(data,'%d/%m/%Y')
        self.data_hora.setDate(self.data)
        return self.data



    def fechar(self):
       self.close()


class Mensagem:

    def menss(self,title,text,icon,list_btn):

        mensag = QMessageBox()
        mensag.setWindowTitle(title)
        mensag.setText(text)
        mensag.setIcon(icon)
        mensag.setStyleSheet('QLabel{font-size: 20px;}')
        mensag.setStandardButtons(list_btn)
        return mensag



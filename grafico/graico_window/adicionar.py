import sys
import threading
from datetime import datetime, timedelta
from time import sleep

from PyQt5.QtWidgets import QMainWindow, QDialogButtonBox, QMessageBox, QApplication
import random
# from grafico.graico_window.utils import Calendario, arquivo
# from grafico.window_PY.design_adicionar import Ui_mainWindow
# from processamento_dados.ajusta_lista import adicionar_tarefa
# from processa_arquivo.gerencia_arquivo import abrir_lista_arquivo
from projeto_Agenda.grafico.graico_window.atualizar import arquivo
from projeto_Agenda.grafico.graico_window.utils import Calendario
from projeto_Agenda.grafico.window_PY.design_adicionar import Ui_mainWindow
from projeto_Agenda.processamento_dados.ajusta_lista import adicionar_tarefa


class Adicionar(QMainWindow, Ui_mainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.calendario_window = Calendario()
        self.calendario_window.btn_confirma.button(QDialogButtonBox.Ok).\
            clicked.connect(self.set_data)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.btn_ok)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancelar)
        self.pushButton.clicked.connect(self.calendario)

        self.set_data()
        self.impedimento = False
        self.spinBox.setMinimum(1)
        self.threads = threading.Thread(target=self.habilited)
        self.threads.start()




    def btn_ok(self):
            print(self.impedimento)
            if self.impedimento == True:
                return
            print('ok',self.calendario_window.ajusta_data())
            msg = self.lineEdit.text()
            if msg == '':
                QMessageBox.critical(self,'nome error', 'Não foi inserido o nome da tarefa.',
                                     QMessageBox.Ok, QMessageBox.Ok)
            else:
                data = self.dateTimeEdit.text()
                intervalo_check = self.checkBox.isChecked()
                intervalo_opcao = self.comboBox.currentText()
                intervalo_valor = self.spinBox.text()


                if not data < self.data_agora:

                    self.ops = adicionar_tarefa(arquivo, msg, data, intervalo_opcao, intervalo_valor, intervalo_check)
                    reply = QMessageBox.question(self, 'ADICIONAR MAIS', 'Adicionar outra tarefa ?',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

                    print()
                    if reply == QMessageBox.Yes:
                        print('salvou')
                        self.lineEdit.clear()
                        # self.btn_input

                    else:
                        self.cancelar()

                else:
                    QMessageBox.information(self, 'Data invalida', 'A data não pode ser inferior a atual !',
                                                 QMessageBox.Ok, QMessageBox.Ok)



    def habilited(self):
        sleep(1)
        calculo = 1

        while True:
            self.check = self.checkBox.isChecked()

            if self.check == True:
                self.label_5.setEnabled(True)
                self.comboBox.setEnabled(True)
                self.spinBox.setEnabled(True)

            else:
                self.label_5.setEnabled(False)
                self.comboBox.setEnabled(False)
                self.spinBox.setEnabled(False)






            # print('habilite', self.calendario_window.ajusta_data())


    def set_data(self):
        data_agora = datetime.now() #+ timedelta(days=1)
        self.data_agora = data_agora.strftime('%d/%m/%Y %H')
        data = datetime.strptime(self.data_agora, '%d/%m/%Y %H')
        data = data + timedelta(days=1)
        self.dateTimeEdit.setDateTime(data)
        data_calendario = self.calendario_window.ajusta_data()
        if data_agora.day != data_calendario.day:
            print('simmm',data_agora,'..',data_calendario)
            self.dateTimeEdit.setDateTime(data_calendario)


    def calendario(self):
        self.calendario_window.show()


    def cancelar(self):
        self.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    opcao = Adicionar()
    opcao.show()
    app.exec_()
print(__name__,'grafico_window/adicionar')
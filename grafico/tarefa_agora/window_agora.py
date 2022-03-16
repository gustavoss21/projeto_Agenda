import sys
import threading
from datetime import datetime
from time import sleep

from projeto_Agenda.grafico.tarefa_agora.verificar_agora import agora
from PyQt5.QtGui import QPixmap
from PyQt5 import sip
# from grafico.window_PY import opcoes
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFrame, QApplication

from projeto_Agenda.grafico.window_PY import opcoes


class ParaAgora(QMainWindow,opcoes.Ui_MainWindow):

    def __init__(self,tarefa, parent=None):
        self.tarefa = tarefa
        super().__init__(parent)
        super().setupUi(self)
        # self.mostrar()
        agora = threading.Thread(target=self.set_hora)
        agora.start()
        self.exec_amostral()

    def set_hora(self):

        while True:
            data = datetime.now().strftime('%H:%M:%S')
            # self.lab_hora.setText(data)
            sleep(1)

    def relogio(self):
            tarefa = self.tarefa

            self.separa = tarefa[0]

            date = datetime.strptime(f'{tarefa[1]}', '%Y-%m-%d %H:%M')

            date = date.strftime('%X')

            self.date = datetime.strptime(f'{date}','%X')

            agora_dat = datetime.now()

            if self.date.hour - datetime.now().hour <= 1:
                if self.date.hour == agora_dat.hour:
                    if self.date.minute < agora_dat.minute:
                        return

                    subt_min = self.date.minute - agora_dat.minute

                else:
                   subt_hor = self.date.hour - agora_dat.hour
                   if self.date.minute > agora_dat.minute:
                       # self.exec_amostral()
                       return

                   subt_min = (self.date.minute+60) - agora_dat.minute

                while True:
                   if subt_min >= 60:
                       subt_min -= 60
                       hora = datetime.now().hour + subt_hor
                       self.date = datetime.strptime(f'1900-01-01 {hora}:{subt_min}', '%Y-%m-%d %H:%M')
                       self.date = self.date.strftime('%X')
                       self.date = datetime.strptime(f'{self.date}', '%X')

                   else:
                       break

                relogio = threading.Thread(target=self.tempo)
                relogio.start()
            return True



    def tempo(self):
        date = self.date
        taref = self.separa
        # date = datetime.strptime(f'{date[1]}','%Y-%m-%d %H:%M')
        while True:
                agora = datetime.now()
                temp = datetime.strptime(f'{agora}', '%Y-%m-%d %H:%M:%S.%f')
                temp = temp.strftime('%X')
                temp = datetime.strptime(f'{temp}', '%X')
                dat = f'{date - temp}'
                print(dat)
                if f'{dat}' == '0:00:01':
                    return #self.nadaAgora()
                    break

                try:
                  dat = datetime.strptime(f'{dat}', '%X')

                except:
                    self.exec_amostral()
                    return
                self.mostrol = True
                dat = dat.strftime('%M:%S')

                if not sip.isdeleted(self.lab_tarefa):
                    self.lab_tarefa.setText(f'{taref}')
                    self.lab_dat.setText(f'{dat}')
                sleep(1)

    def exec_amostral(self):

        try:
            thred = threading.Thread(target=self.relogio)
            thred.start()

        except:
            return

    def nadaAgora(self):
        # self.label_5.clear()

        self.lab_tex_tarefa.deleteLater()
        self.lab_dat.deleteLater()
        self.lab_tex_tempo.deleteLater()

        self.lab_tex_opcao.deleteLater()
        self.lab_tex.setText('  nada para agora')
        # self.label.setFrameShape()
        qpixmap = QPixmap('vazio.ico')

        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.label_4.setMinimumWidth(300)
        self.lab_tarefa.setPixmap(qpixmap)
        self.frame_5.setVisible(False)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    dicio = agora()
    print(dicio)
    if not dicio == []:

        app = QApplication(sys.argv)
        agora = ParaAgora(*dicio)
        agora.show()
        app.exec_()
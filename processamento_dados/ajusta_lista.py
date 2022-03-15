# from grafico.graico_window.utils import gera_id
# from processa_arquivo.gerencia_arquivo import salvar_mudancas, abrir_lista_arquivo
from datetime import datetime,timedelta

from projeto_base.grafico.graico_window.utils import gera_id
from projeto_base.processa_arquivo.gerencia_arquivo import abrir_lista_arquivo, salvar_mudancas

opcao = ['LEMBRETE RAPIDO', 'COMPROMISSO DO DIA', 'ADICIONAR COMPROMISSO', 'EDITAR COMPROMISSO', 'ENCERRAR PROGAMA']
# from processa_arquivo.proc_arq import proc_arquivo

# arquivo = proc_arquivo('escreva.txt')


#############################
#se a tela estiver cheia colocar o para agora na tela


class ListaEditada:# ops_2 mostra a lista de tarefas
        def __init__(self,documento):
            self.lista_original = abrir_lista_arquivo(documento)
            self.lista = [x['dicionario'] for x in self.lista_original]


            self.data_agora = datetime.now().strftime('%Y-%m-%d')
            self.data_agora = datetime.strptime(self.data_agora,'%Y-%m-%d')

            self.lista_nova = []

            for contador, dicionario in enumerate(self.lista[:]):

                data_tarefa = datetime.strptime(dicionario['date'], '%Y-%m-%d %H:%M')
                if data_tarefa.month == self.data_agora.month:
                    if data_tarefa.day < self.data_agora.day:

                        if dicionario['checking'] == True:
                            intervalo_opcao = dicionario['intervalo_opcao']
                            intervalo_valor = dicionario['intervalo_valor']

                            if intervalo_opcao == 'day':
                                 print('atualizou data dia')
                                 data_tarefa = self.data_agora + timedelta(days=intervalo_valor)

                            if intervalo_opcao == 'month':
                                x=0
                                while True:
                                    x += 1
                                    data = data_tarefa + timedelta(days=x)
                                    if data.day == data_tarefa.day and data.month != data_tarefa.month:
                                        data_tarefa = data_tarefa
                                        break

                            if intervalo_opcao == 'weeks':
                                print('simm')


                            data = data_tarefa.strftime('%Y-%m-%d %H:%M')
                            self.lista[contador]['date'] = data
                            salvar_mudancas(documento,self.lista)
                            return
                        else:
                           self.lista_original[contador]['dicionario'] = dicionario
                           self.lista_nova.append(self.lista_original[contador])

        def tarefaAgora(self):
            lista_nova = []

            for contador,dicionario in enumerate(self.lista[:]):

                data_tarefa = datetime.strptime(dicionario['date'], '%Y-%m-%d %H:%M')
                data_tarefa = data_tarefa.strftime('%Y-%m-%d')
                data_tarefa = datetime.strptime(data_tarefa, '%Y-%m-%d')


                if data_tarefa.day == self.data_agora.day:

                        # if dicionario['checking'] == True:
                        #     intervalo = self.lista[contador]['intervalo']
                        #     data = self.data_agora + timedelta(days=intervalo)
                        #     data = data.strftime('%Y-%m-%d %H:%M')
                        #     self.lista[contador]['date'] = data
                        #
                        # else:

                          lista_nova.append(dicionario)

            # salvar_mudancas(arquivo, self.lista)

            lista_nova = sorted(lista_nova, key=lambda x: x['tarefa'])
            # print('123', self.lista[1]['dicionario']['tarefa'])
            lista = sorted(self.lista, key=lambda x: x['tarefa'])

            return lista_nova,lista

        def tarefaPassada(self):
            #teste se vai dar certo
            # lista_nova = sorted(self.lista_nova, key=lambda x: x['tarefa'])
            # dicio = {'lista_nova':lista_nova,'lista_original':self.lista_original}
            # return dicio
            return self.lista_nova


def adicionar_tarefa(arquivo, msg,data,opcao='',valor='',check=False):

        lista = abrir_lista_arquivo(arquivo)

        dicionario = {}
        id = gera_id()

        data = datetime.strptime(data,'%d/%m/%Y %H:%M')
        # intervalo = data.day - datetime.now().day
        data = data.strftime('%Y-%m-%d %H:%M')
        data_tarefa = data

        dicionario['date'] = data_tarefa

        # for c in lista:
        #            if msg == c['tarefa']:#''''nome já existente!'''
        #               return 'ja exites a tarefa'


        dicionario['tarefa'] = msg

        dicionario['checking'] = check

        if check == True:
            dicionario['intervalo_opcao'] = opcao
            dicionario['intervalo_valor'] = valor


        lista_dicionario = {'id': id, 'dicionario':dicionario}
        lista.append(lista_dicionario)
        salvar_mudancas(arquivo,lista)





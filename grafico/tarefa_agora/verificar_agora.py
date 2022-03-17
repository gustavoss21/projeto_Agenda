import os
from datetime import datetime,time
# from processamento_dados.ajusta_lista import ListaEditada
# from processa_arquivo.proc_arq import proc_arquivo
from projeto_Agenda.processa_arquivo.proc_arq import proc_arquivo
from projeto_Agenda.processamento_dados.ajusta_lista import ListaEditada

arquivo = proc_arquivo().todas_tarefa('escreva.txt')

lista = ListaEditada(arquivo)
lista = lista.tarefaAgora()[0]


def agora():

      nova_lista = []

      for dicionario in lista:
        data = dicionario['date']
        date = datetime.strptime(f'{data}', '%Y-%m-%d %H:%M')
        date = time(date.hour,date.minute)

        if f'{date}' == '00:00:00':
            date = time(23,59)

        agora_dat = datetime.now()
        agora_dat = agora_dat.time()
        print(date.hour - agora_dat.hour)
        if 0 <= date.hour - agora_dat.hour <= 1:
            print(date.hour)
            if date.hour == agora_dat.hour:
                print('aqui')
                nova_lista.append((dicionario['tarefa'], dicionario['date']))

            else:
                if date.minute < agora_dat.minute:
                    print('aqui1')
                    nova_lista.append([dicionario['tarefa'], dicionario['date']])
                else:

                    print('nao2')
      return nova_lista


if __name__ == '__main__':
   print(agora())




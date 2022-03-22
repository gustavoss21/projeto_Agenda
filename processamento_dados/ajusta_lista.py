from datetime import datetime,timedelta
import pymysql

class ListaEditada:# ops_2 mostra a lista de tarefas
        def __init__(self):
            self.lista = self.get_lista()
            self.data_agora = datetime.now().strftime('%Y-%m-%d')
            self.data_agora = datetime.strptime(self.data_agora, '%Y-%m-%d')

        def get_lista(self):
            # acessa o banco e coloca todas as tuplas dele em uma lista#
            lista = []
            conexao = pymysql.connect(host='127.0.0.1', user='root', database='tarefa', password='991465393gs')
            cursor = conexao.cursor()
            cursor.execute('select * from tarefa')
            for c in cursor.fetchall():
                lista.append(c)

            cursor.close()
            conexao.close()
            #############################################
            return lista

        def forlista(self, data_tarefa, tupla):
                print(data_tarefa.day)
                if data_tarefa.day < self.data_agora.day:
                    if tupla[3] == 1:  # verifica se a tarefa esta habilitado para atualizar data automaticamente
                        intervalo_opcao = tupla[4]
                        intervalo_valor = tupla[5]
                        print('este sera atualizado', tupla[0])
                        if intervalo_opcao == 'day':
                            print('atualizou data dia')
                            data_tarefa = self.data_agora + timedelta(days=intervalo_valor)

                        if intervalo_opcao == 'month':
                            x = 0
                            while True:
                                x += 1
                                data = data_tarefa + timedelta(days=x)
                                if data.day == data_tarefa.day and data.month != data_tarefa.month:
                                    data_tarefa = data_tarefa
                                    break

                        if intervalo_opcao == 'weeks':
                            data_tarefa = self.data_agora + timedelta(weeks=intervalo_valor)
                            print('simm')

                        data = data_tarefa.strftime('%Y-%m-%d %H:%M')
                        conexao = pymysql.connect(host='127.0.0.1', user='root', database='tarefa',
                                                  password='991465393gs')
                        cursor = conexao.cursor()
                        cursor.execute(f'UPDATE tarefa SET data="{data}" WHERE id_tarefa={tupla[0]}')
                        cursor.close()
                        conexao.close()
                    else:
                        self.lista_nova.append(tupla)

        def tarefaAgora(self):
            lista_nova = []
            for contador,dicionario in enumerate(self.lista[:]):
                data_tarefa = dicionario[2]
                # data_tarefa = datetime.strptime(dicionario[2], '%Y-%m-%d %H:%M')
                data_tarefa = data_tarefa.strftime('%Y-%m-%d')
                data_tarefa = datetime.strptime(data_tarefa, '%Y-%m-%d')
                if data_tarefa.day == self.data_agora.day:
                    lista_nova.append(dicionario)

            lista_nova = sorted(lista_nova, key=lambda x: x[1])
            return lista_nova

        def tarefaPassada(self):
            self.lista_nova = []
            for contador, tupla in enumerate(self.lista[:]):
                data_tarefa = tupla[2]
                if data_tarefa.month == self.data_agora.month:
                    self.forlista(data_tarefa,tupla)
                else:
                    if data_tarefa.month < self.data_agora.month:
                        self.forlista(data_tarefa, tupla)
            return self.lista_nova

def adicionar_tarefa(msg,data,intervalo_check,intervalo_opcao,intervalo_valor):
    conexao = pymysql.connect(host='127.0.0.1', user='root', database='tarefa', password='991465393gs')
    print(msg, data, intervalo_check, intervalo_opcao, intervalo_valor)
    cursor = conexao.cursor()
    if intervalo_check in 'false':
        cursor.execute(
            f'insert INTO tarefa values (default,"{msg}","{data}",{intervalo_check},null,null);')
    else:
        cursor.execute(
            f'insert INTO tarefa values (default,"{msg}","{data}",{intervalo_check},"{intervalo_opcao}",{intervalo_valor});')
    conexao.commit()
    cursor.close()
    conexao.close()
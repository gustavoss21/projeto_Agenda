from datetime import datetime
import json


#entra no arquivo(escreva.txt) e coloca todos os dados em uma lista
# from processa_arquivo.proc_arq import proc_arquivo
from projeto_Agenda.processa_arquivo.proc_arq import proc_arquivo


def abrir_lista_arquivo(arquivo):

    try:

       with open(arquivo, 'rt') as arq:
           lista = arq.readlines()
           list = []

       for dicio in lista[:]:
            dicionario = json.loads(dicio)
            list.append(dicionario)

    except :

          proc_arquivo().resultado(arquivo)
    else:
        return list


def salvar_mudancas(arquivo, lista=(), dicionary=()):
    """
    esta função é responsavel por salvar todos os dados gerados no arquivo,
    esses dados podem ser tanto uma lista como tambem um dicionario
    :param arquivo:
    :param lista: contem varios dicionario que sera salva no arquivo
    :param dicionary: contem as tarefas e outros dados
    :return:
    """
    #extrair_lista = abrir_lista_arquivo(arquivo)

    if lista:

        with open(arquivo, 'w+') as arqu:
                for dicionario in lista[:]:
                    dicio = json.dumps(dicionario)
                    print(dicio)
                    print()
                    arqu.write(dicio)
                    arqu.write('\n')
                return
    if dicionary:
         with open(arquivo, 'a+') as arqu:

              dicionary = json.dumps((dicionary))
              arqu.write(str(dicionary))
              arqu.write('\n')
              arqu.close()
              return


#apagar todos os dados requisitados
def apagar_tarefa(arquivo, list, selecionado):

    nova_lista = []
    # print('lista:',list)
    # print('selecionado,:',selecionado)

    for c in list:
        if not str(selecionado).upper() == str(c['dicionario']['tarefa']).upper():
            nova_lista.append(c)
    print(11111,'apagar tarefa')
    salvar_mudancas(arquivo,lista=nova_lista)

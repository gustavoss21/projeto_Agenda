import pymysql

def salvar_mudancas(lista=(),check=False):
    """
    esta função é responsavel por salvar todos os dados gerados no arquivo,
    esses dados podem ser tanto uma lista como tambem um dicionario
    :param arquivo:
    :param lista: contem varios dicionario que sera salva no arquivo
    :param dicionary: contem as tarefas e outros dados
    :return:
    """
    conexao = pymysql.connect(host='127.0.0.1', user='root', database='tarefa', password='991465393gs')
    cursor = conexao.cursor()
    if check:
        print(123,{lista[4]})
        cursor.execute(f'UPDATE tarefa SET NOME_TAREFA="{lista[1]}", DATA="{lista[2]}",CHECKING={lista[3]},'
                       f'INTERVALO_OPCAO = "{lista[4]}",INTERVALO_VALOR={lista[5]} WHERE ID_TAREFA={lista[0]}')
    else:
        cursor.execute(f'UPDATE tarefa SET NOME_TAREFA="{lista[1]}", DATA="{lista[2]}", INTERVALO_OPCAO=null,'
                       f' INTERVALO_VALOR=null WHERE ID_TAREFA={lista[0]}')

    #INTERVALO_OPCAO="null", INTERVALO_VALOR="null"
    conexao.commit()
    cursor.close()
    conexao.close()

#apagar todos os dados requisitados
def apagar_tarefa(selecionado):
    print('selecionado',selecionado)
    conexao = pymysql.connect(host='127.0.0.1', user='root', database='tarefa', password='991465393gs')
    cursor = conexao.cursor()
    cursor.execute(f'delete from tarefa WHERE id_tarefa={selecionado}')
    conexao.commit()
    cursor.close()
    conexao.close()
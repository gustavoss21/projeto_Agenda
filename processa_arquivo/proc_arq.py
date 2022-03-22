import os
arquivo = 'escreva.txt'
caminho = os.path.abspath(arquivo)
caminho = caminho.partition(arquivo)
print(caminho)

# class proc_arquivo:
#
#
#     def resultado(self):
#
#         ficheiro = self.todas_tarefa(arquivo)
#         if not self.arquivo_existe():
#
#             self.criar_arquivo(ficheiro)
#
#
#         return ficheiro
#
#     def todas_tarefa(self,arquivo):
#         # caminho = os.path.abspath(arquivo)
#         # caminho = caminho.partition(arquivo)
#         # caminho = r'C:\Users\santo\PycharmProjects\meu_prejeto\processamento_dados'
#         print(caminho[0])
#         ficheiro = os.path.join(caminho[0], arquivo)
#
#         return ficheiro
#
#     def arquivo_existe(self):
#         try:
#             if arquivo:
#                 existe = open(arquivo, 'r+')
#                 existe.close()
#                 return existe
#         except:
#             return False
#
#
#     def criar_arquivo(self,arquivo,atualizar=False,dados=''):
#
#         if atualizar:
#             with open(arquivo, 'w+') as lista:
#                lista.write(dados)
#
#         with open(arquivo, 'w+') as lista:
#              ...
#
#         return lista

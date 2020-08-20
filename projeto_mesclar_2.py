import openpyxl
from openpyxl import Workbook
import os
from openpyxl.worksheet.worksheet import Worksheet as ws

planilha_vazao = openpyxl.Workbook()

try:
    diretorio = input('cole o diretorio do arquivo\n')

    lista_dir = os.listdir(diretorio)

    for file in lista_dir:
        arquivo_txt = open(diretorio+os.sep+ f'{file}','r+')
        
        for linha in arquivo_txt:
            linha_arquivo = linha.replace(',','.')
            lista_linha = linha_arquivo.split(';')

            lista_do_arquivo = [float(lista_linha[4]),float(lista_linha[5])]
            print(lista_do_arquivo)

            planilha_vazao.active.append(lista_do_arquivo)
        planilha_vazao.active.append(['***'])

    planilha_vazao.save('planilha_resultados.xlsx')

except FileNotFoundError:
    print('Abra o arquivo novamente e digite um diretório válido')

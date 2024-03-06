import camelot
from IPython.display import display
from time import time

pdf_links = [
    'https://www.gov.br/anvisa/pt-br/setorregulado/regularizacao/medicamentos/medicamentos-de-referencia/arquivos/lista-a-incluidos-050124.pdf',
    'https://www.gov.br/anvisa/pt-br/setorregulado/regularizacao/medicamentos/medicamentos-de-referencia/arquivos/lista-a-excluidos-050124.pdf',
    'https://www.gov.br/anvisa/pt-br/setorregulado/regularizacao/medicamentos/medicamentos-de-referencia/arquivos/lista-b-incluidos-050124.pdf',
    'https://www.gov.br/anvisa/pt-br/setorregulado/regularizacao/medicamentos/medicamentos-de-referencia/arquivos/lista-b-excluidos-050124.pdf'
]

# while True:
#     try:
#         op = int(input('Escolha uma opção:\n[0] - Inativos\n[1] - Ativos\n->'))

#         if op == 0 or op == 1:
#             if op == 0:
#                 link_pdf = 'https://www.gov.br/anvisa/pt-br/setorregulado/regularizacao/medicamentos/medicamentos-de-referencia/arquivos/lista-a-excluidos-050124.pdf'
#             else:
#                 link_pdf = 'https://www.gov.br/anvisa/pt-br/setorregulado/regularizacao/medicamentos/medicamentos-de-referencia/arquivos/lista-a-incluidos-050124.pdf'
#             break
#         else:
#             print('Opção inválida, escolha outra')
#     except:
#         print('Opção inválida, escolha outra')

def filterTable(temp_table):
    for row in range(0, len(temp_table.df)):
        if temp_table.df.at[row, 3] != '' and '/' not in temp_table.df.at[row, 3]:
            for col in range(0, len(temp_table.df.columns)):
                if temp_table.df.at[row, col] == '':
                    # print(f'{temp_table.df.at[row-1, col]} {temp_table.df.at[row+1, col]}')
                    temp_table.df.at[row,col] = f'{temp_table.df.at[row-1, col]} {temp_table.df.at[row+1, col]}'

    for row in range(0, len(temp_table.df)):
        if temp_table.df.at[row, 3] == '' or '/' in temp_table.df.at[row, 3]:
            temp_table.df = temp_table.df.drop(index=row)
        
    temp_table.df = temp_table.df.reset_index(drop=True)
    
    return temp_table

def filterTable2(temp_table):
    for row in range(0, len(temp_table.df)):
        if temp_table.df.at[row, 3] == '':
            for col in range(0, len(temp_table.df.columns)):
                if temp_table.df.at[row, col] != '':
                    newData = list()
                    rw = 1
                    while True:
                        if temp_table.df.at[row+rw, 3] == '':
                            rw += 1
                        else:
                            break
                    for temp_row in range(0, rw+rw+1):
                        newData.append(temp_table.df.at[temp_row, col])
                        temp_table.df.at[temp_row, col] = ''
                    
                    print(' '.join(newData))
                    temp_table.df.at[row+rw, col] = ' '.join(newData)
    
    return temp_table


def getDatas(ntable):
    link_pdf = pdf_links[ntable]
    tables = camelot.read_pdf(link_pdf, flavor='stream', pages='all', flag='text')
    
    npg = 0

    for pg in range(0, len(tables)):
        if npg == 10:
            a = input('\nEnter para continuar')
            npg = 0
        
        print('\n\n')
        print('='*100)
        print(f'pag: {pg}')
        print('\n\n')
        
        table = tables[pg]

        if pg == 0:
            match ntable:
                case 0:
                    table.df = table.df[2:].reset_index(drop=True)
                case 1:
                    table.df = table.df[4:].reset_index(drop=True)
                case 3:
                    table.df = table.df[4:].reset_index(drop=True)

        # table = filterTable(table)

        display(table.df)

        npg += 1


getDatas(3) #usando a tabela validos A





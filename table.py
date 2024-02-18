import camelot
from IPython.display import display
from time import time

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

link_pdf = 'https://www.gov.br/anvisa/pt-br/setorregulado/regularizacao/medicamentos/medicamentos-de-referencia/arquivos/lista-a-incluidos-050124.pdf'

temp_init = time()

tables = camelot.read_pdf(link_pdf, flavor='stream', pages='all', flag='text')

npg = 0

for pg in range(0, len(tables)):
    if npg == 10:
        a = input('Enter para continuar')
        npg = 0
    
    print('\n\n')
    print('='*100)
    print(f'pag: {pg}')
    print('='*100, end='\n\n')
    
    table = tables[pg]

    if pg == 0:
        table.df = table.df[2:].reset_index(drop=True)


    col = 1
    for row in range(0, len(table.df)):
        if len(table.df.at[row, col]) == 0:
            print(f'{table.df.at[row-1, col]} {table.df.at[row+1, col]}')
            table.df.at[row, col] = f'{table.df.at[row-1, col]} {table.df.at[row+1, col]}'

    display(table.df)

    npg += 1


temp_exec = time() - temp_init
print(f'\n\nTempo de execução: {temp_exec:.5f}s')

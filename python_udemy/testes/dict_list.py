tudao = {}
valores = []
qtdColuna = int(input('DIGITE O NÚMERO DE COLUNAS DA SUA TABELA: '))
qtdLinha = int(input('DIGITE O NÚMERO DE LINHAS DA SUA TABELA: '))


for coluna in range(qtdColuna):
    repetido = False
    while repetido:
        nome_coluna = (input('DIGITE O NOME DA COLUNA: '))
        if nome_coluna not in tudao:
            for valor_coluna in range(qtdLinha):
                valores.append(input('DIGITE O VALOR DA COLUNA: '))
            tudao.update({nome_coluna: valores})
            valores = []
            repetido = False
        else:
            print('Nome da coluna repetido.')
            nome_coluna = ''
            repetido = True

print(f'Lista completa: {tudao}')
print(f'Colunas: {list(tudao.keys())}')
print(f'Valores: {list(tudao.values())}')




# This Python file uses the following encoding: utf-8

import csv


def escrever(data, nome, produto, valor):

    dados = ler_arquivo()

    with open('teste.CSV', 'w', newline='') as arquivo:
        escreve = csv.writer(
            arquivo,
            delimiter=',',
            quoting=csv.QUOTE_ALL

        )
        if not dados:
            escreve.writerow(
                [
                    'Data',
                    'Nome',
                    'Produto',
                    'Valor',
                ]
            )
        else:
            chaves = dados[0].keys()
            chaves = list(chaves)
            escreve.writerow(
                [
                    chaves[0],
                    chaves[1],
                    chaves[2],
                    chaves[3]
                ]
            )
        for dado in dados:
            escreve.writerow(
                [
                    dado['Data'],
                    dado['Nome'],
                    dado['Produto'],
                    dado['Valor']
                ]
            )
        escreve.writerow(
            [
                data,
                nome,
                produto,
                valor
            ]
        )


def ler_arquivo():
    with open('teste.CSV', 'r', newline='') as arquivo:
        dados = [x for x in csv.DictReader(arquivo)]
    return dados


def limpar_arquivo():
    senha = input('Senha: ')
    if senha == '123456':
        with open('teste.CSV', 'w', newline='') as arquivo:
            escreve = csv.writer(
                arquivo,
                delimiter=',',
                quoting=csv.QUOTE_ALL
            )
            escreve.writerow([])
    else:
        print('Senha incorreta. Acesso negado.')


escrever('08/06/2022', 'Shirlei', 'Blusa', '39.90')
limpar_arquivo()


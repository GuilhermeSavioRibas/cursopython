import re
import requests
import json


def atualizar():
        requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        cotacao = json.loads(requisicao.text)
        print()
        print('-' * 25)
        print(f'{cotacao["USDBRL"]["create_date"]}')
        print('-' * 25)
        print(f'USD: {cotacao["USDBRL"]["high"]} - {cotacao["USDBRL"]["low"]} \n')
        print(f'EUR: {cotacao["EURBRL"]["high"]} - {cotacao["EURBRL"]["low"]} \n')
        print(f'BTC: {cotacao["BTCBRL"]["high"]} - {cotacao["BTCBRL"]["low"]}')
        print('-' * 25)


atualizar()
while True:
    print('Atualizar --- [A] \nSair -------- [S]')
    resp = input('>> ').upper()[0]
    if resp in 'AS':
        if resp == 'A':
            atualizar()
        else:
            exit()
    else:
        print('Opção invalida!')
        continue

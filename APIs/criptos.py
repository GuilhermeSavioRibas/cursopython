import re
import requests
import json

print()
bitcoin = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/')
cotacao_bitcoin = json.loads(bitcoin.text)
print('BTC')
print(f'High: {float(cotacao_bitcoin["ticker"]["high"]):.2f}')
print(f'Low: {float(cotacao_bitcoin["ticker"]["low"]):.2f}')
print()
ethereum = requests.get('https://www.mercadobitcoin.net/api/ETH/ticker/')
cotacao_ethereum = json.loads(ethereum.text)
print('ETH')
print(f'High: {float(cotacao_ethereum["ticker"]["high"]):.2f}')
print(f'Low: {float(cotacao_ethereum["ticker"]["low"]):.2f}')

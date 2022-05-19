import re
import requests
import json

#  cidade = input('Cidade: ')
cidade = 'Campo Grande'
requisicao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=6aad23efb5e2466e8d3dc3ec78b764d1')
requisicao2 = requests.get('https://atlas.microsoft.com/weather/currentConditions/json?api-version=1.1&query=47.641268,-122.125679')
clima = json.loads(requisicao.text)
clima2 = json.loads(requisicao2.text)

print('-=-'*10)
print(f'Cidade: {clima["name"]}')
print(f'Condição: {clima["weather"][0]["description"]}')
print(f'Temperatura: {float(clima["main"]["temp"]) - 273.15:.2f} ªC')
print('-=-'*10)


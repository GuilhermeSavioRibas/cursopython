import re
import requests
import json

print()
requisicao = requests.get('https://api.adviceslip.com/advice')
conselhos = json.loads(requisicao.text)
conselho = conselhos['slip']['advice']

print(conselho)

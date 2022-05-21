import re
import requests
import json

# imagem do dia
requisicao_apod = requests.get('https://api.nasa.gov/planetary/apod?api_key=2f8mxhxiDehuaPd0pdKcrbqTL3FImUJLVi0VRQxo')
picture_of_the_day = json.loads(requisicao_apod.text)

# asteróides
# neo = json.loads(requisicao_neo.text)

#  imagem da Terra
# requisicao_earth = requests.get('https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01'
#                                 '&api_key=2f8mxhxiDehuaPd0pdKcrbqTL3FImUJLVi0VRQxo')
# print(requisicao_earth.text)


print(picture_of_the_day)
# print(neo)
# print(earth)

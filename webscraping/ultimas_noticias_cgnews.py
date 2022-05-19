# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

cgnews = 'https://www.campograndenews.com.br/ultimas-noticias'
midiamax = 'https://midiamax.uol.com.br/ultimas-noticias/'
response1 = requests.get(cgnews)
response2 = requests.get(midiamax)
html1 = BeautifulSoup(response1.text, 'html.parser')
html2 = BeautifulSoup(response2.text, 'html.parser')
# print(html.prettify())
# print(html.title.string)
# print(html.p.string)
# print(html.find_all('a'))
# print(html.find(id="id_example"))
# print(html.get_text())


# midiamax
print('Últimas notícias - midiamax')
for resumos in html2.select('.elementor-post__text'):
    titulo = resumos.h2
    texto = resumos.select_one('.elementor-post__excerpt')
    data = resumos.select_one('.elementor-post-date')
    hora = resumos.select_one('.elementor-post-time')
    link = resumos.h2.a
    print(f'{data.text}', end='')
    print(f'{hora.text}', end='')
    print(titulo.text)
    print(texto.text)
    print(link.get('href'))
    print('-=' * 60)

# cgnews
print()
print('Últimas notícias - cgnews')
print()
for resumos in html1.select('.col-12.col-md'):
    titulo = resumos.select_one('h2 > a')
    data = resumos.select_one('.Data')
    link = resumos.select_one('.btn.btn-link.btn-sm')
    print(data.text)
    print(titulo.text)
    print(link.get('href'))
    print('-='*60)


#  mostra o texto da noticia
#
#     noticia = requests.get(link.get('href'))
#     html3 = BeautifulSoup(noticia.text, 'html.parser')
#     for x in html3.select('.Texto.clearfix.bg-content-transp'):
#         print(x.text)
#         print()

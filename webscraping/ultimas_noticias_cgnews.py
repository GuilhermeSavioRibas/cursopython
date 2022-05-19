# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'https://www.campograndenews.com.br/ultimas-noticias'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
# print(html.prettify())
# print(html.title.string)
# print(html.p.string)
# print(html.find_all('a'))
# print(html.find(id="id_example"))
# print(html.get_text())

for resumos in html.select('.col-12.col-md'):
    titulo = resumos.select_one('h2 > a')
    data = resumos.select_one('.Data')
    link = resumos.select_one('.btn.btn-link.btn-sm')
    print(data.text)
    print(titulo.text)
    print(link.get('href'))
    print()
    # noticia = requests.get(link.get('href'))
    # html2 = BeautifulSoup(noticia.text, 'html.parser')
    # for x in html2.select('.Texto.clearfix.bg-content-transp'):
    #     print(x.text)
    #     print()

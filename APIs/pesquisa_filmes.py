import requests
import json


def lista_filmes(titulo):
    lista = []
    for i in range(1, 101):
        try:
            req = requests.get('http://www.omdbapi.com/?apikey=eb3dc56d&s=' + titulo + '&type=movie&page=' + str(i))
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    poster = filme['Poster']
                    string = tit + ' (' + ano + ')' + poster
                    lista.append(string)
            else:
                break
        except:
            print('Erro na conexao')
    return lista


sair = False
while not sair:
    op = input('Pesquise por um filme ou digite sair: ').upper()
    if op == 'SAIR':
        print('Saindo...')
        sair = True
    else:
        lista_de_filmes = lista_filmes(op)
        for filme in lista_de_filmes:
            print(filme)
        print('Filmes encontrados: ', len(lista_de_filmes))
    print()
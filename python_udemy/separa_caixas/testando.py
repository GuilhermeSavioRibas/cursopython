class Caixa:
    def __init__(self, ident, loc):
        self.ident = ident
        self.loc = loc
        self.items = []

    def cadastra_items(self, referencia, cor, tamanho):
        self.items.append(Item(referencia, cor, tamanho))

    def lista_items(self):
        for item in self.items:
            print(item.referencia, item.cor, item.tamanho)

    def procura_item(self):
        ref = input('referencia: ')
        cor = input('cor: ')
        tam = input('tamanho: ')
        for item in self.items:
            if item.referencia == ref and item.cor == cor and item.tamanho == tam:
                print(f'Caixa {self.ident}')
                print(f'Localização: {self.loc}')
                print(f'Item: {item.referencia}, {item.cor}, {item.tamanho}')


class Item:
    def __init__(self, referencia, cor, tamanho):
        self.referencia = referencia
        self.cor = cor
        self.tamanho = tamanho

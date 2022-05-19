def cadastrar():
    try:
        produto = str(input('Produto: '))
        preco = str(input('Preço: ')).replace(',', '.')
        carrinho.append((produto, float(preco)))
    except:
        print('Erro')


carrinho = list()
resp = 'S'
while resp == 'S':
    cadastrar()
    resp = str(input('Cadastrar? S/N: ')).upper()[0]
    if resp == 'S':
        total = sum([float(y) for x, y in carrinho])
        print(f'Total: {total}')
        continue
    elif resp == 'N':
        total = sum([float(y) for x, y in carrinho])
        print(f'Total: {total}')
        exit()
    else:
        print('Erro. Digite S ou N')
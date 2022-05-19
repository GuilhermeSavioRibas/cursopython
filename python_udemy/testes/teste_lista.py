lista = [1, 4, 1, 4, 'b', 1, 4, 'b', 3, 3, 3, 4, 5, 6, 6, 5, 2, 1, 'a', 'c']
repetidos = []
while True:

    val = input('Buscar: ').lower()
    for k, v in enumerate(lista):
        v = str(v)
        if val == v:
            if v not in repetidos:
                repetidos.append(v)
            print(f'{k}, ', end='')
    if val not in str(lista):
        print('Valor não foi encontrado na lista.')
    print()
    print(f'Repetidos: {repetidos}')

    resp = str(input('Chega? [S/N] ')).upper()[0]
    if resp == 'N':
        continue
    elif resp == 'S':
        break
    else:
        print('Opção errada')
        continue

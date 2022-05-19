from testando import Caixa

while True:
    print()
    op = int(input('1 - Cadastrar caixa\n2 - Cadastrar item\n3 - Procurar Item'))
    if op == 1:
        caixa_id = int(input('ID: '))
        loc = str(input('Loc: '))
        caixa1 = Caixa(caixa_id, loc)
        print(caixa1.ident, caixa1.loc)






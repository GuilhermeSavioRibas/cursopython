# for a, b in enumerate(range(10, 1, -1)):
#     print(a, b)
while True:
    try:
        cpf = input('Digite o CPF: ')
        cpf = cpf.replace('.', '').replace('-', '')
        m = 10
        c = 11
        soma = 0
        soma2 = 0
        for i, n in enumerate(cpf):
            if i < 9:
                soma += int(n) * m
                m -= 1
        x = 11 - (soma % 11)
        if x > 9:
            digito1 = 0
        else:
            digito1 = x
        for i, n in enumerate(cpf):
            if i < 10:
                soma2 += int(n) * c
                c -= 1
        y = 11 - (soma2 % 11)
        if y == 9:
            digito2 = 9
        else:
            digito2 = y
        novo_cpf = cpf[:9] + str(digito1) + str(digito2)
        sequencia = novo_cpf == str(novo_cpf[0]) * 11
        if novo_cpf == cpf and not sequencia:
            print('Válido')
        else:
            print('Invalido')
            print(novo_cpf)
    except:
        print('ERRO" Valores digitados não podem ser computados.')
        continue

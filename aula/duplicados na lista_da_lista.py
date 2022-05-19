from random import choices


listona = []
for n in range(0, 10):
    listona.append(choices(range(1, 11), k=10))


def duplicados(param_lista):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in param_lista:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)
    return primeiro_duplicado


for lista in listona:
    print(lista, duplicados(lista))




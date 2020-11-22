
def simbola(lista, tip):
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if tip == 'cod':
        for i in range(len(lista)):
            if lista[i] > 9:
                lista[i] = base[ lista[i]-10 ]

    elif tip == 'decod':
        for i in range(len(lista)):
            if lista[i] in base:
                lista[i] = base.index(lista[i]) + 10

    print(lista)
    return lista

simbola(['A', 'A'], 'decod')
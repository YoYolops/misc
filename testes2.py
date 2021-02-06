from random import sample


def mega_sena(q):
    for i in range(1, q + 1):
        yield sorted(sample(range(1, 61), 6))


quant = int(input('Quantidade de palpites: '))

for j in mega_sena(quant):
    for k in j:
        print(f'{k:02}', end=' ')
    print()
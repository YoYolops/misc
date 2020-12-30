def gNota(lista):
    peso = 5
    soma = 0
    div = 0

    for i in lista:
        soma += i*peso
        div += i 

        peso -= 1

    saida = soma/div

    print(f'a nota é: {saida}')

while True:
    val = input().split()

    nval = []
    for i in val:
        nval.append(int(i))

    gNota(nval)

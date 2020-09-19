resultado = []

#função que inverte a lista para apresentar o resultado em ordem correta
def inversor(lista):
    resposta = []
    tam = len(lista) - 1

    while tam >= 0:
        resposta.append(lista[tam])
        tam -= 1

    return resposta


# Conversor de Decimal para Binário:
def DecBin(decimal):
    while decimal > 1:
        add = decimal % 2
        resultado.append(add)
        decimal = int(decimal/2)
    resultado.append(1)
    saida = inversor(resultado)
    print(saida)

DecBin(int(input()))

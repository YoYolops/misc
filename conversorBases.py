
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
    resultado = []

    while decimal > 1:
        add = decimal % 2
        resultado.append(add)
        decimal = int(decimal/2)

    resultado.append(1)
    saida = inversor(resultado)

    print(saida)

# Conversor de Decimal para Octal: (usa conversão nativa do python)
def DecOct(decimal):
    print('O resultado é: %o'%decimal)

# Conversor de Decimal para Octal: (usa conversão nativa do python)
def DecHex(decimal):
    print('O resultado é: %x'%decimal)


conversores = {

    'decimal':{
        'binario': DecBin,
        'octal': DecOct,
        'hexadecimal': DecHex
    }

}

print(
    """ Este é um conversor de bases.

    Instruções:
    Digite no terminal a base do número que será convertido,
    por escrito, seguido da base do número para o qual se
    quer converter, também por escrito.
    
    Exemplo:
    Para converter um numero de decimal para binário digite:
    > $ decimal binario"""
)

while True:
    
    partida, chegada = input().split()

    if partida not in conversores or chegada not in conversores[partida]:
        print('Desculpe, não entendemos o que você quer')
    else:
        conversores[partida][chegada](int(input('Insira o número a ser transformado: ')))



    



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

    print('----BINÁRIO:----')
    print(saida)
    return saida

# Conversor de Decimal para Octal: (usa conversão nativa do python)
def DecOct(decimal):
    print('OCTAL: %o'%decimal)

    resultado = []

    while decimal > 7:
        add = decimal % 8
        resultado.append(add)
        decimal = int(decimal/8)

    resultado.append(decimal)
    saida = inversor(resultado)

    return saida

# Conversor de Decimal para Octal: (usa conversão nativa do python)
def DecHex(decimal):
    print('HEXADECIMAL: %x'%decimal)

    resultado = []

    while decimal > 15:
        add = decimal % 16
        resultado.append(add)
        decimal = int(decimal/16)

    resultado.append(decimal)
    saida = inversor(resultado)

    for i in range(len(saida)):
        if saida[i] > 9:
            if saida[i] == 10:
                saida[i] = 'A'
            elif saida[i] == 11:
                saida[i] = 'B'
            elif saida[i] == 12:
                saida[i] = 'C'
            elif saida[i] == 13:
                saida[i] = 'D'
            elif saida[i] == 14:
                saida[i] = 'E'
            elif saida[i] == 15:
                saida[i] = 'F'

    return saida

def BinDec(bin):
    manipulacao = []
    stringbin = str(bin)

    for i in stringbin:
        manipulacao.append(int(i))

    ctrl = len(manipulacao) - 1
    pot = 0
    while ctrl >= 0:
        manipulacao[ctrl] = manipulacao[ctrl] * (2**pot)
        pot += 1
        ctrl -= 1
    
    saida = 0
    for i in manipulacao:
        saida = saida + i

    print('----DECIMAL:----')
    print(saida)
    return saida
        
def OctDec(oct):
    manipulacao = []

    stringoct = str(oct)

    for i in stringoct:
        manipulacao.append(int(i))

    ctrl = len(manipulacao) - 1
    pot = 0
    while ctrl >= 0:
        manipulacao[ctrl] = manipulacao[ctrl] * (8**pot)
        pot += 1
        ctrl -= 1
    
    saida = 0
    for i in manipulacao:
        saida = saida + i
    
    print('----DECIMAL:----')
    print(saida)
    return saida

def HexDec(hex):
    manipulacao = []

    stringhex = str(hex)

    for i in stringhex:
        manipulacao.append(i)

    for i in range(len(manipulacao)):
        if manipulacao[i] in ['a', 'A']:
            manipulacao[i] = 10
        elif manipulacao[i] in ['b', 'B']:
            manipulacao[i] = 11
        elif manipulacao[i] in ['c', 'C']:
            manipulacao[i] = 12
        elif manipulacao[i] in ['d', 'D']:
            manipulacao[i] = 13
        elif manipulacao[i] in ['e', 'E']:
            manipulacao[i] = 14
        elif manipulacao[i] in ['f', 'F']:
            manipulacao[i] = 15
        else:
            manipulacao[i] = int(manipulacao[i])

    ctrl = len(manipulacao) - 1
    pot = 0
    while ctrl >= 0:
        manipulacao[ctrl] = manipulacao[ctrl] * (16**pot)
        pot += 1
        ctrl -= 1
    
    saida = 0
    for i in manipulacao:
        saida = saida + i
    
    print('----DECIMAL:----')
    print(saida)
    return saida

conversores = {

    'decimal':{
        'binario': DecBin,
        'octal': DecOct,
        'hexadecimal': DecHex
    },

    'binario':BinDec,
    'octal':OctDec,
    'hexadecimal':HexDec

}

print(
    """ Conversor yoyo, v1.0.1.

    INSTRUÇÕES:

    Digite no terminal a base do número que será convertido,
    por escrito, seguida da base do número para o qual se
    quer converter, também por escrito.

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    Exemplo:

    Para converter um numero de decimal para binário digite:
    > $ decimal binario
    
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    BASES SUPORTADAS:

    - Binária
    - Octal
    - Decimal
    - Hexadecimal

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
"""
)

while True:
    print('insira as bases de partida e chegada: ')
    partida, chegada = input().split()


    if partida != 'decimal' and chegada == 'decimal':
        conversores[partida](int(input('Insira o número a ser transformado: ')))

    elif partida != 'decimal' and chegada != 'decimal':
        a = conversores[partida](input('Insira o número a ser transformado: '))
        conversores['decimal'][chegada](a)

    else:
        conversores[partida][chegada](int(input('Insira o número a ser transformado: ')))



    


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
    
    total = 0
    for i in manipulacao:
        total = total + i
    
    print(total)
    return total
# {'posCelula':posCelula, 'dimX':quantX, 'dimY':quantY}

#regras: 
#   quaisquer celulas com menos de 2 vizinhos, morre OK
#   quaisquer celulas com 2 ou 3 vizinhos vive na proxima geração
#   quaisquer celulas com mais de 3 vizinhos, morre OK
#   quaisquer casas com 3 vizinhos vivos, torna-se viva na próxima geração

#Essa função verifica se as celulas existentes morrem ou vivem e
#retorna um array de arrays que representam as coordenadas das novas células


def killer(dados):
    x = dados['dimx']
    y = dados['dimy']

    celulasEmProvacao = list(dados['posCelula'])
    cacheCelulasVivas = list(dados['posCelula'])

    def isValid(coords, x, y):
        #Se as duas ultimas condições abaixo forem retiradas, o programa vai continuar calculando o ciclo de vida 
        # das celulas que passam da borda do mapa, mesmo que elas não estejam sendo mostradas, o que pode gerar problemas de 
        # performance, Caso as condições estejam ativas, o programa considera as celulas que cruzam a borda como celulas mortas
        if coords[0] < 1 or coords[1] < 1 or coords[0] > x or coords[1] > y: 
            return False
        return True

    def counter(casa, _cacheCelulasVivas):

        vizinhos = [
            [ casa[0] + 1, casa[1] ],
            [ casa[0] - 1, casa[1] ],
            [ casa[0], casa[1] + 1 ],
            [ casa[0], casa[1] - 1 ],
            [ casa[0] + 1, casa[1] + 1 ],
            [ casa[0] - 1, casa[1] - 1 ],
            [ casa[0] + 1, casa[1] - 1 ],
            [ casa[0] - 1, casa[1] + 1 ] 
        ]

        casasProsperas = []
        celulasQueDevemMorrer = []
        cont = 0

        for i in vizinhos:
            if isValid(i, x, y) and i not in _cacheCelulasVivas:
                casasProsperas.append(i)
            elif isValid(i, x, y) and i in _cacheCelulasVivas:
                cont += 1

        retorno = {
            'casasProsperas': casasProsperas,
            'quantidadeCelulasVivasAoRedor': cont
        }

        return retorno

    celulasSobreviventes = []
    casasQuePodemGerarVida = []
    for i in celulasEmProvacao:
        resultado = counter(i, cacheCelulasVivas)

        for casa in resultado['casasProsperas']:
            if casa not in casasQuePodemGerarVida:
                casasQuePodemGerarVida.append(casa)

        if resultado['quantidadeCelulasVivasAoRedor'] == 2 or resultado['quantidadeCelulasVivasAoRedor'] == 3:
            celulasSobreviventes.append(i)

    retornoFinal = {
        'vizinhos': casasQuePodemGerarVida,
        'posCelulaFututo': celulasSobreviventes,
        'posCelula': cacheCelulasVivas
    }

    return retornoFinal






#pra cada celula, verificar as casas ao redor
#retirar posiçoes invalidas (coordenadas menores que 1)
#a quantidade de posicoes validas é o num de vizinhos
#decidir se a celula vive ou morre
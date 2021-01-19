from killer import killer
from liver import liver
from tableConstructor import setScenario
from time import sleep

def runner(larguraX, alturaY, celulasVivas):

    x = larguraX
    y = alturaY

    while True:
        out = setScenario(y, x, celulasVivas)
        out = killer(out)
        celulasVivas = liver(out)
        print("\x1b[2J\x1b[1;1H", end="")
        sleep(0.2)

oscilator = [
    [2,2],
    [1,2],
    [3,2]
]

glider = [
    [3,2],
    [4,3],
    [2,4],
    [3,4],
    [4,4]
]

tetrisIni = [
    [2,1],
    [2,2],
    [2,3],
    [1,2]
]

tetrisCent = [
    [7,6],
    [7,7],
    [7,8],
    [6,7]
]

runner(60, 24, tetrisCent)


def counter(casa, vizinhosRelevantes):

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

    for i in vizinhos

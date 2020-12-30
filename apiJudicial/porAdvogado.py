
import json
import requests

def pesquisa_advogado():

    jasons = []

    numero_oab = input('Insira o Número da OAB: ')
    letra = input('Insira a letra (se não tiver, pressione enter): ')
    uf = input('Insira o UF: ')

    headers = {
        'host': 'esb.tjpb.jus.br',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'connection': 'keep-alive',
    }

    sendData = {
        'numOab': numero_oab,
        'letra': letra.upper(),
        'uf': uf.upper()
    }

    count = 9

    while count > 0:

        url = 'https://esb.tjpb.jus.br/cp-backend/sistemas/' + str(count) + '/processos?' + 'numeroOAB=' + sendData['numOab'] + sendData['letra'] + '&ufOAB=' + sendData['uf'] + '&offset=0&quantidade=10'

        paginaUm = requests.get(url, headers=headers)

        try:

            for i in paginaUm.json():
                print('='*40)
                print()
                print(f'Encontrados os seguintes dados no sistema {count}:')
                print()
                print(json.dumps(i, sort_keys=True, indent=4))
                jasons.append(i)
                

        except:
            print(f'nada no sistema {count}')

        count -= 1
        
    return jasons

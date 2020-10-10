# Este é um protótipo com finalidade de estudar o funcionamento
# de um chatbot e verificar a eficáia de soluções e técnicas

def mostraOpc(val):
    escolha = 'opc' + val

    print()
    if fluxo['nCam']:
        for i in fluxo[val][escolha]:
            print(i)
    else:
        print(fluxo[val])

    print()

def escavadora(val):
    return fluxo[val]

controle = 0
fluxo = {
    'nCam': True,
    '0': {
        'nCam': False,
        'opc0': [
            '0 - Pessoal',
            '1 - Bancário'
        ],

        '0': 'Qual Seu Nome? ',
        '1': 'Qual Seu CPF? '
    },
    
    '1':  {
        'nCam': False,
        'opc1': [
            '0 - atuais',
            '1 - atrasadas'
        ],

        '0': 'Em que mês estamos? ',
        '1': 'De que mês?'
    }
}

print('Selecione uma das opções: ')
print(
    """
    0 - Serviços
    1 - Faturas Abertas
    """
)

while True:

    param = input()

    mostraOpc(param)

    if fluxo['nCam']:
        fluxo = escavadora(param)

    
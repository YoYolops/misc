from porAdvogado import pesquisa_advogado
from porParte import pesquisa_parte
from porProcesso import pesquisa_processo

while True:

    operacao = {
        'a': pesquisa_parte,
        'b': pesquisa_advogado,
        'c': pesquisa_processo
    }

    opcao = input('''Digite:
    a - Para busca por nome da parte
    b - Para busca por Advogado
    c - Para busca por Nº do processo
    d - Para sair

    ''')

    if opcao == 'd':
        break
    else:
        operacao[opcao]()
    
    print()
    print('Fim da Busca')
    print()
entrada = ''

while entrada != EOF:
  try:
    #Recebo a entrada, e já a converto para minúsculo
    entradaParcial = input()
    entradaParcial = entradaParcial.lower()

    entrada += entradaParcial

    print(f'entrada total: {entrada}')
  except EOFError:
    break


#Tento remover todos os caracteres que não sejam letras. Aí está o PRINCIPAL erro do meu código, pois desta forma, sei que não consigo remover todos os caracteres desejados da string
S = entrada
for x in '0123456789+-*/[]{}().,?":~´`ªº!@#$%¨&_':
    S = S.replace(x, ' ')

#Armazeno cada "palavra" na lista, separando pelo o espaço vazio (' '), e ordeno a lista
L = S.split(' ')
L = sorted(set(L))

#Removo índices que estão vazios ('')
i = 0
while i < len(L):
    if L[i] == '':
        L.pop(i)
    i += 1

#Exibo o conteúdo de cada índice da lista, um por linha
j = 0
print('saida:')
while j < len(L):
    print(L[j])
    j += 1
print('fim de saida')
print()

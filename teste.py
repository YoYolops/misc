
# coletando o texto a ser analisado e criando uma lista onde cada palavra é um item
texto = input().split()

#criando uma espécie de contador para saber em que ponto está o for
index = 0
for palavra in texto:

    #para cada palavra do texto verifico se ela é composta somente por caracteres alfabéticos
    if not palavra.isalpha():
        #caso exista algum caractere não alfabético, crio uma lista onde cada item é uma letra, para poder analisar letra por letra
        print(f'a palavra {palavra} não é alpha')
        letras = list(palavra)
        print(f'suas letras são: {letras}')
        print()

        #c é um controle de index. vamos verificar quais dos caracteres não são letras e apagá-los
        c = 0
        while c < len(letras):
            print(f'estamos no index: {c}')

            if not letras[c].isalpha():
                print(f'a letra {letras[c]} não é alpha, eliminaremos {letras[c]}')
                letras.pop(c)
                print(f'eliminando-a temos a nova lista: {letras}')
                print()
            else:
                print(f'a letra {letras[c]} é alpha')
                print()
                c += 1

        #depois de retirar caracteres indesejados, vamos pegar o que sobrou e crair uma nova palavra
        novaPalavra = ''
        for i in letras:
            novaPalavra += i
        
        print(f'a nova palavra será: {novaPalavra}')
        print()
        #agora substituímos a antiga palavra da lista texto pela nova
        texto[index] = novaPalavra


    index += 1

#vamos agora adicionar tudo a uma nova lista que não tolera repetições
palavrasUnicas = []
print('vamos verificar se há palavras repetidas:')
for palavra in texto:
    if palavra.lower() not in palavrasUnicas:
        palavrasUnicas.append(palavra.lower())
    else:
        print(f'a palavra {palavra} já existe em: {palavrasUnicas}')
        print()

#organizamos em ordem alfabética
palavrasUnicas = sorted(palavrasUnicas)

#printamos cada palavra em uma linha
for palavra in palavrasUnicas:
    print(palavra)
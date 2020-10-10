def gerador_primos(n):
    li = 2
    numeros_primos = list()

    while li <= n:
        if primo(li):
            numeros_primos.append(li)

        li += 1

    return numeros_primos


def primo(m):
    i = 1
    cont = 0

    while i <= m:
        if m % i == 0:
            cont += 1

        i += 1
        
    if cont > 2:
        return False
    else:
        return True


num = int(input('Digite um número inteiro: '))

print(f'\033[32mOs números primos entre "2" e "{num}" são:\n{gerador_primos(num)}')
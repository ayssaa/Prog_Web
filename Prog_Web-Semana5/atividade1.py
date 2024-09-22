# Problema 1
# Entrada: Uma lista númerica
print('Bem vindo(a) ao programa de funções com listas!\n')
qnt_num = int(input('\nDigite a quantidade de números: '))
lista_input = []
for i in range(qnt_num):
    num = int(input('\nDigite o número: '))
    lista_input.append(num)


# Criando minhas  funções
def somatoria(lista):
    somatorio = 0
    for i in lista:
        somatorio += i
    return somatorio


def par(lista):
    contador_pares = 0
    for i in lista:
        if i % 2 == 0:
            contador_pares += 1
    return contador_pares


def impar(lista):
    contador_impares = 0
    for i in lista:
        if i % 2 != 0:
            contador_impares += 1
    return contador_impares


# Chamando funções e saida
soma = somatoria(lista_input)
par = par(lista_input)
impar = impar(lista_input)
print(f'\nA lista digitada é: {lista_input}\n')
print(f'A somatória dos números na lista é: {soma}')
print(f'A quantidade de números pares na lista é: {par}')
print(f'A quantidade de números ímpares na lista é: {impar}')

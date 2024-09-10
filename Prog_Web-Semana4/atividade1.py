# Problema 1
# Entrada: Dado dois inputs, imprimir uma tabuada
print('Bem vindo(a) ao programa de tabuada!')
tabuada = int(input('Digite um número inteiro positivo: '))
valor_lim = int(input('Digite o valor limite d tabuada: '))

# Saida
print(f'A tabuada do {tabuada} de 0 a {valor_lim} é:')
for i in range(valor_lim + 1):
    print(f'{tabuada} X {i} = {tabuada * i}')
    
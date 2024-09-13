# Problema 3
# Entrada: solicitar N números e organizar em ordem crescente
print('Bem vindo(a) ao programa de organização de números!\n')
qnt_num = int(input('Digite a quantidade de números n = '))
# Recebendo e organizando
lista = []
for i in range(1, qnt_num + 1, 1):
    num = int(input(f'\nDigite o # {i} :\n'))
    lista.append(num)
# Saida
print('\nOs números digitados em ordem crescente são:\n')
for i in range(len(lista)):
    menor = min(lista)
    lista.remove(menor)
    print(menor)

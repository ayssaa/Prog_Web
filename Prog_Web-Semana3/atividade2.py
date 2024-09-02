# Problema 2
# Entrada: ler um nome e imprimir as n primeiras letras
print('Bem vindo(a) ao programa!')
nome = str(input('Digite um nome: '))
valor_n = int(input('Digite o valor de n: '))
# Saida
if valor_n > len(nome):
    print('Erro')
else:
    print(f'As primeiras {valor_n} letras do nome são: {nome[:valor_n]}')

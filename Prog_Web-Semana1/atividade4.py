# Elaborar um programa que calcule a área de um trapézio
print('Bem vindo(a) ao programa de cálculo de área de um trapézio!')
# Entrada dos dados do trapézio
base_maior = float(input('Digite o comprimento da base maior: '))
base_menor = float(input('Digite o comprimento da base menor: '))
h = float(input('Digite a altura do trapézio: '))
# Calculando...
a = (base_maior + base_menor) * h / 2
# Saida
print(f'A área do trapézio é: {a}')

# Problema: 3
# Entrada: dado dois valores, verificar sua soma é maior que 10 e imprimir uma saída
print('Bem vindo(a) ao programa!')
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
# Somando os valores
soma = valor1 + valor2
# Verificando...
if soma >= 10:
    soma += 5
else:
    soma -=7
# Saida
print(f'O resultado é: {soma}')

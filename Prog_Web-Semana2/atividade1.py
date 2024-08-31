# Problema: 1
# Entrada: dado a soma de 2 números, imprimir uma determinada saída
print('Bem vindo(a) ao programa!')
valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))
# Achando a soma
soma = valor1 + valor2
# Saida
if soma > 10:
    print(f'A soma dos números é: {soma}')
else:
    print(f'A soma dos números é menor que 10')

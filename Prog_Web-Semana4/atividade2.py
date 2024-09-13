# Problema 2
# Entrada: Dado dois números positivos, imprimir uma saida da somatória
print('Bem vindo(a) ao programa!')
while True:
    num1 = int(input('Digite o valor para x: '))
    num2 = int(input('Digite o valor para y: '))
    if num2 > num1:
        break
    else:
        print('O valor de y deve ser maior que o valor de x. Digite de novo os números.')
# Achando a somatória
somatorio = 0
for i in range(num1,num2+1,1):
    somatorio += i
# Saida
print(f'O valor da somatória dos valores de {num1} até {num2} é {somatorio}')
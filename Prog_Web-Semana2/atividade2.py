# Problema: 2
# Entrada: dada duas notas, achar a média aritmética e imprimir determinada saída
print('Bem vindo(a) ao programa!')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
# Achando a média
media = (nota1 + nota2) / 2
# Saida
print(f'A média do aluno é: {media}')
if media >= 6:
    print('Estudante aprovado(a)!')
else:
    print('Estudante reprovado(a)!')

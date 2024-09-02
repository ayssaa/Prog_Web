# Problema 1
# Entrada: Ler uma string qualquer
print('Bem vindo(a) ao programa!')
string = str(input('Digite uma palavra: '))
# Verificando o número de caractéres
numc = len(string)
# Saida: Dependendo do numc, realizar determinada saída
print(string)
if numc >= 5:
    print(f'O comprimento da palavra {string} é de {numc} caracteres')
else:
    print(f'A palavra {string} não possui 5 ou mais caracteres')

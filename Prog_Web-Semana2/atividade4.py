# Problema: 4
# Entrada: dado dois valores, realizar algumas contas...
print('Bem vindo(a) ao programa de diferença de valores!')
A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
# Continhas e saida!
if A == B:
    print('Os valores são iguais!')
else:
    if A > B:
        print(f'A diferença entre o maior valor e o menor valor é: {A - B}')
    else:
        print(f'A diferença entre o maior valor e o menor valor é: {B - A}')

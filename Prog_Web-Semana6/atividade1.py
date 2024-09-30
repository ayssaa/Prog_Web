"""Esse programa lê uma lista de alunos num arquivo (notas.in). O programa calcula a média das notas de cada aluno
e verifica se o aluno foi aprovado/reprovado. Os resultados são impressos num novo arquivo 'resultado.txt'"""


# Definindo a função para calcular média dos alunos
def medianota(valores):  # Recebe como parêmetro uma lista de notas de um aluno
    qnt_notas = len(valores)  # Calcula a quantidade de notas na lista dada
    soma = 0
    for i in range(qnt_notas):
        soma += valores[i]
    resultado = soma / qnt_notas  # calcula a média das notas do aluno
    return resultado


# Definindo a função que lê o arquivo de entrada
def ler_entrada(arquivo):
    with open(arquivo) as notas:  # Abre o arquivo de entrada como sendo a variável notas
        dados = notas.readlines()
        # lê todas as linhas do arquivo e armazena na variável dados = ['Aluno1 9 4 6\n', ...]
        for i in range(len(dados)):  # Percorrendo cada elemento de dados
            dados[i] = dados[i].rstrip("\n").split()
            # 'rstrip' remove o '\n'
            # 'split' separa os elementos, convertendo numa sublista dados = [['Aluno1', '9', '4', '6'], ...]
            for j in range(1, len(dados[i])):
                # Percorrendo cada sublista, dado que j = posição na lista (sempre iniciando em índice 1)
                # e i = índice indicando qual sublista estamos
                dados[i][j] = int(dados[i][j])  # convertendo os números str em ints
        # dados = [['Aluno1', 9, 4, 6], ['Aluno2', 8, 3, 3], ...]
        return dados


# Definindo a função que verifica os alunos aprovados/reprovados
def verifica_aprovados(notas):  # notas = dados = [['Aluno1', 9, 4, 6], ['Aluno2', 8, 3, 3], ...]
    num_alunos = len(notas)  # número de alunos = número de elementos na lista
    for i in range(num_alunos):
        media = round(medianota(notas[i][1:]), 1)
        # Calcula a média de notas sendo que i indica a sublista e o outro índice inicia em 1 até o final,
        # pegando somente as notas e o round arredonda em 1 casa decimal
        notas[i].append(media)  # Adiciona a média do aluno como último elemento nas sublistas
        if media >= 7.0:
            # Adiciona um novo último elemento nas sublistas, que pode ser Aprovado ou Reprovado
            notas[i].append('Aprovado')
        else:
            notas[i].append('Reprovado')
    return notas  # retorna a lista 'notas' com a média e aprovado/reprovado


# notas = [['aluno1', 1, 2, 3, media, situacao], ['aluno2', 1, 2, 3, media, situacao]]


# Função que calcula a quantidade de aluno reprovados e aprovados
def contagem(notas):  # recebe como parâmetro de entrada a lista 'notas'
    aluno_aprovado = 0
    aluno_reprovado = 0
    for i in range(len(notas)):
        for j in notas[i]:  # Passa por todos elementos de cada sublista verificando os aprovados e reprovados
            if j == 'Aprovado':
                aluno_aprovado += 1
            if j == 'Reprovado':
                aluno_reprovado += 1
    situacoes = [aluno_aprovado, aluno_reprovado]
    return situacoes  # Retorna a quantidade de aprovados e reprovados


# Função que escreve no arquivo de saída 1
def exporta_resultado1(notas):  # recebe como parâmetro de entrada a lista 'notas'
    arquivo1 = open('resultado1.txt', 'w')  # abre o arquivo de saída e o renomeia como sendo a variável arquivo
    num_alunos = len(notas)  # número de alunos = número de elementos na lista
    for i in range(num_alunos):
        nome = notas[i][0]  # nome do aluno que está na coluna [0] da sublista e na linha [i] da lista
        situacao = notas[i][-1]  # situação do aluno que está sempre como último elemento
        arquivo1.write(f'O aluno {nome} foi {situacao}\n')
    arquivo1.close()  # fecha o arquivo


# Função que escreve no arquivo de saída 2
def exporta_resultado2(situacoes):  # recebe como parâmetro de entrada a lista no formato [aluno_aprovado, aluno_reprovado]
    arquivo2 = open('resultado2.txt', 'w')  # abre o arquivo de saída e o renomeia como sendo a variável arquivo
    arquivo2.write(f'Alunos aprovados: {situacoes[0]}\nAlunos reprovados: {situacoes[1]}')
    arquivo2.close()  # fecha o arquivo

#############################################################################
# O programa começa aqui
# Primeiro chamamos a função que lê o arquivo de entrada e armazena o valor retornado na variável 'notas'
notas = ler_entrada("notas.in")

# Agora chamamos a função que chama a função medianota e calcula a média, posteriormente verifica a média e indica se o
# aluno foi aprovado ou reprovado. Depois armazena o valor retornado na variável 'notas'
notas = verifica_aprovados(notas)

# Chamando a função que conta quantos alunos foram reprovados e aprovados
situacoes = contagem(notas)

# Chamamos as funções que exportam oa resultadoa em um arquivo resultado1 e um arquivo resultado2
exporta_resultado1(notas)
exporta_resultado2(situacoes)

# FOR que percorre cada elemento de 'notas'
for i in range(len(notas)):
    print(notas[i])  # imprime os valores de cada linha da variável 'notas'

# Printando quantidade de alunos reprovados e aprovados
print(f'\nAlunos aprovados: {situacoes[0]}\nAlunos reprovados: {situacoes[1]}')

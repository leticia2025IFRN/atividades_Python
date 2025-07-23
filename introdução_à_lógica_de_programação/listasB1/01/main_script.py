"""
# ------------------------- ROTEIRO ------------------------- #
Construa soluções de algoritmos e implemente-os utilizando a 
linguagem de programação Python para os seguintes casos:
"""

# Funções para formar cabeçalho e rodapé:
def heading(n, text):
    if n != 0:
        repeat = int(n / 2) - int(len(text) / 1.7)
        space = ' '
        for i in range(0, repeat):
            space = space + ' '
        print('\033[1;34;40m=\033[0m' * n)
        print(f'\033[1;34;40m{space}{text.title()}\033[0m')
        print('\033[1;34;40m=\033[0m' * n)


def footer(n, text):
    if n != 0:
        repeat = int(n / 2) - int(len(text) / 1.7)
        space = ' '
        for i in range(0, repeat):
            space = space + ' '
        print('\033[1;31;40m#\033[0m' * n)
        print(f'\033[1;31;40m{space}{text.title()}\033[0m')
        print('\033[1;31;40m#\033[0m' * n + '\n')

"""
QUESTÃO 01

Calculadora Simples: Solicite ao usuário para inserir dois valores numéricos, 
realize as operações de soma, subtração, multiplicação e divisão, e ao final 
exiba os valores de cada uma das operações.

TESTES:
1. Entradas 10 e 2
2. Entradas 10 e 0
3. Entradas 0 e 2
4. Entradas 10 e -2
5. Entradas -2 e 10
"""
heading(60, 'QUESTÃO 01:')

print('\nSeja bem-vindo a calculadora simples.\nDigite dois valores numéricos para começar as operações.\n')
# Variáveis:
numA = float(input('Digite o primeiro número: '))
numB = float(input('Digite o segundo número: '))
# Decisão: verifica se o segundo número é equivalente a zero para responder adequadamente a respeito da divisão.
if numB == 0:
    soma = float(numA + numB) # Adição
    mult = float(numA * numB) # Multiplicação 
    subt = float(numA - numB) # Subtração
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nSoma: {numA} + {numB} = {soma}.\nMultiplicação: {numA} x {numB} = {mult}.\nSubtração: {numA} - {numB} = {subt}.\n\033[1;33;40mPara poder executar o operador de divisão, era necessário que o segundo número seja maior que 0 (zero) para prosseguir com a operação.\nAfinal, não existe número divisível por 0.\033[0m\n')
else:
    soma = float(numA + numB)
    mult = float(numA * numB)
    subt = float(numA - numB)
    divs = float(numA / numB) # Divisão
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nSoma: {numA} + {numB} = {soma}.\nMultiplicação: {numA} x {numB} = {mult}.\nSubtração: {numA} - {numB} = {subt}.\nDivisão: {numA} / {numB} = {divs}.\n')

footer(60, 'FIM DA QUESTÃO 01')
"""
QUESTÃO 02

Conversor de Temperatura: Solicite ao usuário um valor de temperatura em 
graus Celsius, converta-a para Fahrenheit e exiba o resultado da conversão.

TESTES:
1. Entrada 25 => 77
2. Entrada -5 => 23
3. Entrada 0 => 32
"""
heading(60, 'QUESTÃO 02:')

print('\nSeja bem-vindo ao conversor de temperatura.\n')
# Variáveis:
temperatura = float(input('Digite uma temperatura em graus Celsius (°C) para começar a aplicação e convertê-la para Fahrenheit (°F).\nTEMPERATURA: '))
fahrenheit = ((9/5) * temperatura) + 32
# Exibição do resultado:
print(f'\n\033[1;33;40mRESULTADO:\033[0m A conversão de {temperatura}°C para Fahrenheit é {fahrenheit}°F.\n')

footer(60, 'FIM DA QUESTÃO 02')
"""
QUESTÃO 03

Área do Círculo: Solicite ao usuário um valor do raio de um círculo, calcule 
sua área e exiba o resultado do cálculo.

TESTES:
1. Entrada 300 => 282743.34
2. Entrada 0 => ERRO
"""
heading(60, 'QUESTÃO 03:')
# Importação da biblioteca 'math' para resgatar o valor de pi:
# Se houver a necessidade de utilizar essa biblioteca nos próximos códigos, não precisarei digitar novamente.
import math
# Equação da área do círculo em função do raio:
def area(raio):
    return math.pi * (raio ** 2)

print('\nSeja bem-vindo à aplicação.\nPara saber a área de um cículo, digite um raio para começar a aplicação.\n')
# Entrada:
raio_input = float(input('RAIO: '))
# Decisão: Verificará se o raio digitado pelo usuário é maior que zero para prosseguir com o cálculo. Caso contrário, o programa informará ao usuário sobre o erro e encerrará o programa.
if raio_input > 0:
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nA área do cículo com raio de {raio_input} unidades é {round(area(raio_input), 2)} unidades ao quadrado.')
else:
    print("\n\033[1;31;40mERRO! Para formar a área da figura, é necessário que a medida do raio seja maior que 0 (zero).\033[0m")

footer(60, 'FIM DA QUESTÃO 03')
"""
QUESTÃO 04

Área do Triângulo: Solicite ao usuário um valor da base e da altura de um
triângulo, calcule sua área e exiba o resultado do cálculo.

TESTES:
1. Entradas 9 e 12 => 54
2. Entradas 0 e 12 => ERRO
3. Entradas 9 e 0 => ERRO
"""
heading(60, 'QUESTÃO 04:')

# Equação da área do círculo em função do raio:
def area(base, altura):
    return (base * altura) / 2

print('\nSeja bem-vindo à aplicação.\nPara saber a área de um triângulo, o valor da base e da altura para começar a aplicação.\n')
# Variáveis de entrada (base e altura):
base_input = float(input('BASE: '))
altura_input = float(input('ALTURA: '))
# Estrutura. básica de tratamento de erro: verificará se o usuário digitou 0 em uma das entradas.
if base_input > 0 and altura_input > 0:
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nA área do triângulo que possui {base_input} unidades de base e {altura_input} unidades de altura é {round(area(base_input, altura_input), 1)} unidades ao quadrado.')
elif base_input <= 0:
    print("\n\033[1;31;40mERRO! Para formar a área da figura, é necessário que a base seja maior que 0 (zero).\033[0m")
elif altura_input <= 0:
    print("\n\033[1;31;40mERRO! Para formar a área da figura, é necessário que a altura seja maior que 0 (zero).\033[0m")
else:
    print("\n\033[1;31;40mERRO! Para formar a área da figura, é necessário que ambos as medidas sejam maiores que 0 (zero).\033[0m")

footer(60, 'FIM DA QUESTÃO 04')
"""
QUESTÃO 05

Volume da Esfera: Solicite ao usuário um valor do raio de uma esfera, 
calcule seu volume e exiba o resultado do cálculo.

TESTES:
1. Entrada 5 => 523.6
2. Entrada 0 => ERRO
"""
heading(60, 'QUESTÃO 05:')

def volume(raio):
    return (4 * math.pi * (raio**3))/3

print('\nSeja bem-vindo à aplicação.\nDeseja saber o volume de uma determinada esfera? Digite o raio para começar a calcular.\n')
# Variável de entrada (raio):
raio_input = float(input('RAIO: '))
# Estrutura de decisão: se o raio digitado for maior que 0, exibirar o resultado. Caso contrário, mostrará a mensagem de erro.
if raio_input > 0:
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nO volume da esfera de raio {raio_input} unidades é {round(volume(raio_input), 2 )} unidades ao cubo.')
else:
    print("\n\033[1;31;40mERRO! Não poderei prosseguir sem um raio definido! É necessário que o raio seja maior que 0 (zero).\033[0m")

footer(60, 'FIM DA QUESTÃO 05')
"""
QUESTÃO 06

Calculadora de Média Aritmética: Solicite ao usuário para que ele insira três
valores de notas, realize o cálculo da média aritmética e em seguida exiba os três
valores digitados pelo usuário e o resultado do cálculo.

TESTES:
1. Entradas -1, 10, 10 => ERRO
2. Entradas 10, -1, 10 => ERRO
3. Entradas 10, 10, -1 => ERRO
4. Entradas 5.9, 2.1, 1 => 3
5. Entradas 8, 5.2, 6.6 => 6.6
6. Entradas 8, 6.4, 6.6 => 7
"""
heading(60, 'QUESTÃO 06:')

def media(n1, n2, n3):
    return (n1 + n2 + n3)/3

print('\nSeja bem-vindo à aplicação de média aritmética.\nDigite três notas para calcular sua média e ver se você será reprovado, em recuperação ou aprovado.\n')
# Variável de entrada
nota1 = float(input('1° NOTA: '))
nota2 = float(input('2° NOTA: '))
nota3 = float(input('3° NOTA: '))
# Estrutura de decisão: se as notas digitado forem maiores que 0, exibirar o resultado. Caso contrário, mostrará a mensagem de erro.
if nota1 < 0 or nota1 > 10:
    print("\n\033[1;31;40mTemos um problema! Para se ter resultado, é necessário que sua primeira nota esteja entre 0 (zero) e 10 (dez).\033[0m")
elif nota2 < 0 or nota2 > 10:
    print("\n\033[1;31;40mTemos um problema! Para se ter resultado, é necessário que sua segunda esteja entre 0 (zero) e 10 (dez).\033[0m")
elif nota3 < 0 or nota3 > 10:
    print("\n\033[1;31;40mTemos um problema! Para se ter resultado, é necessário que sua terceira esteja entre 0 (zero) e 10 (dez).\033[0m")
# A partir desta linha, a estrutura verificará se o aluno passou de ano ou não.
elif round(media(nota1, nota2, nota3), 1) <= 3:
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nSua média a partir a soma das notas {nota1}, {nota2} e {nota3}, dividida por 3, é {round(media(nota1, nota2, nota3), 1)}.\n\033[1;31;40mATENÇÃO! ESTÁ REPROVADO(A).\033[0m')
elif round(media(nota1, nota2, nota3), 1) < 7:
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nSua média a partir a soma das notas {nota1}, {nota2} e {nota3}, dividida por 3, é {round(media(nota1, nota2, nota3), 1)}.\n\033[1;33;40mCUIDADO! ESTÁ EM RECUPERAÇÃO.\033[0m')
else:
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nSua média a partir a soma das notas {nota1}, {nota2} e {nota3}, dividida por 3, é {round(media(nota1, nota2, nota3), 1)}.\n\033[1;32;40mPARABÉNS! ESTÁ APROVADO(A).\033[0m')

footer(60, 'FIM DA QUESTÃO 06')
"""
QUESTÃO 07

Calculadora de Média Ponderada: Solicite ao usuário para que ele insira os
valores de 4 notas e seus respectivos pesos, em seguida realize o cálculo da média
pondera e exiba o resultado do cálculo.

TESTES:
1. Entradas -1, 1, 10, 2, 10, 3, 10, 4 => (ERRO)
2. Entradas 5, 1, 12, 2, 20, 3, 15, 4 => 14.9 (ERRO)
3. Entradas 8, 1, 5.2, 2, 6.6, 3, 10, 4 => 7.8
4. Entradas 4.3, 1, 6.4, 2, 6.6, 3, 7.8, 4 => 6.8
5. Entradas 5.1, 1, 4.7, 2, 2.3, 3, 1.6, 4 => 2.8
6. Entradas 5.2, 1, 6.0, 2, 3.3, 3, 1.2, 4 => 3.2 (opcional)
"""
heading(60, 'QUESTÃO 07:')

def media(nota1, peso1, input_n2, peso2, input_n3, peso3, nota4, peso4):
    return ((nota1*peso1) + (input_n2*peso2) + (input_n3*peso3) + (nota4*peso4)) / (peso1 + peso2 + peso3 + peso4)

print('\nSeja bem-vindo à aplicação de média aritmética.\nDigite três notas para calcular sua média e ver se você será reprovado, em recuperação ou aprovado.\n')
# Variável de entrada
while True:
    input_n1 = float(input('1° NOTA: '))
    input_p1 = float(input('1° PESO: '))
    input_n2 = float(input('\n2° NOTA: '))
    input_p2 = float(input('2° PESO: '))
    input_n3 = float(input('\n3° NOTA: '))
    input_p3 = float(input('3° PESO: '))
    input_n4 = float(input('\n4° NOTA: '))
    input_p4 = float(input('4° PESO: '))
    # Estrutura de decisão: se as notas digitado forem maiores que 0, exibirar o resultado. Caso contrário, mostrará a mensagem de erro.
    if input_n1 < 0 or input_n1 > 10:
        print("\n\033[1;31;40mTemos um problema! Para se ter resultado, é necessário que sua primeira nota esteja entre 0 (zero) e 10 (dez).\033[0m")
    else:
        if input_n2 < 0 or input_n2 > 10:
            print("\n\033[1;31;40mTemos um problema! Para se ter resultado, é necessário que sua segunda nota esteja entre 0 (zero) e 10 (dez).\033[0m")
        else:
            if input_n3 < 0 or input_n3 > 10:
                print("\n\033[1;31;40mTemos um problema! Para se ter resultado, é necessário que sua terceira nota esteja entre 0 (zero) e 10 (dez).\033[0m")
            else:
                if input_n4 < 0 or input_n4 > 10:
                    print("\n\033[1;31;40mTemos um problema! Para se ter resultado, é necessário que sua quarta nota esteja entre 0 (zero) e 10 (dez).\033[0m")
                else:
                    break

resultado = round(media(input_n1, input_p1, input_n2, input_p2, input_n3, input_p3, input_n4, input_p4), 1)
# A partir desta linha, a estrutura verificará se o aluno passou de ano ou não.
if resultado <= 3:
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nSua média a partir a soma das notas {input_n1}, {input_n2}, {input_n3} e {input_n4}, dividida pela soma dos pesos, é {resultado}.\n\033[1;31;40mATENÇÃO! ESTÁ REPROVADO(A).\033[0m')
elif resultado < 7:
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nSua média a partir a soma das notas {input_n1}, {input_n2}, {input_n3} e {input_n4}, dividida pela soma dos pesos, é {resultado}.\n\033[1;33;40mCUIDADO! ESTÁ EM RECUPERAÇÃO.\033[0m')
else:
    print(f'\n\033[1;33;40mRESULTADOS:\033[0m\nSua média a partir a soma das notas {input_n1}, {input_n2}, {input_n3} e {input_n4}, dividida pela soma dos pesos, é {resultado}.\n\033[1;32;40mPARABÉNS! ESTÁ APROVADO(A).\033[0m')

footer(60, 'FIM DA QUESTÃO 07')
"""
QUESTÃO 08

Equação de Segundo Grau: Solicite ao usuário os valores de “a”, “b”, “c” e “x”, em
seguida resolva uma equação quadrática do tipo y = ax2 + bx + c e exiba o valor
de y para o usuário.
"""
heading(60, 'QUESTÃO 08:')

def y(a, b, c, x):
    return (a * (x ** 2)) + (b * x) + c

print('\nSeja bem-vindo à aplicação de Equação de Segundo Grau.\nDigite quatro valores (a, b, c e x) para montar uma equação quadrática e você receberá a resolução (y) em poucos instantes.\n')
input_a = float(input('a = '))
input_b = float(input('b = '))
input_c = float(input('c = '))
input_x = float(input('x = '))

print(f"O resultado da equação é {y(input_a, input_b, input_c, input_x)}.")

footer(60, 'FIM DA QUESTÃO 08')
"""
QUESTÃO 09

Calculadora de IMC: Solicite ao usuário os valores de peso (kg/quilos) e 
altura (m/metros), calcule o índice de massa corporal (IMC), sabendo que 
peso/altura^2, em seguida exiba o valor do IMC calculado.
"""
heading(60, 'QUESTÃO 09:')
# Entrada:
print('Seja bem-vindo a aplicação!\nDeseja saber seu índice de massa corporal? Digite seu peso e sua altura para começar a calcular.')
while True:
    peso = float(input('PESO (Esperamos que digite um número entre 60 e 130): '))
    altura = float(input('ALTURA (Esperamos que digite um número entre 1,5 e 1,9): '))
    if peso < 60 or peso > 130:
        print('Temos um problema! O peso está fora do limite estabelecido. Tente novamente.\n')
    elif altura < 1.5 or altura > 1.9:
        print('Temos um problema! A altura está fora do limite estabelecido. Tente novamente.\n')
    else:
        break
# Variável - IMC:
indice = peso / (altura**2)
# Saída:
if round(indice, 2) < 18.5:
    print(f'\nSeu índice de massa corporal é {round(indice, 2)}. Você se encontra Abaixo do Peso.')
elif 18.5 <= round(indice, 2) < 24.9:
    print(f'\nSeu índice de massa corporal é {round(indice, 2)}. Você se encontra com Peso Normal.')
elif 24.9 <= round(indice, 2) < 30:
    print(f'\nSeu índice de massa corporal é {round(indice, 2)}. Você se encontra com Excesso de Peso.')
elif 30 <= round(indice, 2) < 34.9:
    print(f'\nSeu índice de massa corporal é {round(indice, 2)}. Você se encontra com Obesidade de Classe I.')
elif 34.9 <= round(indice, 2) < 39.9:
    print(f'\nSeu índice de massa corporal é {round(indice, 2)}. Você se encontra com Obesidade de Classe II.')
elif 39.9 <= round(indice, 2):
    print(f'\nSeu índice de massa corporal é {round(indice, 2)}. Você se encontra com Obesidade de Classe III.')

footer(60, 'FIM DA QUESTÃO 09')
"""
QUESTÃO 10

Tabuada: Solicite ao usuário um valor numérico, em seguida, exiba a tabuada de
um número específico (por exemplo, 5). O programa deverá ter como saída:
■ 5x1 = 5;
■ 5x2 = 10;
■ 5x3 = 15;
■ 5x4 = 20;
■ 5x5 = 25;
■ 5x6 = 30;
■ 5x7 = 35;
■ 5x8 = 40;
■ 5x9 = 45;
■ 5x10 = 50;
"""
heading(60, 'QUESTÃO 10:')
# Função principal:
def tabuada(valor, item):
    return valor * item

print('\nSeja bem-vindo à aplicação.')
# Entrada:
input_valor = float(input('\nDigite um número para saber a sua tabuada: '))
# Saída:
print('\n\033[1;33;40mRESULTADOS:\033[0m')
for num in range(1, 11):
    print(f'■ {input_valor} x {num} = {tabuada(input_valor, num)}')

footer(60, 'FIM DA QUESTÃO 10')
"""
QUESTÃO 11

Conversão de Segundos para o Formato HORA:MINUTO:SEGUNDO: Solicite  ao usuário
um valor numérico correspondente à quantidade de segundos, em  seguida converta 
o valor para o formato de HORA:MINUTO:SEGUNDO.

TESTES
1. 19.922 => 05:32:02
2. 0 => 00:00:00
3. -19.922 => ERRO
"""
# TODO: Este código não tem (ainda) seu fluxograma. Farei quando finalizar todos os códigos.
heading(60, 'QUESTÃO 11:')
# Função para converter o tempo (opcional):
# def relogio(valor):
#     hora = valor // 3600
#     minutos = (valor % 3600) // 60
#     segundos = (valor % 3600) % 60
#     return '%02d:%02d:%02d.' % (hora, minutos, segundos)

print('\nSeja bem-vindo ao conversor de tempo.\nDigite um número em segundos para aparecer no formato "HORA:MINUTO:SEGUNDO".\n')
# Entrada:
input_segundos = float(input('SEGUNDOS: '))
# Saída:
if input_segundos < 0: # Verifica se o tempo em seguandos inserido pelo usuário é negativo.
    print('\033[1;31;40mTemos um problema! Não estamos considerando princípios e teorias da física para aceitar o valor de tempo negativo, além de que o resultado apresente-se totalmente diferente do valor esperado.\nPor favor, digite o valor novamente.\n\033[0m')
else:
    # Variáveis principais:
    hora = input_segundos // 3600
    minutos = (input_segundos % 3600) // 60
    segundos = (input_segundos % 3600) % 60

    # Outros testes:
    #print(f'O tempo, \033[1;33m{input_segundos} segundos,\033[0m corresponde a \033[1;32m{hora}:{minutos}:{segundos}\033[0m\n.')
    #print(f'O tempo, \033[1;33m{input_segundos} segundos,\033[0m corresponde a \033[1;32m{relogio(input_segundos)}\033[0m\n' ) # Depende da função está habilitada.

    # Considere-se esta linha de comando:
    print(f'O tempo, \033[1;33m{input_segundos} segundos,\033[0m corresponde a \033[1;32m%02d:%02d:%02d.\033[0m\n' % (hora, minutos, segundos))

footer(60, 'FIM DA QUESTÃO 11')

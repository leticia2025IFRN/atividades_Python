# Impotação dos módulos criados:
import module.utils as utils
import module.estatisticas as estatistica
# Funções para formar cabeçalho e rodapé:
def heading(n: int, text: str):
    if n != 0:
        repeat = int(n / 2) - int(len(text) / 1.7)
        space = ' '
        for i in range(0, repeat):
            space = space + ' '
        print('\033[1;34m=\033[0m' * n)
        print(f'\033[1;34m{space}{text.title()}\033[0m')
        print('\033[1;34m=\033[0m' * n)

def footer(n: int, text: str):
    if n != 0:
        repeat = int(n / 2) - int(len(text) / 1.7)
        space = ' '
        for i in range(0, repeat):
            space = space + ' '
        print('\033[1;31m#\033[0m' * n)
        print(f'\033[1;31m{space}{text.title()}\033[0m')
        print('\033[1;31m#\033[0m' * n + '\n')

"""
# QUESTÃO 01
Criar um módulo chamado 'utils.py' e implemente dentro do módulo 5 funções:
    1. Criar uma lista de números e retornar essa lista;
    2. Exibir uma lista de números;
    3. Cálculo de média aritmética, cuja a entrada deve ser uma lista de números e o retorno (a saída é) o resultado da média;
    4. Verificar se um valor é par ou ímpar e retorna um (valor) booleano;
    5. Receber uma lista de números inteiros e retornar duas listas, uma com pares e outra com ímpares;
Após isso, implemente um programa (main_script.py) que ofereça ao usuário um menu de funcionalidades que possibilite testar as funções do item anterior.
    > O programa deverá funcionar em looping e dar ao usuário a opção para encerrá-lo.
"""
heading (60, 'QUESTÃO 01')
# Insira o código aqui.
footer(60, 'FIM DA QUESTÃO 01')
"""
# QUESTÃO 02
Criar um módulo chamado 'estatisticas.py' e implemente estas funções:
    1. gerar_lista(tamanho: int, minimo: int, maximo: int) -> list:
        Gera e retorna uma lista de números inteiros aleatórios dentro de um intervalo definido.
    2. maior_valor(lista: list) -> int:
        Retorna o maior valor presente na lista.
    3. menor_valor(lista: list) -> int:
        Retorna o menor valor da lista.
    4. frequencia_valores(lista: list) -> dict:
        Retorna um dicionário com a frequência de cada número na lista.
    5. remover_repetidos(lista: list) -> list:
        Retorna uma nova lista contendo apenas os valores únicos (sem repetições).
Após isso, implemente um programa principal (main_script.py) que:
    1. Importe o módulo 'estatisticas';
    2. Exiba um menu interativo com as seguintes opções para o usuário:
        > Gerar uma nova lista
        > Exibir maior valor
        > Exibir menor valor
        > Ver frequência de cada valor
        > Remover valores repetidos
        > Sair
    3. O programa deverá funcionar em looping até que o usuário escolha sair.
"""
heading (60, 'QUESTÃO 02')
# Insira o código aqui.
footer(60, 'FIM DA QUESTÃO 02')

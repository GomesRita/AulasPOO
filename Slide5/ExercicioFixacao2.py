"""
Implemente um programa que realiza o cálculo de uma lista de
valores de y correspondente a uma equação de primeiro grau, a
qual é dada por y = a*x + b
■ O programa deverá:
■ Perguntar ao usuário quantas equações serão calculadas
■ Pergunta os valores de a, b e x para cada uma das equações
■ Exibir a equação no forma “y = a*x + b”, substituindo cada valor de a, b e x pelo
valores fornecidos pelo próprio usuário
■ Exibir o valor de y em cada uma das funções
■ Use listas para armazenar os valores das variáveis fornecidos pelo usuário
"""

qntd = int(input("Quantas equações serão calculadas? "))
lista = []
contador = 0
while contador < qntd:
    print(f'Equação número {contador+1}')
    a = int(input("Valor de a: "))
    x = int(input("Valor de x: "))
    b = int(input("Valor de b: "))
    y = a**x + b
    lista.append((f'Equação {contador+1}',y))
    print(f'O valor da equação {contador} é igual a {y}')
    contador = contador + 1
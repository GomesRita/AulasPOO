"""
Escreva um programa que solicite do usuário um valor positivo e imprima
todos os números inteiros de 1 até o número digitado pelo usuário.
"""

numero = int(input("Digite um número inteiro e positivo: "))

while numero <=0:
    numero = int(input("Digite um número inteiro e positivo: "))

for i in range(1, numero+1, +1):
    print(i, end=" ")

"""
O cálculo do fatorial de um número é dado pela multiplicação desse
número com todos os antecessores inteiros positivos. Por exemplo, o
fatorial de 5 é 5! = 5*4*3*2*1 = 120. Escreva um programa que
solicite um número e apresente o resultado do seu fatorial.
"""

num = int(input("Informe um número: "))

while num > 1:
    fatorial = num*(num -1)
    num = num - 1
    print(num)
    if num == 1:
        print(fatorial)

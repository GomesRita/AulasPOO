"""
Escreva um programa que solicite do usuário dois valores positivos e
imprima todos os números inteiros dentro desse intervalo excluindo-se o
valor inicial do intervalo e o valor final.
"""

Inicio = int(input("Valor incial: "))
Fim = int(input("Valor final: "))

while Inicio <= 0 or Fim <=0 :
    if Inicio > Fim:
        print("O valor inicial é maior que o valor final!")
        Inicio = int(input("Valor incial: "))
        Fim = int(input("Valor final: "))

    elif Inicio <=0 or Fim <= 0:
        print("Informe apenas valores inteiros e positivos!!")
        Inicio = int(input("Valor incial: "))
        Fim = int(input("Valor final: "))
    
if Inicio == Fim:
    print("Não existe intervalo de números inteiros entre esses dois valores pois eles são iguais")


for i in range(Inicio, Fim, +1):
    if( i != Inicio):
        print(i, end=" ")

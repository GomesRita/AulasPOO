"""
Escreva um programa que solicite do usuário dois valores positivos e
imprima todos os números inteiros dentro desse intervalo. O algoritmo
deve armazenar cada valor em duas variáveis diferentes (v_ini e v_fim).
"""

v_ini = int(input("Valor incial: "))
v_fim = int(input("Valor final: "))

while v_fim <=0 or v_ini <= 0 or v_ini > v_fim:
    if v_ini > v_fim:
        print("O valor inicial é maior que o valor final !!")
        v_ini = int(input("Valor incial: "))
        v_fim = int(input("Valor final: "))

    elif v_fim <=0 or v_ini <= 0:
        print("Informe apenas valores inteiros e positivos!!")
        v_ini = int(input("Valor incial: "))
        v_fim = int(input("Valor final: "))

for i in range(v_ini, v_fim, +1):
        print(i, end=" ")
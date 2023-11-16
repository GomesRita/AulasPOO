"""
Escreva um programa que leia dois valores que representem o início
e o fim de um intervalo. O programa deverá ler um terceiro valor
digitado e verificar se este terceiro valor está dentro do intervalo ou
fora. Caso esteja fora do intervalo, deverá informar se está na parte
inferior ou superior do intervalo.
"""
numero1 = int(input("Início: "))
numero2 = int(input("Fim: "))

numero3 = int(input("Verificar qual número? "))

if numero3 >= numero1  and numero3 <= numero2:
    print("Dentro do intervalo")
else: 
    print("Fora do intervalo")
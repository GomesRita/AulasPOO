"""
Escreva um programa que sempre escolhe o menor caminho a ser percorrido pelo usuário em
função do local onde se encontra e as opções de caminho a serem seguidas. O usuário sempre
parte do ponto A. O usuário deverá fornecer os valores de distância entre os pontos e o programa
deverá apresentar o caminho a ser percorrido e a distância, conforme o exemplo. Sua solução
deve utilizar apenas estruturas condicionais.
"""

DistanciaAB = int(input("Distância de A à B: "))
DistanciaAC = int(input("Distância de A à C: "))

if DistanciaAB < DistanciaAC: 
    print("Seguir o caminho de AB")
    DistanciaBD = int(input("Distância de B à D: "))
    DistanciaBC = int(input("Distância de B à C: "))

    if DistanciaBD < DistanciaBC: 
        print("Seguir o caminho de BD")
    if DistanciaBD > DistanciaBC: 
        print("Seguir o caminho de BC")

elif DistanciaAB > DistanciaAC:
    print("Seguir o caminho de AC")

    DistanciaCF = int(input("Distância de C à F: "))
    DistanciaCG = int(input("Distância de C à G: "))

    if DistanciaCF < DistanciaCG: 
        print("Seguir o caminho de CF")
    if DistanciaCF > DistanciaCG: 
        print("Seguir o caminho de CG")

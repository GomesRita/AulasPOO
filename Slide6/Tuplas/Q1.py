"""
Escreva uma função que receba uma tupla de números inteiros e retorne
uma nova tupla com os elementos pares da tupla original. Por exemplo, se a
tupla for (1, 2, 3, 4, 5), a função deve retornar (2, 4).
"""
def Calc():
    qntd = int(input('Quantos valores seão inseridos: '))
    lista = []
    NovaLista = []
    while qntd > 0:
        valor = int(input('Informe o valor: '))
        lista.append(valor)
        qntd = qntd - 1

    TuplaOriginal = tuple(lista)
    print(f'Tupla Original: {TuplaOriginal}')

    for i in lista:
        if i%2 == 0:
            NovaLista.append(i)

    NovaTupla = tuple(NovaLista)
    print(f'Nova Tupla: {NovaTupla}')

Calc()
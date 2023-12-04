"""
Escreva uma função que receba uma tupla de strings e retorne uma nova
tupla com as strings ordenadas alfabeticamente e sem repetições. Por
exemplo, se a tupla for ("banana", "maçã", "laranja", "banana", "uva"), a
função deve retornar ("banana", "laranja", "maçã", "uva").
"""

frutas = ("banana", "maçã", "laranja", "uva")
def Ordenar(frutas):
    ListaFrutas = list(frutas)
    print(sorted(ListaFrutas))

Ordenar(frutas)


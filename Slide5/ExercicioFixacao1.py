""""
Considere o seguinte código Python
e modificando apenas os valores do
campo prox faça:
■ Exiba as letras em ordem alfabética
■ Remova a letra ‘c’ da sequência
exibida

■ Inclua a letra ‘j’ na posição do Nó
‘c’
■ Qual a categoria de alocação de
memória foi utilizada na
implementação desse programa?
Justifique.
"""

class No:
    def __init__(self, letra, prox):
        self.letra = 'a'
        self.prox = 6

lista = [
    ('e', 1), ('h',2), ('b',3), ('f', 4), ('a',5),
    ('i',6), ('g',7), ('c',8), ('d', -1)
]

l = 0
while l != -1:
    print(lista[l].letra, end = ' ')
    l = lista[l].prox


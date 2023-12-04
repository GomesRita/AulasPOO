"""
Escreva um programa em Python para auxiliar uma pessoa a realizar uma lista de compras em um
supermercado. O seu programa deve permitir que o usuário crie uma lista de compras contendo o
nome do produto, o seu respectivo valor e o status (comprado ou não comprado). O usuário do
programa deverá poder cadastrar os produtos e valores na lista de compras, bem como poder
visualizar a lista de compras a qualquer momento que ele desejar. Caso o usuário encontre o
produto no supermercado e deseje levar o produto o programa deverá marcar o item como
comprado. A término das compras, o usuário deverá poder visualizar o total e a quantidade de itens
comprados, bem como a relação de itens que não foram comprados. (25pts)
a. OBS: Utilize o tipo, ou os tipos, de coleção(ões) que você considerar mais adequado(s)
para solucionar o problema.
"""

# O seu programa deve permitir que o usuário crie uma lista de compras contendo o nome do produto
# > Pedir a quantidade de itens que serão inseridos, adicionar estrutura while e inserir em uma lista (nome, valor, status)
# poder cadastrar os produtos e valores na lista de compras,poder visualizar a lista de compras 
# > adicionar um menu com opção de inserir item, visualizar lista, finalizar compra

#Inicializando a primeira lista
qntd = int(input("Quantos produtos deseja comprar? "))
listaCompras = []
contador = 1
while contador <= qntd:
    contador = contador +1
    lista = []
    nome = input("Nome do produto: ")
    valor = int(input("Valor do produto: "))
    lista.append(nome)
    lista.append(valor)
    listaCompras.append(lista)

#funções utilizadas
def menu():

    print("""
        LISTA DE COMPRAS
        
        1 - Inserir um novo produto
        2 - Marcar item como comprado
        3 - Visualizar lista de compras
        4 - Finalizar compras
    """)


def InserirItem():
    lista = []
    nome = input("Nome do produto: ")
    valor = int(input("Valor do produto: "))
    lista.append(nome)
    lista.append(valor)
    listaCompras.append(lista)

def Comprar(): 
    return True

menu()
opcao = int(input("Escolha uma opção: "))

while(opcao < 1 or opcao > 4):
    print("Informe um valor válido!")
    menu()
    opcao = int(input("Escolha uma opção: "))

if(opcao == 1):
    InserirItem()
    menu()
    opcao = int(input("Escolha uma opção: "))
if(opcao == 2):
    Comprar()
    menu()
    opcao = int(input("Escolha uma opção: "))
if(opcao == 3):
    for i in range(len(listaCompras)):
        print()
        for j in range(3):
            print(listaCompras[i][j], end = "")

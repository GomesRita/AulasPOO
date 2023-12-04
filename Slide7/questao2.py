"""
Considere a abstração de um objeto cachorro. Crie uma classe
que possa representar as características e ações que podem ser
realizadas por esse objeto. Implemente a classe e um programa
que faça um teste demonstrativo do funcionamento da mesma.
"""

class Cachorro:

    def __init__(self,raca, porte):
        raca = raca
        porte = porte

    def latir(self):
        print("Au Au Au")
    
    def correr(self):
        print("Correndo...")
    
    def dormir(self):
        print('zzzzzz')
    
    def comer(self):
        print('hmmm nhac nhac')

dog = Cachorro()

dog.comer()
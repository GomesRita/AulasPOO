class Carro:
    
    def __init__ (self, modelo, cor, marca):
     modelo = modelo
     cor = cor
     marca = marca

    def ligar(self):
         print('Carro ligado')

    def desligar(self):
         print('Carro Desligado')

    def acelerar(self):
         print('Acelerando...')

    def frear(self):
         print('Freando!')
    
carro = Carro()
carro2 = Carro
carro.ligar()
print(id(carro))
print(id(carro2))
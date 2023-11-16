class Carro:
    modelo = ''
    cor = ''
    marca = ''

    def ligar(self):
         print('Carro ligado')

    def desligar(self):
         print('Carro Desligado')

    def acelerar(self):
         print('Acelerando...')

    def frear(self):
         print('Freando!')
    
carro = Carro()
carro.ligar()
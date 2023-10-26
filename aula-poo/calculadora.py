class Calculadora:

    def calcular(self, operacao, num1, num2):
        if operacao  == '+':
            return self.__adicao(self, num1, num2)
        
        if operacao == '-':
            return self.__subtracao(num1,num2)
    
    def __adicao(num1, num2):
        return (num1 + num2)
    
    def __subtracao(num1, num2):
        return num1 - num2

calculadora = Calculadora()
resposta = calculadora.calcular('+', 3, 6)
print(resposta)
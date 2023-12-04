"""
Implemente todos os exemplos dessa unidade. Faça alterações e veja o que
acontece em cada um dos exemplos.

Implemente a classe a partir do diagrama UML abaixo. A classe deverá possuir
um método construtor que tenha como parâmetro todos os atributos da classe.
Implemente os métodos getters e setters usando o decorator property. Realize
testes de validação da sua classe.
"""

class Pessoa:
    def __init__(self, nome, idade=20, cpf=123456789, cep=None):
        self.nome = nome # público +
        self._idade = idade # protegido (convenção) #
        self.__cpf = cpf # privado -
        self.__cep = cep
    def dizerNome(self):
        print(f'Meu nome é {self.nome}')
              
    def atualizarCEP(self, cep):
        if len(self.__cep) != 8:
            print('Quantidade de dígitos inválida!')
        else:
            self.__cep = cep
            print('CEP atualizado com sucesso!')
              
    def isAdulto(self) -> bool:
        return True if self._idade >= 18 else False
class Pessoa2:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome
    def getCPF(self):
        return self.__cpf
    def setCPF(self, cpf):
        self.__cpf = cpf
"""
p1 = Pessoa2('Jose', '123.456.789-00')
print(f'Meu nome é {p1.getNome()}')
print(f'Meu CPF é {p1.getCPF()}')
p1.setCPF('111.222.333-44')
print(f'Meu novo CPF é {p1.getCPF()}')
print(dir(p1))
#Como acessar externamente um atributo privado em python

print(p1._Pessoa__cpf)
p1.dizerNome()
p1.isAdulto()
"""

class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

p1 = Pessoa('Jose', '123.456.789-00')
print(f'Meu nome é {p1.nome}')
print(f'Meu CPF é {p1.cpf}')
p1.cpf = '111.222.333-44'
print(f'Meu novo CPF é {p1.cpf}')

class Cliente:

    def __init__(self, nome,cpf,renda):
        self.__nome = nome 
        self.__cpf = cpf
        self.__renda = renda 
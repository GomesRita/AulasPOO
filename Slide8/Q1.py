"""
>Escreva uma definição para uma classe denominada Circle, com os atributos center e
radius, onde center é um objeto Point e radius é um número.

>Instancie um objeto Circle, que represente um círculo com o centro em 150, 100 e
raio 75.

>Escreva uma função denominada point_in_circle, que tome um Circle e um Point e
retorne True, se o ponto estiver dentro ou no limite do círculo.

>Escreva uma função chamada rect_in_circle, que tome um Circle e um Rectangle e
retorne True, se o retângulo estiver totalmente dentro ou no limite do círculo.

>Escreva uma função denominada rect_circle_overlap, que tome um Circle e um
Rectangle e retorne True, se algum dos cantos do retângulo cair dentro do círculo.
Ou, em uma versão mais desafiadora, retorne True se alguma parte do retângulo cair
dentro do círculo.
"""
import math;

class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self,altura,largura):
        self.H = altura
        self.l = largura

circulo = Circle([150, 100], 75)
ponto = Point(150,100)
retangulo = Rectangle(100,110)
def point_in_circle(circle_x, circle_y, point):
    verificador = math.sqrt((point.x - circle_x)**2 + (point.y - circle_y)**2)
    if verificador <= circulo.radius:
        print('Está no circulo')
        return True
    else:
        print('Não está no circulo')
        return False

def rect_circle_overlap(circleRadius, largura, altura):
    if circleRadius*2 >= math.sqrt((largura**2)+(altura**2)):
        print('O retângulo cabe')
        return True
    else:
        print('O retângulo não cabe')
point_in_circle(circulo.center[0],circulo.center[1], ponto)
rect_circle_overlap(circulo.radius,retangulo.l, retangulo.H)
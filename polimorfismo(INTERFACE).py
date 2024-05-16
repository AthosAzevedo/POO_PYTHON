class Forma():
    
    def area(self):
        pass
    
class Quadrado(Forma):
    #CONSTRUTOR 
    def __init__(self,lado):
        self.lado = lado
    
    def area(self):
        return  self.lado ** 2
    
class Circulo(Forma):
    
    def __init__(self,raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2
    
quadrado = Quadrado(5)
areaQuadrado = quadrado.area()
print(areaQuadrado)

quadrado2 = Quadrado(7)
areaQuadrado2 = quadrado2.area()
print(areaQuadrado2)

circulo = Circulo(4)
areaCirculo = circulo.area()
print(areaCirculo)

circulo2 = Circulo(6)
areaCirculo2 = circulo2.area()
print(areaCirculo2)
class Animal:
    
    def emitirSom(self):
        print('Barulho de Animal')

class Cachorro(Animal):
    
    def emitirSom(self):
        print('Au Au!!')
        
class Gato(Animal):
    
    def emitirSom(self):
        print('Miau!')
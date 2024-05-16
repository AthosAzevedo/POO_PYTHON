class Carro:
    numero_rodas = 4
    qnts_Passageiro = 5
    
    def acelerar(self):
        print('Acelerando')
    
    def frear(self):
        print('Freando')
        
    def buzinar(self):
        print('Buzinando')
     
class Uno(Carro):
    marca = 'Fiat'
    ano = '1992'
            
carro = Carro()
carro.acelerar()

uno = Uno()
print(uno.ano)
from abc import ABC, abstractmethod   

#implementando o metodo abstrado na classe de estrategia
class Strategy(ABC):
    @abstractmethod
    def tax_calculation(self, number):
        pass 

#implementando a classe da nota fiscal
class Invoice():
    #construtor recebendo uma estrategia inicial do tipo Strategy
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    
    #metodo getter
    @property
    def strategy(self) -> Strategy:
        return self._strategy

    #metodo setter
    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    #metodo para exibir a mensagem com o valor do imposto
    def print_tax_calculation(self, value):
        print('Calculando o valor de '+str(value)+' reais de acordo com o imposto do estado')
        result = self._strategy.tax_calculation(value)
        print(result)

####implementanto o metodo abstrato para cada um das classes####
#calculando imposto de São Paulo
class TaxSP(Strategy):
    def tax_calculation(self, number):
        return 'de São Paulo: '+str((number*0.05))

#calculando imposto do Rio de Janeiro
class TaxRJ(Strategy):
    def tax_calculation(self, number):
        return 'do Rio de Janeiro: '+str((number*0.08))

#calculando imposto do Ceará
class TaxCE(Strategy):
    def tax_calculation(self, number):
        return 'do Ceará: '+str((number*0.1))
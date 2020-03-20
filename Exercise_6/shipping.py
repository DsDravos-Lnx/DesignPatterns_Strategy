from abc import ABC, abstractmethod   

#implementando o metodo abstrado na classe de estrategia
class Strategy(ABC):
    @abstractmethod
    def shipping_calculation(self, shipping_country, country, weight = 1):
        pass 

#implementando a classe de fretes
class Shipping():
    #construtor recebendo uma estrategia inicial do tipo Strategy
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
        self._shipping = {
                            'South': 20.00,
                            'North': 45.00, 
                            'Northeast': 50.00,
                            'Southeast': 25.00,
                            'Midwest': 35.00
                         }
    
    #Getters
    @property
    def strategy(self):
        return self._strategy

    @property
    def shipping(self):
        return self._shipping

    #Setters
    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy
    
    @shipping.setter
    def shipping(self, country, value):
        self._shipping[country] = value


    def print_shipping(self, country, weight = 1):
        print('O valor do envio para regiao é de: ')
        result = self._strategy.shipping_calculation(self._shipping, country, weight)
        print(result)


class StandardShipping(Strategy):
    def shipping_calculation(self, shipping_country, country, weight = 1):
        return shipping_country[country]

class ExpressShipping(Strategy):
    def shipping_calculation(self, shipping_country, country, weight = 1):
        return (shipping_country[country]*weight)

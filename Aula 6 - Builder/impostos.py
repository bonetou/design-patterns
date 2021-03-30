from abc import ABCMeta, abstractmethod

class Imposto:
    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    def calculo_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass

class TemplateDeImpostoCondicional(Imposto):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_outro_imposto(orcamento)
        return self.minima_taxacao(orcamento) + self.calculo_outro_imposto(orcamento)

    @abstractmethod
    def usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07
    
    @abstractmethod
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05 

def IPVX(metodo_ou_funcao):
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50.0
    return wrapper

class ISS(Imposto):
    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_outro_imposto(orcamento)

class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_outro_imposto(orcamento)

# impostos hipotéticos abaixo
class ICPP(TemplateDeImpostoCondicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500
    
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07
    
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

class IKCV(TemplateDeImpostoCondicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1
    
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            return item.valor > 100

from abc import ABCMeta, abstractmethod

class TemplateDeImpostoCondicional:

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        return self.minima_taxacao(orcamento)

    @abstractmethod
    def usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07
        
    @abstractmethod
    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

class ISS:
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ICMS:
    def calcula(self, orcamento):
        return orcamento.valor * 0.06

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

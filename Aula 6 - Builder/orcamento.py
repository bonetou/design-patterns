from abc import ABCMeta, abstractmethod

class EstadoDeUmOrcamento:

    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass
    
    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass

class EmAprovacao(EstadoDeUmOrcamento):

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado = Reprovado()
    
    def finaliza(self, orcamento):
        raise Exception('Orçamento em aprovaçao nao pode ser finalizado')
    
class Aprovado(EstadoDeUmOrcamento):

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception('Orçamento ja está aprovado')
    
    def reprova(self, orcamento):
        raise Exception('Orçamento aprovado não pode ser reprovado')

    def finaliza(self, orcamento):
        orcamento.estado = Finalizado()
    
class Reprovado(EstadoDeUmOrcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser reprovado')
    
    def reprova(self, orcamento):
        raise Exception('Orçamento já está reprovado')
    
    def finaliza(self, orcamento):
        self.estado = Finalizado()
    
class Finalizado(EstadoDeUmOrcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser aprovado')
    
    def reprova(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser reprovado')
    
    def finaliza(self, orcamento):
        raise Exception('Orçamento já está finalizado')
    
class Orcamento:

    def __init__(self):
        self.__itens = []
        self.estado = EmAprovacao()
        self.__desconto_extra = 0
    
    def aprova(self):
        self.estado.aprova(self)
    
    def reprova(self):
        self.estado.reprova(self)

    def finaliza(self):
        self.estado.finaliza(self)

    def aplica_desconto_extra(self):
        self.estado.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto
    
    @property
    def valor(self):
        total = 0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra
        
    @property
    def total_itens(self):
        return len(self.__itens)

    def obter_itens(self):
        return tuple(self.__itens)
    
    def adiciona_item(self, item):
        self.__itens.append(item)

class Item:
    
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome
        
    @property
    def valor(self):
        return self.__valor
    

if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 2', 250))

    print('Desconto em Aprovaçao')
    print(orcamento.valor)
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)

    orcamento.aprova()
    

    #desconto extra para orçamento ja aprovado deve ser maior
    print('Desconto depois de Aprovado')
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 2', 250))

    print(orcamento.valor)
    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)

    orcamento.finaliza()
    #orcamento.aprova() -> raise Exception: orcamento finalizado nao pode ser aprovado 

    
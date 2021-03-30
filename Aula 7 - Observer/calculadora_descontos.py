from descontos import DescontoMaisDeCincoItens, DescontoMaisDeQuinhentosReais, SemDesconto

class CalculadoraDescontos:

    def calcula(self, orcamento):
        desconto = DescontoMaisDeCincoItens(
            DescontoMaisDeQuinhentosReais(
                SemDesconto()
            )
        ).calcula(orcamento)
        return desconto

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 100))
    orcamento.adiciona_item(Item('ITEM 1', 100))
    orcamento.adiciona_item(Item('ITEM 1', 100))
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 1', 50))
    
    calculadora = CalculadoraDescontos()
    desconto = calculadora.calcula(orcamento)

    print(f'Desconto: {round(desconto, 2)} R$')
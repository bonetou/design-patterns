from impostos import ISS, ICMS, ICPP, IKCV

class CalculadoraImpostos:

    def realiza_calculo(self, orcamento, tipo_imposto):

        imposto_calculado = tipo_imposto.calcula(orcamento)
        print(imposto_calculado)

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    calculadora = CalculadoraImpostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 2', 250))

    print('IMPOSTOS - ISS ICMS')
    calculadora.realiza_calculo(orcamento, ISS())
    calculadora.realiza_calculo(orcamento, ICMS())
    print('IMPOSTOS - ICPP E IKCV')
    calculadora.realiza_calculo(orcamento, ICPP())
    calculadora.realiza_calculo(orcamento, IKCV())

from impostos import ISS, ICMS

class CalculadoraImpostos:

    def realiza_calculo(self, orcamento, tipo_imposto):

        imposto_calculado = tipo_imposto.calcula(orcamento)
        print(imposto_calculado)

if __name__ == '__main__':

    from orcamento import Orcamento

    calculadora = CalculadoraImpostos()
    orcamento = Orcamento(500)
    calculadora.realiza_calculo(orcamento, ISS())
    calculadora.realiza_calculo(orcamento, ICMS())

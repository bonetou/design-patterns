from datetime import date

class Item:

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valor(self):
        return self.__valor

class NotaFiscal:

    def __init__(self, razao_social, cnpj, itens, data_emissao=date.today(), detalhes=''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_emissao = data_emissao
        self.__itens = itens
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota maior do que 20 caracteres')
        self.__detalhes = detalhes

    @property
    def razao_social(self):
        return self.__razao_social
    
    @property 
    def cnpj(self):
        return self.__cnpj
    
    @property
    def detalhes(self):
        return self.__detalhes

if __name__ == '__main__':

    from criador_nota_fiscal import CriadorNotaFiscal

    itens = [
        Item('ITEM A', 100),
        Item('ITEM B', 200)
    ]

    nota_fiscal = NotaFiscal(
        razao_social='Boneto Co.',
        cnpj='01120391029301',
        itens=itens
    )
    
    nota_fiscal_com_builder = (CriadorNotaFiscal()
                            .com_razao_social('Boneto Co.')
                            .com_cnpj('01120391029301')
                            .com_itens(itens)
                            .constroi())
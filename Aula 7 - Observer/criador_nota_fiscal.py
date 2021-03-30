from datetime import date
from nota_fiscal import NotaFiscal

class CriadorNotaFiscal:

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_emissao = None
        self.__itens = None
        self.__detalhes = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_emissao(self, data_emissao):
        self.__data_emissao = data_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self
    
    def constroi(self):
        if self.__razao_social is None:
            raise Exception('Razão social deve ser preenchida')
        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchido')
        if self.__itens is None:
            raise Exception('Itens devem ser preenchidos')
        if self.__data_emissao is None:
            self.__data_emissao = date.today()
        if self.__detalhes is None:
            self.__detalhes = ''
        
        return NotaFiscal(razao_social=self.__razao_social, 
            cnpj=self.__cnpj, 
            itens=self.__itens,
            data_emissao=self.__data_emissao,
            detalhes=self.__detalhes
        )
    

#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Medicamento:
    
    __medicamentos = []
    def __init__(self,nome:str,composto:str,laboratorio:str,descricao:str, valor:float, quantidade:int):
        """
        Função para construir objeto Cliente.
        Parâmetros:
          nome: Recebe o nome do medicamento
          composto: Recebe o composto do medicamento
          laboratorio: Recebe o nome do laboratorio
          descricao: Recebe a descrição do medicamento
        Retorno: O objeto recem criado
        """
    
        self.__nome = nome
        self.__composto = composto
        self.__laboratorio = laboratorio
        self.__descricao = descricao
        self.__valor = valor
        self.__quantidade = quantidade
        __class__.__medicamentos.append(self)
        
    @classmethod
    def medicamentos(cls:str) -> list:
        return [str(item) for item in cls.__medicamentos]
    
    
    def __str__(self) -> str:
        """
        Função para apresentar através de print o objeto
        Retorno: String contendo nome, o composto, o laboratorio e a descrição do medicamento
        """
        return f' Medicamento:{self.__nome} \n Composto:{self.__composto} \n Laboratorio:{self.__laboratorio} \n Descricao:{self.__descricao} \n Valor:{self.__valor} \n Quantidade:{self.__quantidade}'


    @property
    def nome(self) -> str:
        """
        Função para recuperar o nome do medicamento
        Retorno: Nome do medicamento
        """
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        """
        Função para definir o nome do medicamento
        Retorno: None
        """
        self.__nome = nome
        

    @property
    def composto(self) -> str:
        """
        Função para recuperar o nome composto do medicamento
        Retorno: Composto do medicamento
        """
        return self.__composto

    @composto.setter
    def composto(self, composto:str):
        """
        Função para definir o composto do medicamento
        Retorno: None
        """
        self.__composto = composto
        

    @property
    def laboratorio(self) -> str:
        """
        Função para recuperar o nome composto do medicamento
        Retorno: Composto do medicamento
        """
        return self.__laboratorio

    @laboratorio.setter
    def laboratorio(self, laboratorio:str):
        """
        Função para definir o composto do medicamento
        Retorno: None
        """
        self.__laboratorio = laboratorio
        
    
    @property
    def descricao(self) -> str:
        """
        Função para recuperar a descrição do medicamento
        Retorno: Descrição do medicamento
        """
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao:str):
        """
        Função para definir a Descrição do medicamento
        Retorno: None
        """
        self.__descricao = descricao
        

    @property
    def valor(self) -> str:
        """
        Função para recuperar o valor do medicamento
        Retorno: Valor do medicamento
        """
        return self.__valor

    @valor.setter
    def valor(self, valor:str):
        """
        Função para definir o valor do medicamento
        Retorno: None
        """
        self.__valor = valor
        
        
    @property
    def quantidade(self) -> str:
        """
        Função para recuperar a quantidade do medicamento
        Retorno: Quantidade do medicamento
        """
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade:str):
        """
        Função para definir a quantidade do medicamento
        Retorno: None
        """
        self.__quantidade = quantidade
    
    
    @classmethod
    def busca(cls, busca:str) -> str:
        """
        Função para buscar o cliente de acordo com um criterio (string)
        Parâmetros:
          busca: Recebe um string que será utilizado para realizar a busca.
        Retorno: Lista de objetos cliente que atendem ao critério apresentado.
        """
        return [medicamento for medicamento in cls.__medicamentos if busca.upper() in medicamento.__nome.upper() or busca.upper() in medicamento.__composto.upper() or busca.upper() in medicamento.__laboratorio.upper() or busca.upper() in medicamento.__descricao.upper()]
        
        
        

        
class MedicamentoQuimio(Medicamento):
    
    def __init__(self, nome:str, composto:str, laboratorio:str, descricao:str, receita:bool):
        super().__init__(nome, composto, laboratorio, descricao, valor, quantidade)
        self.__receita = receita
        
    @property
    def receita(self) -> bool:
        """
        Função para recuperar a necessidade de receita para compra do medicamento
        Retorno: Necessidade de receita ou não
        """
        return self.__receita

    @receita.setter
    def receita(self, receita:bool):
        """
        Função para definir se o medicamento precisa ou não de receita para ser vendido 
        Retorno: None
        """
        self.__receita = receita
        
    def __str__(self) -> str:
        """
        Função para apresentar através de print o objeto
        Retorno: String contendo nome, o composto, o laboratorio e a descrição do medicamento
        """
        return f' Medicamento:{self.nome} \n Composto:{self.composto} \n Laboratorio:{self.laboratorio} \n Descricao:{self.descricao} \n Necessita receita:{self.__receita} \n Valor:{self.__valor} \n Quantidade:{self.__quantidade}'



# In[ ]:





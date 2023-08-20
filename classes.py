"""
Importação de bibliotecas
"""
from datetime import datetime

"""
Classe Cliente
"""
class Cliente:
  def __init__(self, cpf:str, nome:str, nascimento:str):
    """
    Função para construir objeto Cliente.
    Parâmetros:
      cpf: Recebe o CPF em formato de string
      nome: Recebe o nome
      nascimento: Recebe data de nascimento em formato de string (DD/MM/YYYY)
    Retorno: O objeto recem criado
    """
    self.cpf = cpf
    self.nome = nome
    self.nascimento = nascimento
    __class__.__clientes.append(self)

  __cpf = None
  __nome = None
  __nascimento = None
  __clientes = []
  
  def __str__(self) -> str:
    """
    Função para apresentar através de print o objeto
    Retorno: String contendo nome e CPF do cliente
    """
    return f'{self.nome} ({self.cpf})'

  @property
  def cpf(self) -> str:
    """
    Função para recuperar o CPF do Cliente
    Retorno: CPF do Cliente
    """
    return self.__cpf

  @cpf.setter
  def cpf(self, cpf:str):
    """
    Função para definir o CPF do cliente, apresentando erro caso não passe pelo validador.
    Parâmetros:
      cpf: Recebe o CPF em formato de string
    """
    if self.validadorCPF(cpf):
      self.__cpf = cpf
    else:
      raise KeyError('CPF inválido!!')

  @property
  def nome(self) -> str:
    """
    Função para recuperar o nome do Cliente
    Retorno: Nome do Cliente
    """
    return self.__nome

  @nome.setter
  def nome(self, nome:str):
    """
    Função para definir o nome do cliente.
    Parâmetros:
      nome: Recebe o nome
    """
    self.__nome = nome

  @property
  def nascimento(self) -> str:
    """
    Função para recuperar o nascimento do Cliente
    Retorno: Nascimento do Cliente
    """
    return self.__nascimento

  @nascimento.setter
  def nascimento(self, nascimento:str):
    """
    Função para definir o data de nascimento do cliente, apresentando erro caso não passe pelo validador.
    Parâmetros:
      nascimento: Recebe o nascimento em formato de string
    """
    if self.validadorData(nascimento):
      self.__nascimento = nascimento
    else:
      raise ZeroDivisionError('Erro de divisão por zero!!')

  def idade(self) -> int:
    """
    Função para calcular e retorna a idade do cliente de acordo com a data de nascimento.
    Retorno: A idade em anos do cliente
    """
    return (datetime.now() - datetime.strptime(self.__nascimento, "%d/%m/%Y")).days // 365

  @classmethod
  def busca(cls, busca:str) -> str:
    """
    Função para buscar o cliente de acordo com um criterio (string)
    Parâmetros:
      busca: Recebe um string que será utilizado para realizar a busca.
    Retorno: Lista de objetos cliente que atendem ao critério apresentado.
    """
    return [cliente for cliente in cls.__clientes if busca.upper() in cliente.nome.upper() or busca.upper() in cliente.cpf.upper() or busca.upper() in cliente.nascimento.upper()]

  @staticmethod
  def validadorData(nascimento:str) -> bool:
    """
    Função para validar se a string recebida de fato representa uma data válida
    Parâmetros:
      nascimento: Data de nascimento em formato de string
    Retorno: Bolleano indicado se a data é válida.
    """
    if len(nascimento) == 10 and nascimento.count('/') == 2:
      dia, mes, ano = nascimento.split('/')
      dia, mes, ano = int(dia), int(mes), int(ano)
      if mes in [1,3,5,7,8,10,12] and dia >= 1 and dia <= 31:
        return True
      elif mes in [4,6,9,11] and dia >= 1 and dia <= 30:
        return True
      elif mes in [2] and dia >= 1 and dia <= 28:
        return True
      elif mes in [2] and dia == 29 and ((ano%4 or not ano%100) or (ano%400)):
        return True
    return False

  @staticmethod
  def validadorCPF(cpf:str) -> bool:
    """
    Função para validar se a string recebida de fato representa um CPF válido.
    Parâmetros:
      nascimento: CPF em formato de string
    Retorno: Bolleano indicado se o CPF é válido.
    """
    return True

"""
Classe laboratório
"""
class Laboratorio:

  __nome = None
  __endereco = None
  __telefone = None
  __cidade = None
  __estado = None
  __laboratorios = []

  def __init__(self, nome:str, endereco:str, telefone:str, cidade:str, estado:str):
    """
    Função para construir objeto Laboratorio.
    Parâmetros:
      nome: Recebe o CPF em formato de string
      endereco: Recebe o nome
      telefone: Recebe data de nascimento em formato de string (DD/MM/YYYY)
      cidade: Recebe data de nascimento em formato de string (DD/MM/YYYY)
      estado: Recebe data de nascimento em formato de string (DD/MM/YYYY)
    Retorno: O objeto recém criado.
    """
    self.nome = nome
    self.endereco = endereco
    self.telefone = telefone
    self.cidade = cidade
    self.estado = estado
    __class__.__laboratorios.append(self)

  def __str__(self) -> str:
    """
    Função para apresentar através de print o objeto
    Retorno: String contendo Nome, Cidade e Estado do laboratório.
    """
    return f'{self.nome} (Telefone: {self.telefone} | Endereço: {self.endereco} | Cidade: {self.cidade} | Estado: {self.estado})'

  @property
  def nome(self) -> str:
    """
    Função para recuperar o nome do Laboratório.
    Retorno: Nome do Laboratório
    """
    return self.__nome

  @nome.setter
  def nome(self, nome:str):
    """
    Função para definir o nome do laboratório.
    Parâmetros:
      nome: Recebe o nome do laboratório
    """
    self.__nome = nome

  @property
  def endereco(self) -> str:
    """
    Função para recuperar o endereço do Laboratório.
    Retorno: Endereço do Laboratório
    """
    return self.__endereco

  @endereco.setter
  def endereco(self, endereco:str):
    """
    Função para definir o endereço do laboratório.
    Parâmetros:
      nome: Recebe o endereço do laboratório
    """
    self.__endereco = endereco

  @property
  def telefone(self) -> str:
    """
    Função para recuperar o telefone do Laboratório.
    Retorno: Telefone do Laboratório
    """
    return self.__telefone

  @telefone.setter
  def telefone(self, telefone:str):
    """
    Função para definir o telefone do laboratório.
    Parâmetros:
      nome: Recebe o telefone do laboratório
    """
    self.__telefone = telefone

  @property
  def cidade(self) -> str:
    """
    Função para recuperar a cidade do Laboratório.
    Retorno: Cidade do Laboratório
    """
    return self.__cidade

  @cidade.setter
  def cidade(self, cidade:str):
    """
    Função para definir o cidade do laboratório.
    Parâmetros:
      nome: Recebe a cidade do laboratório
    """
    self.__cidade = cidade

  @property
  def estado(self) -> str:
    """
    Função para recuperar a estado do Laboratório.
    Retorno: Estado do Laboratório
    """
    return self.__estado

  @estado.setter
  def estado(self, estado:str):
    """
    Função para definir o estado do laboratório.
    Parâmetros:
      nome: Recebe o estado do laboratório
    """
    self.__estado = estado

  @classmethod
  def busca(cls, busca:str) -> list:
    """
    Função para buscar o laboratório de acordo com um criterio (string)
    Parâmetros:
      busca: Recebe um string que será utilizado para realizar a busca.
    Retorno: Lista de objetos laboratório que atendem ao critério apresentado.
    """
    return [laboratorio for laboratorio in cls.__laboratorios if busca.upper() in laboratorio.nome.upper()]
  
"""
Classe medicamento
"""
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

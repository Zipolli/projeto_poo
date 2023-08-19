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
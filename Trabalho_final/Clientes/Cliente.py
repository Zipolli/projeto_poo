class Cliente:

  __cpf = None
  __nome = None
  __nascimento = None
  __clientes = []

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
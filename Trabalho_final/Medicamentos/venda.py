class Venda:

  __produtos = None
  __cliente = None
  __data_hora = None
  __total_original = None
  __desconto = None
  __vendas = []

  def __init__(self, produtos:list, cliente:Cliente):
    """
    Função para construir objeto que registra uma venda.
    Parâmetros:
      produtos: Receber uma lista contendo lista com 2 itens (Objeto Medicamento, Qtd Venda)
      cliente: Recebe um OBJETO do tipo Cliente.
    Retorno: O objeto recém criado.
    """
    self.produtos = produtos #Lista de Lista onde cada lista interna é uma composicao de Objeto Meicamento e quantidade [[Cimegripe, 10],[Losartana,2]]
    self.cliente = cliente
    self.data_hora = datetime.now()
    self.calculaTotalOriginal()
    self.calculaDesconto()
    __class__.__vendas.append(self)

  def calculaTotalOriginal(self):
    self.__total_original = valor_resultado

  def calculaDesconto(self):
    self.__desconto = valor_desconto

  def valor_pagar(self):
    return self.__total_original - self.__desconto
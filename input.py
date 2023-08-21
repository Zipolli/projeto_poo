#Importando as classes
from classes import Cliente, Laboratorio, Medicamento, MedicamentoQuimio, Venda

#Cadastro de clientes
def cadastrar_cliente():
    cpf = input("Digite o CPF do cliente: ")
    nome = input("Digite o nome do cliente: ")
    nascimento = input("Digite a data de nascimento (DD/MM/YYYY) do cliente: ")

    cliente = Cliente(cpf, nome, nascimento)
    print()
    print("Cliente cadastrado com sucesso!")

#Busca de clientes
def busca_cliente():
    busca = input("Digite o critério de busca (CPF, nome ou nascimento): ")
    resultados = Cliente.busca(busca)
    if resultados:
        print("Resultados da busca:")
        resultados_ordenados = sorted(resultados, key=lambda cliente: cliente.nome)
        for cliente in resultados_ordenados:
            print(cliente)
    else:
        print("Nenhum cliente encontrado.")

#Cadastro de laboratório
def cadastrar_laboratorio():
    nome = input("Digite o nome do laboratório: ")
    endereco = input("Digite o endereço: ")
    telefone = input("Digite o telefone (XXxxxxxxxxx): ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado (XX): ")
    
    laboratorios = Laboratorio(nome, endereco, telefone, cidade, estado)
    print()
    print("Laboratório cadastrado com sucesso!")

#Busca de laboratório    
def busca_laboratorio():
    busca = input("Digite o nome do laboratório: ")
    resultados = Laboratorio.busca(busca)
    if resultados:
        print("Resultados da busca: ")
        resultados_ordenados = sorted(resultados, key=lambda laboratorio: laboratorio.nome)
        for laboratorio in resultados_ordenados:
            print(laboratorio)
            
    else:
        print("Nenhum laboratório encontrado.")
        
#Cadastro de medicamento fitoterápico
def cadastrar_medicamento():
    nome = input("Digite o nome do medicamento: ")
    composto = input("Digite o nome do composto: ")
    laboratorio = input("Digite o nome do labortatório: ")
    descricao = input("Digite a descrição: ")
    valor = input("Digite o valor unitário (XX.XX): R$ ")
    quantidade = input("Digite a quantidade em estoque: ")
    
    medicamentos = Medicamento(nome, composto, laboratorio, descricao, valor, quantidade)
    print()
    print("Medicamento cadastrado com sucesso!")

#Busca de medicamento fitoterápico
def busca_medicamento():
    busca = input("Digite o nome do medicamento: ")
    resultados = Medicamento.busca(busca)
    if resultados:
        print("Resultados da busca: ")
        resultados_ordenados = sorted(resultados, key=lambda medicamentos: medicamentos.nome)
        for medicamentos in resultados_ordenados:
            print(medicamentos)
            
    else:
        print("Nenhum medicamento encontrado.")
        
#Cadastro de medicamento quimioterápico
def cadastrar_quimioterapico():
    nome = input("Digite o nome do medicamento: ")
    composto = input("Digite o nome do composto: ")
    laboratorio = input("Digite o nome do labortatório: ")
    descricao = input("Digite a descrição: ")
    receita = input("Precisa de receita médica (Sim / Não)? ")
    if receita == 'Sim':
        return True
    elif receita == 'Não':
        return False
    else:
        print("Resposta inválida. Por favor, responda 'Sim' ou 'Não'.")            
    valor = input("Digite o valor unitário (XX.XX): R$ ")
    quantidade = input("Digite a quantidade em estoque: ")
    
    medicamentos = Medicamento(nome, composto, laboratorio, descricao, receita, valor, quantidade)
    print()
    print("Medicamento cadastrado com sucesso!")

#Busca de medicamento fitoterápico
def busca_quimioterapico():
    busca = input("Digite o nome do medicamento: ")
    resultados = Medicamento.busca(busca)
    if resultados:
        print("Resultados da busca: ")
        resultados_ordenados = sorted(resultados, key=lambda medicamentos: medicamentos.nome)
        for medicamentos in resultados_ordenados:
            print(medicamentos)
            
    else:
        print("Nenhum medicamento encontrado.")


def venda_medicamento():
    info_cliente = str(input("Digite o nome completo ou CPF do cliente: "))
    if len(Cliente.busca(info_cliente)) == 0:
        return print("Cliente não encontrado!")
    else:
        produtos=[]
        cliente = Cliente.busca(info_cliente)
        qtd_medicamentos = input("Digite quantos medicamentos distintos o cliente deseja comprar: ")
    for i in range(0,len(qtd_medicamentos)):
        lista_produto=[]
        info_medicamento = str(input("Digite o nome, composto do medicamento {}: ".format(i)))
        
        if len(Medicamento.busca(info_medicamento)) == 0:
            return print("Medicamento não encontrado!")

        else:
            medicamento = Medicamento.busca(info_medicamento)
            qtd_venda = int(input("Digite a quantidade do medicamento: "))
            preco_unitario = medicamento.valor

        lista_produto=[medicamento,qtd_venda,preco_unitario]
        produtos.append(lista_produto)
    
    venda = Venda(produtos, cliente)
    venda.finaliza_venda()
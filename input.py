#Importando as classes
from classes import Cliente, Laboratorio, Medicamento, MedicamentoQuimio

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
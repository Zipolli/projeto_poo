from classes import Cliente, Laboratorio, Medicamento
from input import cadastrar_cliente, busca_cliente, cadastrar_laboratorio, busca_laboratorio, cadastrar_medicamento, busca_medicamento, cadastrar_quimioterapico, busca_quimioterapico, venda_medicamento

def main():
    while True:
        print("Menu cadastros:")
        print()
        print("1. Cliente")
        print("2. Laboratório")
        print("3. Medicamento fitoterápico")
        print("4. Medicamento quimiterápico")
        print()
        print("Menu de busca:")
        print()
        print("5. Cliente")
        print("6. Laboratório")
        print("7. Medicamentos")
        print("8. Medicamento fitoterápico")
        print("9. Medicamento quimiterápico")
        print()
        print("Menu de relatórios")
        print("10. Vendas de medicamentos")
        print("11. Vendas de medicamentos fitoterápicos")
        print("12. Vendas de medicamentos quimioterápicos")
        print("13. Total de vendas")
        print()
        print("Menu de vendas")
        print("14. Vendas de medicamentos")
        print("15. Finalizar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_laboratorio()
        elif opcao == "3":
            cadastrar_medicamento()
        elif opcao == "4":
            cadastrar_quimioterapico()
        elif opcao == "5":
            busca_cliente()
        elif opcao == "6":
            busca_laboratorio()
        elif opcao == "7":
            busca_medicamento()
        elif opcao == "8":
            busca_quimioterapico()
        elif opcao == "14":
            venda_medicamento()
        elif opcao == "15":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    cliente01 = Cliente('33736923856', 'Leonardo Zipolli', '25/01/1986')
    cliente02 = Cliente('12345678910', 'Claudio Soares', '26/02/1956')
    cliente03 = Cliente('01234567891', 'Maria da Graça', '06/08/1963')
    medicamento01 = Medicamento()
    main()
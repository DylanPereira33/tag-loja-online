from produtos import listar_produtos, escolher_produto
from modelos import Carrinho, Cliente, PagamentoPix, PagamentoCartao, PagamentoBoleto, Pedido
from funcoes_funcionais import calcular_total_carrinho

carrinho = Carrinho()
cliente = Cliente("Dylan", "dylan@email.com")  # cliente fixo para simplificar

def menu():
    while True:
        print("\n=== Loja Online ===")
        print("1. Listar produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Remover produto do carrinho")
        print("4. Ver carrinho (itens e total)")
        print("5. Finalizar compra (Pedido)")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            listar_produtos()
            codigo = input("Digite o código do produto: ")
            produto = escolher_produto(codigo)
            if produto:
                carrinho.adicionar(produto, 1)
                print("Produto adicionado!")
        elif opcao == "3":
            nome = input("Digite o nome do produto para remover: ")
            carrinho.remover(nome)
            print("Produto removido!")
        elif opcao == "4":
            print("\n--- Seu Carrinho ---")
            for item in carrinho.itens:
                print(f"{item.qtd}x {item.produto.get_nome()} - Subtotal: R${item.subtotal():.2f}")
            total = calcular_total_carrinho(carrinho)
            print(f"Total da compra: R${total:.2f}")
        elif opcao == "5":
            total = calcular_total_carrinho(carrinho)
            print(f"Valor final: R${total:.2f}")
            print("Escolha forma de pagamento:")
            print("1. Pix\n2. Cartão\n3. Boleto")
            forma = int(input("Opção: "))

            match forma:
                case 1: pagamento = PagamentoPix()
                case 2: pagamento = PagamentoCartao()
                case 3: pagamento = PagamentoBoleto()
                case _: 
                    print("Forma inválida!")
                    continue

            pedido = Pedido(cliente, carrinho, pagamento)
            pedido.confirmar_pedido()
            pedido.mostrar_resumo()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
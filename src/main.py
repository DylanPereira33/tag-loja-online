from produtos import listar_produtos, escolher_produto
from modelos import Carrinho, Cliente, PagamentoPix, PagamentoCartao, PagamentoBoleto, Pedido
from funcoes_funcionais import calcular_total_carrinho, aplicar_desconto

carrinho = Carrinho()
cliente = Cliente("Joao das Coves", "joaodascoves@email.com")  # cliente fixo para simplificar

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

        match opcao:
            case "1":
                listar_produtos()

            case "2":
                while True:   # LOOP INTERNO PARA COMPRAS SEQUENCIAIS
                    listar_produtos()
                    codigo = input("Código: ")
                    produto = escolher_produto(codigo)

                    if produto:
                        carrinho.adicionar(produto, 1)

                    print("\n1. Continuar comprando")
                    print("2. Voltar ao menu")

                    escolha = input("Opção: ")

                    if escolha == "1":
                        continue   # volta ao início do loop interno

                    elif escolha == "2":
                        break      # retorna ao menu principal

                    else:
                        print("Opção inválida.")
            case "3":
                codigo = input("Digite o código do produto para remover: ")
                if carrinho.remover(codigo):
                    print("Produto removido!")
                else:
                    print("Código não encontrado no carrinho.")


            case "4":
                print("\n--- Seu Carrinho ---")

                if len(carrinho.itens) == 0:
                    print("Carrinho vazio.")
                else:
                    for item in carrinho.itens:
                        print(f"{item.qtd}x {item.produto.get_nome()} - R${item.subtotal():.2f}")

                    # PARADIGMA FUNCIONAL: reduce para somar valores
                    total = calcular_total_carrinho(carrinho)
                    print(f"Total: R${total:.2f}")

            case "5":
                total = calcular_total_carrinho(carrinho)
                print("Aplicando desconto de 10%.")
                desconto10 = aplicar_desconto(lambda v: v * 0.9)   # Uso real da função funcional aplicar_desconto
                total = desconto10(total)
                print(f"Valor final: R${total:.2f}")
                print("Escolha forma de pagamento:")
                print("1. Pix\n2. Cartão\n3. Boleto")
                forma = int(input("Opção: "))

                if forma == 1:
                    pagamento = PagamentoPix()
                elif forma == 2:
                    pagamento = PagamentoCartao()
                elif forma == 3:
                    pagamento = PagamentoBoleto()
                else:
                    print("Forma inválida!")
                    continue

                pedido = Pedido(cliente, carrinho, pagamento)
                pedido.confirmar_pedido()
                pedido.mostrar_resumo()

                # Limpa carrinho após finalizar
                carrinho.limpar()

            case "6":
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")

menu()

# Paradigma Orientado a Objetos

class Produto:
    def __init__(self, codigo, nome, preco, categoria, descricao, estoque):
        self._codigo = codigo
        self._nome = nome
        self._preco = preco
        self._categoria = categoria
        self._descricao = descricao
        self._estoque = estoque

    def get_codigo(self): return self._codigo
    def get_nome(self): return self._nome
    def get_preco(self): return self._preco
    def get_categoria(self): return self._categoria
    def get_descricao(self): return self._descricao

    def debitar_estoque(self, qtd):
        if self._estoque >= qtd:
            self._estoque -= qtd
        else:
            print("Estoque insuficiente!")

    def __str__(self):
        return f"[{self._codigo}] {self._nome} - R${self._preco:.2f} ({self._categoria}) | Estoque: {self._estoque}"

class ProdutoFisico(Produto):
    def calcular_valor_final(self):
        return self.get_preco() + 10  # frete fixo

class ProdutoDigital(Produto):
    def calcular_valor_final(self):
        return self.get_preco()  # sem frete

class ItemCarrinho:
    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd
    def subtotal(self): return self.produto.calcular_valor_final() * self.qtd

class Carrinho:
    def __init__(self):
        self.itens = []
    def adicionar(self, produto, qtd=1):
        self.itens.append(ItemCarrinho(produto, qtd))
        produto.debitar_estoque(qtd)
    def remover(self, nome_produto):
        self.itens = [i for i in self.itens if i.produto.get_nome() != nome_produto]
    def calcular_total(self):
        return sum(i.subtotal() for i in self.itens)

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Pagamento:
    def processar_pagamento(self, valor):
        raise NotImplementedError("Implementar nas subclasses")

class PagamentoPix(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Pagamento de R${valor:.2f} via Pix realizado com sucesso!")

class PagamentoCartao(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Pagamento de R${valor:.2f} via Cartão aprovado!")

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Boleto gerado no valor de R${valor:.2f}.")

# --- Nova classe Pedido ---
class Pedido:
    def __init__(self, cliente, carrinho, pagamento):
        self.cliente = cliente
        self.itens = carrinho.itens
        self.total = carrinho.calcular_total()
        self.pagamento = pagamento
        self.status = "Pendente"

    def confirmar_pedido(self):
        self.pagamento.processar_pagamento(self.total)
        self.status = "Pago"

    def mostrar_resumo(self):
        print(f"\n--- Resumo do Pedido ---")
        print(f"Cliente: {self.cliente.nome} ({self.cliente.email})")
        for item in self.itens:
            print(f"{item.qtd}x {item.produto.get_nome()} - R${item.subtotal():.2f}")
        print(f"Total: R${self.total:.2f} | Status: {self.status}")


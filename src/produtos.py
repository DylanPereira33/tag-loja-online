
# Paradigma Estruturado: funções e controle clássico
from modelos import ProdutoFisico, ProdutoDigital


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

    def __str__(self):
        return f"[{self._codigo}] {self._nome} - R${self._preco:.2f} ({self._categoria}) | Estoque: {self._estoque}"
        
produtos = [
    ProdutoFisico("P001", "Livro Python", 50, "Livros", "Aprenda Python", 10),
    ProdutoDigital("P002", "Curso Online JS", 100, "Cursos", "Curso completo de JS", 5),
    ProdutoFisico("P003", "Notebook", 3000, "Eletrônicos", "Notebook gamer", 2)
]

def listar_produtos():
    print("\n--- Produtos Disponíveis ---")
    for p in produtos:
        print(p)

def escolher_produto(codigo):
    for p in produtos:
        if p.get_codigo() == codigo:
            return p
    print("Código inválido!")
    return None
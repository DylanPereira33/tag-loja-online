"""
Teste básico para verificar se as classes OO estão funcionando
Execute: python teste_basico.py
"""

import sys
sys.path.append('src')

from orientado_objetos.models.produto_fisico import ProdutoFisico
from orientado_objetos.models.produto_digital import ProdutoDigital

print("="*60)
print("TESTE 1: Criando Produto Físico")
print("="*60)

livro = ProdutoFisico(
    codigo=1,
    nome="Livro Python Fluente",
    descricao="Livro avançado de Python",
    preco=89.90,
    estoque=10,
    categoria="Livros",
    peso_kg=0.8
)

print(f"Produto criado: {livro}")
print(f"   Detalhes: {livro.obter_detalhes_especificos()}")
print(f"   Valor final (1 unidade): R$ {livro.calcular_valor_final(1):.2f}")
print(f"   Valor final (3 unidades): R$ {livro.calcular_valor_final(3):.2f}")

print("\n" + "="*60)
print("TESTE 2: Criando Produto Digital")
print("="*60)

curso = ProdutoDigital(
    codigo=3,
    nome="Curso Python Data Science",
    descricao="Curso completo",
    preco=297.00,
    estoque=999,
    categoria="Cursos",
    tamanho_mb=3500
)

print(f"Produto criado: {curso}")
print(f"   Detalhes: {curso.obter_detalhes_especificos()}")
print(f"   Valor final (1 unidade): R$ {curso.calcular_valor_final(1):.2f}")
print(f"   Link download: {curso.gerar_link_download()}")

print("\n" + "="*60)
print("TESTE 3: Testando POLIMORFISMO")
print("="*60)

# Lista com produtos de tipos diferentes
produtos = [livro, curso]

print("\nCalculando valor final de cada produto (POLIMORFISMO):")
for produto in produtos:
    # Aqui está o POLIMORFISMO em ação!
    # Mesma chamada, comportamento diferente
    valor = produto.calcular_valor_final(2)
    print(f"  - {produto.nome}: R$ {valor:.2f}")

print("\n" + "="*60)
print("TESTE 4: Testando Encapsulamento (Getters/Setters)")
print("="*60)

print(f"Preço original do livro: R$ {livro.preco:.2f}")

# Usando setter para alterar preço
livro.preco = 79.90
print(f"Preço após desconto: R$ {livro.preco:.2f}")

# Tentando setar valor inválido
try:
    livro.preco = -10
except ValueError as e:
    print(f"Erro capturado (encapsulamento funcionando): {e}")

print("\n" + "="*60)
print("TESTE 5: Testando débito de estoque")
print("="*60)

print(f"Estoque atual: {livro.estoque}")

if livro.debitar_estoque(3):
    print(f"Debitado 3 unidades. Novo estoque: {livro.estoque}")
else:
    print("Estoque insuficiente")

if livro.debitar_estoque(100):
    print("✅ Debitado 100 unidades")
else:
    print(f"Estoque insuficiente! Disponível: {livro.estoque}")

print("\n" + "="*60)
print("TODOS OS TESTES PASSARAM!")
print("="*60)
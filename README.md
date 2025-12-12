# Loja Online Multi-Paradigma (Python)

Projeto acadêmico demonstrando o uso integrado dos paradigmas **Estruturado**, **Funcional** e **Orientado a Objetos** em uma aplicação simples de loja online.

## Funcionalidades

* Listagem de produtos
* Adicionar / remover itens do carrinho
* Cálculo de total (com descontos, frete e estoques)
* Finalização de pedido com diferentes formas de pagamento (Pix, Cartão, Boleto)

## Estrutura de Pastas

```
├── funcoes_funcionais.py   # Paradigma Funcional
├── modelos.py              # Paradigma OO (classes, herança, polimorfismo)
├── produtos.py             # Funções estruturadas para produtos
└── main.py                 # Fluxo principal e integração dos paradigmas
```

## Paradigmas Utilizados

### Paradigma Estruturado

* Uso de `if/elif/else`, loops, funções e `match`.
* Arquivo principal `main.py` controla o fluxo do sistema.

### Paradigma Funcional

* `map`, `filter`, `reduce` aplicados em operações reais.
* Função de ordem superior: `aplicar_desconto()`.
* Funções puras e imutabilidade quando possível.

### Paradigma Orientado a Objetos

* Classes: `Produto`, `ProdutoFisico`, `ProdutoDigital`, `Carrinho`, `Pedido`.
* Herança e polimorfismo com sobrescrita de métodos.
* Encapsulamento usando atributos privados.

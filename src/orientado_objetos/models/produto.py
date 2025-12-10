"""
PARADIGMA ORIENTADO A OBJETOS
- Classe abstrata (ABC)
- Encapsulamento (atributos privados com _)
- Métodos abstratos
- Getters e Setters
"""

from abc import ABC, abstractmethod


class Produto(ABC):
    """
    Classe abstrata para produtos (PARADIGMA OO)
    Implementa encapsulamento e define interface para subclasses
    """
    
    def __init__(self, codigo: int, nome: str, descricao: str, 
                 preco: float, estoque: int, categoria: str):
        # ENCAPSULAMENTO: Atributos privados (convenção Python com _)
        self._codigo = codigo
        self._nome = nome
        self._descricao = descricao
        self._preco = preco
        self._estoque = estoque
        self._categoria = categoria
    
    # GETTERS (Encapsulamento - acesso controlado)
    @property
    def codigo(self) -> int:
        return self._codigo
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def descricao(self) -> str:
        return self._descricao
    
    @property
    def preco(self) -> float:
        return self._preco
    
    @property
    def estoque(self) -> int:
        return self._estoque
    
    @property
    def categoria(self) -> str:
        return self._categoria
    
    # SETTERS (Encapsulamento - modificação controlada)
    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco > 0:
            self._preco = novo_preco
        else:
            raise ValueError("Preço deve ser positivo")
    
    @estoque.setter
    def estoque(self, novo_estoque: int):
        if novo_estoque >= 0:
            self._estoque = novo_estoque
        else:
            raise ValueError("Estoque não pode ser negativo")
    
    # Métodos públicos
    def debitar_estoque(self, quantidade: int) -> bool:
        """Debita do estoque se houver disponibilidade"""
        if self._estoque >= quantidade:
            self._estoque -= quantidade
            return True
        return False
    
    def adicionar_estoque(self, quantidade: int):
        """Adiciona quantidade ao estoque"""
        if quantidade > 0:
            self._estoque += quantidade
    
    # MÉTODO ABSTRATO - Será implementado pelas subclasses (POLIMORFISMO)
    @abstractmethod
    def calcular_valor_final(self, quantidade: int) -> float:
        """
        Calcula o valor final do produto
        Cada tipo de produto pode ter cálculo diferente
        """
        pass
    
    @abstractmethod
    def obter_detalhes_especificos(self) -> str:
        """
        Retorna detalhes específicos de cada tipo de produto
        """
        pass
    
    def __str__(self) -> str:
        return f"{self._nome} - R$ {self._preco:.2f} (Estoque: {self._estoque})"
    
    def __repr__(self) -> str:
        return f"Produto(codigo={self._codigo}, nome='{self._nome}')"
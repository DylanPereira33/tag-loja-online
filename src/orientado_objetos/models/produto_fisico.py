
"""
PARADIGMA ORIENTADO A OBJETOS
- HERANÇA: ProdutoFisico herda de Produto
- POLIMORFISMO: Sobrescreve métodos da classe pai
"""

from .produto import Produto


class ProdutoFisico(Produto):
    """
    HERANÇA: ProdutoFisico extends Produto
    Produtos físicos têm peso e frete
    """
    
    # Constante de classe para cálculo de frete
    VALOR_FRETE_POR_KG = 5.00
    
    def __init__(self, codigo: int, nome: str, descricao: str,
                 preco: float, estoque: int, categoria: str, peso_kg: float):
        # Chama o construtor da superclasse
        super().__init__(codigo, nome, descricao, preco, estoque, categoria)
        
        # Atributo específico de produto físico
        self._peso_kg = peso_kg
    
    @property
    def peso_kg(self) -> float:
        return self._peso_kg
    
    def _calcular_frete(self) -> float:
        """Método privado para calcular frete baseado no peso"""
        return self._peso_kg * self.VALOR_FRETE_POR_KG
    
    # POLIMORFISMO: Sobrescreve método abstrato da superclasse
    def calcular_valor_final(self, quantidade: int) -> float:
        """
        POLIMORFISMO: Implementação específica para produto físico
        Valor = (preço * quantidade) + frete
        """
        valor_produtos = self.preco * quantidade
        frete = self._calcular_frete()
        
        return valor_produtos + frete
    
    # POLIMORFISMO: Sobrescreve método abstrato
    def obter_detalhes_especificos(self) -> str:
        """Retorna detalhes específicos de produto físico"""
        frete = self._calcular_frete()
        return f"Peso: {self._peso_kg}kg | Frete: R$ {frete:.2f}"
    
    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Peso: {self._peso_kg}kg (Frete: R$ {self._calcular_frete():.2f})"
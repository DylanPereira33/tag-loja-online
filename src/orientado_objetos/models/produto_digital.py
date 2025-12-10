"""
PARADIGMA ORIENTADO A OBJETOS
- HERANÇA: ProdutoDigital herda de Produto
- POLIMORFISMO: Implementação diferente dos métodos abstratos
"""

from .produto import Produto


class ProdutoDigital(Produto):
    """
    HERANÇA: ProdutoDigital extends Produto
    Produtos digitais não têm frete
    """
    
    def __init__(self, codigo: int, nome: str, descricao: str,
                 preco: float, estoque: int, categoria: str, tamanho_mb: int):
        # Chama o construtor da superclasse
        super().__init__(codigo, nome, descricao, preco, estoque, categoria)
        
        # Atributo específico de produto digital
        self._tamanho_mb = tamanho_mb
    
    @property
    def tamanho_mb(self) -> int:
        return self._tamanho_mb
    
    def _formatar_tamanho(self) -> str:
        """Método privado para formatar o tamanho"""
        if self._tamanho_mb >= 1024:
            return f"{self._tamanho_mb / 1024:.1f} GB"
        else:
            return f"{self._tamanho_mb} MB"
    
    # POLIMORFISMO: Implementação específica para produto digital
    def calcular_valor_final(self, quantidade: int) -> float:
        """
        POLIMORFISMO: Produtos digitais não têm frete
        Valor = preço * quantidade (sem frete)
        """
        return self.preco * quantidade
    
    # POLIMORFISMO: Implementação específica
    def obter_detalhes_especificos(self) -> str:
        """Retorna detalhes específicos de produto digital"""
        return f"Tamanho: {self._formatar_tamanho()} | Download imediato"
    
    def gerar_link_download(self) -> str:
        """Método específico de produto digital"""
        return f"https://downloads.loja.com/{self.codigo}/{self.nome.replace(' ', '-').lower()}"
    
    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | {self._formatar_tamanho()} (Digital)"
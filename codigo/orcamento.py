from typing import Dict

class GerenciadorOrcamento:
    """
    Entidade do Core responsável por estruturar, validar e processar
    o balanço orçamentário e a capacidade de poupança do usuário.
    """
    def __init__(self, renda_bruta: float) -> None:
        if renda_bruta <= 0:
            raise ValueError("A renda bruta inicial deve ser maior que zero.")
        self._renda_bruta: float = renda_bruta
        self._despesas: Dict[str, float] = {}

    def adicionar_despesa(self, categoria: str, valor: float) -> None:
        categoria_limpa = categoria.strip().lower()
        if not categoria_limpa:
            raise ValueError("A categoria da despesa não pode estar vazia.")
        if valor <= 0:
            raise ValueError("O valor da despesa deve ser maior que zero.")
        self._despesas[categoria_limpa] = valor

    def obter_despesas(self) -> Dict[str, float]:
        return self._despesas.copy()

    def calcular_total_despesas(self) -> float:
        return sum(self._despesas.values())

    def verificar_orcamento_estourado(self) -> bool:
        """Retorna True se as despesas superarem ou igualarem a renda bruta."""
        return self.calcular_total_despesas() >= self._renda_bruta

    def calcular_sobra_liquida(self) -> float:
        """Calcula a margem financeira real disponível."""
        sobra = self._renda_bruta - self.calcular_total_despesas()
        return round(sobra, 2)
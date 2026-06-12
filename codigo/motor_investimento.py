from abc import ABC, abstractmethod
from typing import Dict

class EstrategiaAlocacao(ABC):
    """Classe base abstrata para as estratégias de alocação de investimentos."""
    
    @abstractmethod
    def calcular_alocacao(self, sobra_mensal: float) -> Dict[str, float]:
        pass

class AlocacaoConservadora(EstrategiaAlocacao):
    """Alocação focada em Renda Fixa e proteção de capital."""
    
    def calcular_alocacao(self, sobra_mensal: float) -> Dict[str, float]:
        return {
            "Renda Fixa Curto Prazo": round(sobra_mensal * 0.70, 2),
            "Renda Fixa Longo Prazo": round(sobra_mensal * 0.30, 2),
            "Ativos de Risco": 0.00
        }

class AlocacaoModerada(EstrategiaAlocacao):
    """Alocação balanceada entre Renda Fixa e Risco."""
    
    def calcular_alocacao(self, sobra_mensal: float) -> Dict[str, float]:
        return {
            "Renda Fixa Curto Prazo": round(sobra_mensal * 0.50, 2),
            "Renda Fixa Longo Prazo": round(sobra_mensal * 0.30, 2),
            "Ativos de Risco": round(sobra_mensal * 0.20, 2)
        }

class AlocacaoArrojada(EstrategiaAlocacao):
    """Alocação focada em Ativos de Risco e Renda Fixa de menor prazo."""
    
    def calcular_alocacao(self, sobra_mensal: float) -> Dict[str, float]:
        return {
            "Renda Fixa Curto Prazo": round(sobra_mensal * 0.30, 2),
            "Renda Fixa Longo Prazo": round(sobra_mensal * 0.20, 2),
            "Ativos de Risco": round(sobra_mensal * 0.50, 2)
        }

class ContextoAlocacao:
    """Motor de investimentos que aplica o padrão Strategy."""
    
    def __init__(self, estrategia: EstrategiaAlocacao) -> None:
        self._estrategia = estrategia

    def definir_estrategia(self, estrategia: EstrategiaAlocacao) -> None:
        """Altera a estratégia de alocação dinamicamente."""
        self._estrategia = estrategia

    def executar_alocacao(self, sobra_mensal: float) -> Dict[str, float]:
        """Executa o cálculo de alocação com base na estratégia atual."""
        if sobra_mensal <= 0:
            raise ValueError("A sobra orçamentária deve ser maior que zero para permitir a alocação.")
        return self._estrategia.calcular_alocacao(sobra_mensal)
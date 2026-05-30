from abc import ABC, abstractmethod
from typing import Dict

class EstrategiaAlocacao(ABC):
    @abstractmethod
    def calcular_alocacao(self, sobra: float) -> Dict[str, float]:
        pass

class AlocacaoConservadora(EstrategiaAlocacao):
    def calcular_alocacao(self, sobra: float) -> Dict[str, float]:
        return {
            "Renda Fixa Curto Prazo": round(sobra * 0.70, 2),
            "Renda Fixa Longo Prazo": round(sobra * 0.30, 2),
            "Ativos de Risco": 0.00
        }

class AlocacaoModerada(EstrategiaAlocacao):
    def calcular_alocacao(self, sobra: float) -> Dict[str, float]:
        return {
            "Renda Fixa Curto Prazo": round(sobra * 0.50, 2),
            "Renda Fixa Longo Prazo": round(sobra * 0.30, 2),
            "Ativos de Risco": round(sobra * 0.20, 2)
        }

class AlocacaoArrojada(EstrategiaAlocacao):
    def calcular_alocacao(self, sobra: float) -> Dict[str, float]:
        return {
            "Renda Fixa Curto Prazo": round(sobra * 0.30, 2),
            "Renda Fixa Longo Prazo": round(sobra * 0.20, 2),
            "Ativos de Risco": round(sobra * 0.50, 2)
        }

class ContextoAlocacao:
    def __init__(self, estrategia: EstrategiaAlocacao) -> None:
        self._estrategia = estrategia

    def definir_estrategia(self, estrategia: EstrategiaAlocacao) -> None:
        self._estrategia = estrategia

    def executar_alocacao(self, sobra: float) -> Dict[str, float]:
        return self._estrategia.calcular_alocacao(sobra)
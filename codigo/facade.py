from dataclasses import dataclass
from typing import List, Dict

from perfil_risco import AvaliadorPerfilRisco
from relatorio import GeradorRelatorio
from persistencia import GerenciadorDados
from motor_investimento import (
    ContextoAlocacao,
    AlocacaoConservadora,
    AlocacaoModerada,
    AlocacaoArrojada
)

@dataclass
class ResultadoSimulacao:
    """Caixa organizadora (DTO) que a Facade vai devolver para a tela."""
    sobra_mensal: float
    perfil: str
    alocacao: Dict[str, float]


class InvestPlanFacade:
    """
    Fachada que orquestra as chamadas para as classes de negócio, risco e relatório,
    isolando a complexidade da interface do usuário.
    """
    
    def __init__(self):
        self.avaliador_risco = AvaliadorPerfilRisco()
        self.gerador_relatorio = GeradorRelatorio()
        self.gerenciador_dados = GerenciadorDados()

    def obter_perguntas_risco(self) -> list:
        """Pede as perguntas para o avaliador e as entrega para o menu."""
        return self.avaliador_risco.obter_questionario()

    def processar_simulacao_completa(self, sobra: float, respostas_risco: List[str]) -> ResultadoSimulacao:
        """
        Recebe os dados brutos da interface, processa todo o fluxo e devolve o resultado final.
        """
        perfil_definido = self.avaliador_risco.calcular_perfil(respostas_risco)
        
        if perfil_definido == "conservador":
            estrategia = AlocacaoConservadora()
        elif perfil_definido == "moderado":
            estrategia = AlocacaoModerada()
        else:
            estrategia = AlocacaoArrojada() 

        motor = ContextoAlocacao(estrategia)
        alocacao_final = motor.executar_alocacao(sobra)

        resultado = ResultadoSimulacao(
            sobra_mensal=sobra,
            perfil=perfil_definido,
            alocacao=alocacao_final
        )

        self.gerenciador_dados.salvar_dados({
            "sobra_mensal": sobra,
            "perfil_risco": perfil_definido,
            "alocacao": alocacao_final
        })
        self.gerador_relatorio.gerar_txt(resultado)

        return resultado
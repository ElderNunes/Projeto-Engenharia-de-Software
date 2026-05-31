from motor_investimento import (
    ContextoAlocacao,
    AlocacaoConservadora,
    AlocacaoModerada,
    AlocacaoArrojada
)

class InvestPlanFacade:
    """
    Fachada que isola a interface do terminal das regras de negócio complexas do Core.
    """
    
    def calcular_investimentos(self, sobra: float, perfil: str) -> dict:
        perfil_formatado = perfil.strip().lower()
        
        if perfil_formatado == "conservador":
            estrategia = AlocacaoConservadora()
        elif perfil_formatado == "moderado":
            estrategia = AlocacaoModerada()
        elif perfil_formatado == "arrojado":
            estrategia = AlocacaoArrojada()
        else:
            estrategia = AlocacaoConservadora() 

        contexto = ContextoAlocacao(estrategia)
        return contexto.executar_alocacao(sobra)
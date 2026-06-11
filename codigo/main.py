import cli_utils
from facade import InvestPlanFacade

def iniciar_sistema() -> None:
    """Ponto de entrada do sistema. Apenas instancia a Facade e o loop do menu principal."""
    facade = InvestPlanFacade()
    
    while True:
        cli_utils.exibir_titulo("INVESTPLAN - MENU PRINCIPAL")
        print("1. Iniciar Simulação Completa")
        print("2. Sair do Sistema")
        
        opcao = cli_utils.ler_opcao("\nEscolha uma opção (1-2): ", ["1", "2"])
        
        if opcao == "1":
            cli_utils.exibir_titulo("NOVA SIMULAÇÃO")
            try:
                # O método executar_simulacao_completa será implementado pelo Elder na facade.py
                # facade.executar_simulacao_completa()
                print("Aguardando o Elder implementar o executar_simulacao_completa() na Facade...")
            except Exception as e:
                cli_utils.exibir_alerta(f"Erro inesperado durante a simulação: {e}")
                
        elif opcao == "2":
            cli_utils.exibir_sucesso("Encerrando o InvestPlan. Até logo!")
            break

if __name__ == "__main__":
    iniciar_sistema()
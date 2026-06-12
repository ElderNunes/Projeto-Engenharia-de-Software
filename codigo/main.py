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
                # 1. Pega a sobra (O Guilherme e o Felipe vão melhorar isso depois com o orcamento.py)
                sobra = float(input("Digite a sobra orçamentária calculada (R$): "))
                
                # 2. Pega as perguntas da Facade e exibe para o usuário
                perguntas = facade.obter_perguntas_risco()
                respostas = []
                print("\n--- Questionário de Risco ---")
                for p in perguntas:
                    print(f"\n{p.id}. {p.enunciado}")
                    for letra, texto in p.opcoes.items():
                        print(f"  {letra}) {texto}")
                    resp = input("Sua resposta (a/b/c): ")
                    respostas.append(resp)
                
                # 3. Manda tudo para o Garçom (Facade) processar!
                # ADEUS PRINT ANTIGO DO SEU AMIGO!
                resultado_dto = facade.processar_simulacao_completa(sobra, respostas)
                
                # 4. Exibe a caixa pronta (DTO) que a Facade devolveu
                cli_utils.exibir_titulo("ESTRATÉGIA DE ALOCAÇÃO RECOMENDADA")
                print(f"Perfil detectado: {resultado_dto.perfil.capitalize()}")
                print("-" * 30)
                for ativo, valor in resultado_dto.alocacao.items():
                    print(f"* {ativo}: R$ {valor:.2f}")
                
                print("\n[✔] Simulação salva e relatório .txt gerado com sucesso!")
                print("-" * 50)
                
            except ValueError as e:
                cli_utils.exibir_alerta(f"Erro de validação: {e}")
            except Exception as e:
                cli_utils.exibir_alerta(f"Erro inesperado: {e}")
                
        elif opcao == "2":
            cli_utils.exibir_sucesso("Encerrando o InvestPlan. Até logo!")
            break

if __name__ == "__main__":
    iniciar_sistema()
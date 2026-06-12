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
                renda = float(input("Digite sua renda bruta mensal (R$): "))
                
                despesas = {}
                print("\n--- Cadastro de Despesas ---")
                print("Digite as despesas. Pressione ENTER com a categoria vazia para finalizar.")
                while True:
                    categoria = input("Categoria da despesa (ex: Aluguel, Mercado): ").strip()
                    if not categoria:
                        break 
                    valor_despesa = float(input(f"Valor para '{categoria}' (R$): "))
                    despesas[categoria] = valor_despesa

                perguntas = facade.obter_perguntas_risco()
                respostas = []
                print("\n--- Questionário de Risco ---")
                for p in perguntas:
                    print(f"\n{p.id}. {p.enunciado}")
                    for letra, texto in p.opcoes.items():
                        print(f"  {letra}) {texto}")
                    resp = input("Sua resposta (a/b/c): ").lower().strip()
                    respostas.append(resp)
                
                print("\n--- Projeção de Patrimônio ---")
                anos_projecao = int(input("Para quantos anos deseja projetar seus investimentos? (ex: 10): "))
                
                resultado_dto = facade.processar_simulacao_completa(
                    renda=renda, 
                    despesas=despesas, 
                    respostas_risco=respostas, 
                    anos_projecao=anos_projecao
                )
                
                cli_utils.exibir_titulo("RESULTADO DA SIMULAÇÃO")
                print(f"Renda Bruta: R$ {resultado_dto.renda_bruta:.2f}")
                print(f"Total de Despesas: R$ {resultado_dto.total_despesas:.2f}")
                print(f"Sobra Líquida (Aporte Mensal): R$ {resultado_dto.sobra_mensal:.2f}")
                print("-" * 30)
                
                print(f"Perfil detectado: {resultado_dto.perfil.capitalize()}")
                print("Estratégia de Alocação Recomendada:")
                for ativo, valor in resultado_dto.alocacao.items():
                    print(f"* {ativo}: R$ {valor:.2f}")
                print("-" * 30)
                
                print(f"Projeção do Patrimônio em {resultado_dto.anos_projecao} anos: R$ {resultado_dto.patrimonio_projetado:.2f}")
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
from facade import InvestPlanFacade

def exibir_menu_principal() -> None:
    print("\n" + "=" * 50)
    print(" INVESTPLAN - MENU PRINCIPAL ".center(50))
    print("=" * 50)
    print("1. Simular Alocação de Investimentos")
    print("2. Sair do Sistema")
    print("=" * 50)

def capturar_opcao_menu() -> str:
    return input("Escolha uma opção (1-2): ").strip()

def capturar_dados_alocacao() -> tuple[float, str]:
    try:
        sobra = float(input("Digite a sobra orçamentária (R$): "))
    except ValueError:
        return -1.0, "" 
        
    perfil = input("Digite o perfil de risco (Conservador, Moderado, Arrojado): ")
    return sobra, perfil

def exibir_resultado_alocacao(resultado: dict) -> None:
    print("\n" + "-" * 50)
    print(" ESTRATÉGIA DE ALOCAÇÃO RECOMENDADA ".center(50))
    print("-" * 50)
    for ativo, valor in resultado.items():
        print(f"* {ativo}: R$ {valor:.2f}")
    print("-" * 50)

def iniciar_sistema() -> None:
    facade = InvestPlanFacade()
    
    while True:
        exibir_menu_principal()
        opcao = capturar_opcao_menu()
        
        if opcao == "1":
            sobra, perfil = capturar_dados_alocacao()
            
            if sobra <= 0:
                print("\n[!] Erro: Valor inválido. A sobra deve ser um número maior que zero.")
                continue
                
            try:
                resultado = facade.calcular_investimentos(sobra, perfil)
                exibir_resultado_alocacao(resultado)
            except ValueError as erro_regra_negocio:
                print(f"\n[!] Erro no cálculo: {erro_regra_negocio}")
                
        elif opcao == "2":
            print("\nEncerrando o InvestPlan. Até logo!")
            break
            
        else:
            print("\n[!] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    iniciar_sistema()
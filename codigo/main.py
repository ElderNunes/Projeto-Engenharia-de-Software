from facade import InvestPlanFacade
from persistencia import GerenciadorDados

def ler_float_defensivo(mensagem_prompt: str) -> float:
    while True:
        try:
            entrada_usuario = input(mensagem_prompt).strip().replace(",", ".")
            valor_convertido = float(entrada_usuario)
            if valor_convertido < 0:
                print("Erro: O valor informado não pode ser negativo.")
                continue
            return valor_convertido
        except ValueError:
            print("Erro de Digitação: Insira um número decimal válido (Ex: 1500.50).")

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
    sobra = ler_float_defensivo("Digite a sobra orçamentária (R$): ")
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
    gerenciador = GerenciadorDados()
    
    dados_sessao_anterior = gerenciador.carregar_dados()
    if dados_sessao_anterior:
        print(f"[Singleton] Última sobra recuperada: R$ {dados_sessao_anterior.get('ultima_sobra', 0.0)}\n")

    ultima_sobra = 0.0

    while True:
        exibir_menu_principal()
        opcao = capturar_opcao_menu()
        
        if opcao == "1":
            sobra, perfil = capturar_dados_alocacao()
            
            if sobra <= 0:
                print("\n[!] Erro: Valor inválido. A sobra deve ser um número maior que zero.")
                continue
                
            ultima_sobra = sobra
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

    if ultima_sobra > 0:
        dados_para_salvar = {"ultima_sobra": ultima_sobra}
        gerenciador.salvar_dados(dados_para_salvar)
        print("\n[Singleton] Estado salvo localmente com sucesso.")

if __name__ == "__main__":
    iniciar_sistema()
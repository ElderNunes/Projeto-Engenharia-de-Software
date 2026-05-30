from motor_investimento import (
    ContextoAlocacao,
    AlocacaoConservadora,
    AlocacaoModerada,
    AlocacaoArrojada
)

def executar_demonstracao_terminal() -> None:
    print("=" * 70)
    print(" DEMONSTRAÇÃO - MÓDULO DE ALOCAÇÃO (SPRINT 2) ".center(70))
    print("=" * 70)

    try:
        sobra_usuario = float(input("Digite a sobra orçamentária calculada (R$): "))
    except ValueError:
        print("Entrada inválida. Encerrando demonstração.")
        return

    perfil_usuario = input("Digite o perfil de risco (Conservador, Moderado, Arrojado): ").strip().lower()

    if perfil_usuario == "conservador":
        estrategia = AlocacaoConservadora()
    elif perfil_usuario == "moderado":
        estrategia = AlocacaoModerada()
    elif perfil_usuario == "arrojado":
        estrategia = AlocacaoArrojada()
    else:
        print("Perfil inválido. Assumindo Conservador por trava de segurança.")
        estrategia = AlocacaoConservadora()

    contexto = ContextoAlocacao(estrategia)
    resultado_alocacao = contexto.executar_alocacao(sobra_usuario)

    print("\n" + "=" * 70)
    print(" ESTRATÉGIA DE ALOCAÇÃO RECOMENDADA ".center(70))
    print("=" * 70)

    for ativo, valor in resultado_alocacao.items():
        print(f"- {ativo}: R$ {valor:.2f}")

    print("=" * 70)

if __name__ == "__main__":
    executar_demonstracao_terminal()
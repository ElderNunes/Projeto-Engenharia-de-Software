from motor_investimento import (
    ContextoAlocacao,
    AlocacaoConservadora,
    AlocacaoModerada,
    AlocacaoArrojada
)
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

def executar_demonstracao_terminal() -> None:
    print("=" * 70)
    print(" DEMONSTRAÇÃO - MÓDULO DE ALOCAÇÃO (SPRINT 2) ".center(70))
    print("=" * 70)

    gerenciador = GerenciadorDados()
    dados_sessao_anterior = gerenciador.carregar_dados()
    if dados_sessao_anterior:
        print(f"[Singleton] Última sobra recuperada: R$ {dados_sessao_anterior.get('ultima_sobra', 0.0)}\n")

    sobra_usuario = ler_float_defensivo("Digite a sobra orçamentária calculada (R$): ")

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

    dados_para_salvar = {"ultima_sobra": sobra_usuario}
    gerenciador.salvar_dados(dados_para_salvar)
    print("\n[Singleton] Estado salvo localmente com sucesso.")

if __name__ == "__main__":
    executar_demonstracao_terminal()
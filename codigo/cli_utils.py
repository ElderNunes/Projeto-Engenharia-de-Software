def ler_float_obrigatorio(mensagem_prompt: str) -> float:
    """Lê um número decimal do terminal, garantindo que seja um float válido e não negativo."""
    while True:
        try:
            entrada_usuario = input(mensagem_prompt).strip().replace(",", ".")
            valor_convertido = float(entrada_usuario)
            if valor_convertido < 0:
                print("[!] Erro: O valor informado não pode ser negativo.")
                continue
            return valor_convertido
        except ValueError:
            print("[!] Erro de Digitação: Insira um número decimal válido (Ex: 1500.50).")

def ler_opcao(mensagem_prompt: str, opcoes_validas: list[str]) -> str:
    """Lê uma opção do usuário garantindo que ela esteja dentro da lista de opções válidas."""
    while True:
        opcao = input(mensagem_prompt).strip()
        if opcao in opcoes_validas:
            return opcao
        print(f"[!] Opção inválida. Escolha entre: {', '.join(opcoes_validas)}")

def confirmar_sim_nao(mensagem_prompt: str) -> bool:
    """Lê uma resposta de Sim ou Não do usuário, retornando True para Sim e False para Não."""
    while True:
        resp = input(f"{mensagem_prompt} (S/N): ").strip().upper()
        if resp == 'S':
            return True
        if resp == 'N':
            return False
        print("[!] Responda apenas com 'S' para Sim ou 'N' para Não.")

def exibir_titulo(titulo: str) -> None:
    """Exibe um título formatado e centralizado."""
    print("\n" + "=" * 50)
    print(titulo.center(50))
    print("=" * 50)

def exibir_alerta(mensagem: str) -> None:
    """Exibe uma mensagem de alerta formatada."""
    print(f"\n[ALERTA] {mensagem}")

def exibir_sucesso(mensagem: str) -> None:
    """Exibe uma mensagem de sucesso formatada."""
    print(f"\n[SUCESSO] {mensagem}")

import os
from datetime import datetime

# Nota: Assumimos que a equipe vai criar o DTO 'ResultadoSimulacao' no arquivo 'modelos.py'
# from modelos import ResultadoSimulacao

class GeradorRelatorio:
    """
    Responsável por formatar os dados finais em texto e salvar no disco
    utilizando a técnica de escrita atômica para evitar corrupção de arquivos.
    """
    
    def __init__(self, caminho_arquivo: str = "plano_investplan.txt"):
        self.caminho_arquivo = caminho_arquivo

    def gerar_txt(self, resultado_simulacao) -> bool:
        """
        Recebe o DTO com o resultado da simulação, formata e salva de forma atômica.
        (Neste exemplo, resultado_simulacao é um objeto com os dados finais).
        """
        # 1. Monta o texto do relatório
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        linhas = [
            "=" * 50,
            "         RELATÓRIO DE INVESTIMENTO - INVESTPLAN",
            "=" * 50,
            f"Data da Simulação: {data_atual}",
            f"Perfil de Risco: {resultado_simulacao.perfil.upper()}",
            f"Sobra Orçamentária: R$ {resultado_simulacao.sobra_mensal:.2f}",
            "-" * 50,
            "SUA ALOCAÇÃO RECOMENDADA:",
        ]

        # Adiciona a lista de investimentos
        for ativo, valor in resultado_simulacao.alocacao.items():
            linhas.append(f"  * {ativo}: R$ {valor:.2f}")
            
        linhas.append("-" * 50)
        linhas.append("Lembre-se: Invista com responsabilidade e consistência.")
        linhas.append("=" * 50)

        conteudo_texto = "\n".join(linhas)

        # 2. Inicia o Salvamento Atômico
        caminho_temporario = f"{self.caminho_arquivo}.tmp"
        
        try:
            # Escreve tudo no arquivo temporário
            with open(caminho_temporario, "w", encoding="utf-8") as arquivo_tmp:
                arquivo_tmp.write(conteudo_texto)
                
                # Força o sistema operacional a gravar fisicamente no disco agora
                arquivo_tmp.flush()
                os.fsync(arquivo_tmp.fileno())

            # Substitui o arquivo oficial pelo temporário em 1 único movimento
            os.replace(caminho_temporario, self.caminho_arquivo)
            return True
            
        except Exception as erro:
            # Se der pau no meio, apaga o lixo temporário para não sujar o PC
            if os.path.exists(caminho_temporario):
                os.remove(caminho_temporario)
            
            # Repassa o erro para a Facade lidar
            raise RuntimeError(f"Erro crítico ao exportar relatório atômico: {erro}")
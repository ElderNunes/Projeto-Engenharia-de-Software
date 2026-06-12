import json
import os
from typing import Dict, Any, Optional

class GerenciadorDados:
    _instancia: Optional['GerenciadorDados'] = None

    def __new__(cls, *args: Any, **kwargs: Any) -> 'GerenciadorDados':
        if not cls._instancia:
            cls._instancia = super(GerenciadorDados, cls).__new__(cls, *args, **kwargs)
        return cls._instancia

    def __init__(self) -> None:
        if not hasattr(self, '_caminho_arquivo'):
            self._caminho_arquivo: str = "dados_usuario.json"

    def carregar_dados(self) -> Dict[str, Any]:
        if not os.path.exists(self._caminho_arquivo):
            return {}
        try:
            with open(self._caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except (json.JSONDecodeError, IOError):
            return {}

    def salvar_dados(self, dados: Dict[str, Any]) -> bool:
        try:
            with open(self._caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            return True
        except IOError:
            return False
    def salvar_sessao_completa(self, renda: float, despesas: Dict[str, float], perfil: str, alocacao: Dict[str, float]) -> bool:
        """Estrutura os dados brutos e os persiste de forma integrada."""
        payload = {
            "renda_bruta": renda,
            "despesas": despesas,
            "perfil_risco": perfil,
            "ultima_alocacao": alocacao
        }
        return self.salvar_dados(payload)
import unittest
import sys
import os

# Adiciona a pasta raiz do projeto ao path para poder importar o pacote 'codigo'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from codigo.motor_investimento import ContextoAlocacao, AlocacaoArrojada, AlocacaoConservadora

class TestMotorInvestimento(unittest.TestCase):
    
    def setUp(self):
        """Prepara o contexto antes de cada teste rodar."""
        self.motor_arrojado = ContextoAlocacao(AlocacaoArrojada())
        self.motor_conservador = ContextoAlocacao(AlocacaoConservadora())

    def test_alocacao_arrojada_sucesso(self):
        """Cenário de SUCESSO: Verifica se a matemática da alocação está exata."""
        resultado = self.motor_arrojado.executar_alocacao(1000.0)
        
        # Num perfil arrojado, 50% vai para risco
        self.assertEqual(resultado["Ativos de Risco"], 500.0)
        self.assertEqual(resultado["Renda Fixa Curto Prazo"], 300.0)
        self.assertEqual(resultado["Renda Fixa Longo Prazo"], 200.0)

    def test_alocacao_falha_tipo_invalido(self):
        """Cenário de FALHA: Verifica erro ao passar uma string ao invés de número."""
        with self.assertRaises(TypeError):
            # O Python deve quebrar ao tentar fazer matemática com string
            self.motor_arrojado.executar_alocacao("mil reais")

    def test_alocacao_borda_sobra_zero(self):
        """Cenário de BORDA: Verifica se a exceção correta (ValueError) é lançada se a sobra for zero."""
        with self.assertRaises(ValueError) as contexto:
            self.motor_arrojado.executar_alocacao(0.0)
            
        self.assertTrue("sobra orçamentária deve ser maior que zero" in str(contexto.exception))

if __name__ == '__main__':
    unittest.main()

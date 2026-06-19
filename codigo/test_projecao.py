import unittest
from projecao import SimuladorProjecao

class TestSimuladorProjecao(unittest.TestCase):

    def setUp(self):
        self.simulador = SimuladorProjecao()

    def test_calcular_patrimonio_futuro_sucesso(self):
        """Cenário de Sucesso: Alocação válida calculada ao longo de um período padrão."""
    
        alocacao = {
            "Renda Fixa Curto Prazo": 1000.0,
            "Renda Fixa Longo Prazo": 0.0,
            "Ativos de Risco": 0.0
        }
        
        patrimonio_calculado = self.simulador.calcular_patrimonio_futuro(alocacao, anos=1)
        
        self.assertGreater(patrimonio_calculado, 12000.0)
        self.assertAlmostEqual(patrimonio_calculado, 12639.27, places=1)

    def test_projecao_com_anos_invalidos(self):
        """Cenário de Falha: Período menor ou igual a zero deve lançar ValueError."""
        alocacao = {"Renda Fixa Curto Prazo": 500.0}
        
        with self.assertRaises(ValueError):
            self.simulador.calcular_patrimonio_futuro(alocacao, anos=0)
        with self.assertRaises(ValueError):
            self.simulador.calcular_patrimonio_futuro(alocacao, anos=-5)

    def test_alocacao_com_valores_zerados_ou_negativos(self):
        """Cenário de Borda: Ignora chaves com aportes <= 0 sem quebrar a execução."""
        alocacao_borda = {
            "Renda Fixa Curto Prazo": 0.0,
            "Renda Fixa Longo Prazo": -150.0,  
            "Ativos de Risco": 100.0
        }
        
        patrimonio = self.simulador.calcular_patrimonio_futuro(alocacao_borda, anos=1)
        self.assertGreater(patrimonio, 0.0)

    def test_prazo_longo_borda(self):
        """Cenário de Borda: Teste de estresse matemático com prazos longos (Ex: 50 anos)."""
        alocacao = {"Renda Fixa Curto Prazo": 100.0}
        patrimonio_longo = self.simulador.calcular_patrimonio_futuro(alocacao, anos=50)
        
        self.assertGreater(patrimonio_longo, 100 * 12 * 50) 

if __name__ == "__main__":
    unittest.main()
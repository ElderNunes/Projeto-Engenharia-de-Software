# Estratégia de Testes Automatizados - InvestPlan

Este documento atende aos requisitos da Sprint 4 da disciplina de Engenharia de Software. Aqui registramos nossa abordagem para garantir a qualidade matemática e a robustez do núcleo do sistema, bem como a cobertura e as lacunas deixadas.

---

## 1. Estratégia e Ferramental Escolhido

A equipe optou por utilizar a biblioteca nativa `unittest` do Python. Nossa estratégia consistiu em focar os testes de Caixa Branca estritamente no *Core* da aplicação (camada de negócios matemática), isolando as lógicas de Interface (CLI) e Entrada/Saída de dados. Essa separação só foi possível graças à refatoração prévia que removeu chamadas de I/O de dentro dos motores de cálculo. 

No módulo `motor_investimento.py`, garantimos a integridade do padrão *Strategy* cobrindo os seguintes casos:
- **Sucesso:** Verificação do cálculo percentual exato da estratégia (ex: perfil Arrojado alocando corretamente 50% em ativos de risco).
- **Falha:** Validação de segurança de tipagem (injeção de strings para forçar e capturar um `TypeError`).
- **Borda:** Injeção de sobras financeiras iguais a zero, atestando o lançamento da exceção `ValueError` estipulada pela regra de negócio.

---

## 2. Cobertura e Prevenção de Falhas Críticas

*Descreva aqui os módulos que foram cobertos por testes automatizados (motor_investimento, orcamento, etc) e exemplifique os cenários de Sucesso, Falha e Borda que foram protegidos.*

---

## 3. Lacunas Não Cobertas e Tratamento de Exceções

*Documente aqui, conforme exigência da disciplina, as áreas do sistema que não receberam cobertura de testes automatizados (ex: camada CLI, leitura de arquivos) e justifique essa decisão.*

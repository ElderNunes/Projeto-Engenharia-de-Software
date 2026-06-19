# InvestPlan - Planejador Financeiro para Iniciantes

## Visão Geral

O InvestPlan é um sistema Python desenvolvido para auxiliar adultos sem conhecimento financeiro prévio a assumir o controle de suas finanças e criar um plano viável para poupar e alocar recursos. O sistema atua em duas frentes: primeiro, analisa e otimiza o orçamento mensal (controle de gastos) e, em seguida, recomenda uma estratégia de alocação de investimentos com projeções realistas de crescimento baseadas na capacidade real de poupança do usuário.

---

## Problema que Resolve

### Situação-Problema
Adultos em fase de estruturação financeira (especialmente jovens iniciando suas carreiras) frequentemente desejam organizar suas finanças e investir, mas enfrentam barreiras significativas:
- Descontrole orçamentário e dificuldade para calcular o valor real que conseguem poupar mensalmente.
- Falta de conhecimento prático para diferenciar tipos de investimento (renda fixa, ações, fundos).
- Receio de tomar decisões financeiras inadequadas sem uma orientação objetiva.
- Paralisação por análise devido ao excesso de informações desestruturadas na internet.

### Fontes Reais e Justificativa
A relevância do problema para o público-alvo e a necessidade de uma ferramenta de planejamento são sustentadas por dados concretos do mercado brasileiro:

1. **Reportagem/Artigo (Raio X do Investidor Brasileiro - ANBIMA):** O relatório aponta que os canais digitais (como YouTube e Instagram) são as principais fontes de informação de quem investe, com forte adesão das novas gerações. Contudo, **um terço da população (31%) não possui dinheiro guardado para imprevistos (reserva financeira)**. Isso valida a necessidade do sistema InvestPlan focar na construção e cálculo de reservas de emergência (renda fixa) antes de sugerir ativos de risco.
   - *Fonte (Página):* [Raio X do Investidor Brasileiro](https://www.anbima.com.br/pt_br/especial/raio-x-do-investidor-brasileiro.htm)
   - *Fonte (PDF):* [Raio X do Investidor - 9ª Edição](https://www.anbima.com.br/data/files/BE/05/B0/55/1EABD91008E6DAD9F82BA2A8/Raio-X-do-Investidor-9-edicao.pdf)

2. **Fórum Técnico (Comunidade de Finanças):** Em discussões diárias nas comunidades abertas, os iniciantes relatam a chamada "paralisia por análise". Há um excesso de recomendações desconexas vindas de influenciadores (que representam a fonte de aprendizado para 73% dos novos investidores, segundo a B3). Os usuários do fórum buscam ativamente o que o InvestPlan propõe: regras matemáticas e calculadoras que digam de forma fria e estruturada o que fazer com seus primeiros aportes.
   - *Fonte:* [Comunidade r/investimentos no Reddit](https://www.reddit.com/r/investimentos/)

3. **Relatório Institucional (CVM - Comissão de Valores Mobiliários):** A pesquisa "Perfil e Comportamento dos Investidores 2024", realizada com mais de 1.300 respondentes, aponta que o interesse por educação financeira cresceu 42% entre os investidores brasileiros no último ano, e que a formação de reserva de emergência e aposentadoria é o principal objetivo financeiro dos perfis conservador e moderado — exatamente o público-alvo do InvestPlan.
   - *Fonte:* [CVM - Perfil e Comportamento dos Investidores 2024](https://www.gov.br/cvm/pt-br/assuntos/noticias/2025/pesquisa-sobre-perfil-do-investidor-brasileiro-aponta-formacao-de-reservas-para-aposentadoria-como-principal-objetivo-de-investimento)

### Como o InvestPlan Resolve
O sistema realiza as seguintes etapas:
1. **Otimização Orçamentária:** Coleta e categoriza os gastos mensais do usuário contra a sua renda, gerando um diagnóstico de saúde financeira e calculando a capacidade real de poupança (Módulo de Controle de Gastos).
2. **Coleta de Perfil:** Avalia o perfil de risco e os objetivos de curto, médio e longo prazo do usuário.
3. **Análise de Alocação:** Processa a situação financeira de forma objetiva através do terminal.
4. **Recomendações Personalizadas:** Gera uma estratégia de alocação de recursos por tipo de ativo (Tesouro Direto, CDBs, ETFs) usando padrões de projeto (ex: *Strategy*).
5. **Relatório Final:** Produz um documento claro que explica cada recomendação e projeta o crescimento do patrimônio, mitigando a percepção de risco.

### Viabilidade do Escopo (Tempo Disponível)
O conjunto de funcionalidades proposto foi intencionalmente delimitado para caber no ciclo de 4 Sprints da disciplina, priorizando a qualidade da engenharia sobre a quantidade de recursos. A viabilidade de entrega no tempo disponível é garantida pelas seguintes decisões arquiteturais:
1. **Interface de Linha de Comando (CLI):** O sistema rodará 100% no terminal, eliminando o tempo de desenvolvimento de *front-end* ou interfaces gráficas (GUI) e mantendo o foco na lógica de negócio e nos Padrões de Projeto (ex: *Strategy*).
2. **Armazenamento Local Estruturado:** Para evitar o *overhead* de configuração e *deploy* de bancos de dados em nuvem, a persistência e entrada de dados ocorrerá via manipulação de arquivos estruturados locais (ex: `.json` ou `.csv`).
3. **Foco no Fluxo Principal (*Core Flow*):** O escopo restringe-se a um único fluxo de alto valor (Receber Dados -> Otimizar Orçamento -> Recomendar Alocação -> Gerar Relatório). Funcionalidades acessórias, como integração com APIs de cotações em tempo real ou sistemas de autenticação, foram deliberadamente deixadas fora do escopo inicial para garantir a entrega de um protótipo funcional, coberto por testes automatizados, até 19/06.

---

## Público-Alvo

**Perfil Primário:** Adultos em início de jornada de organização financeira (com forte aderência entre jovens profissionais, mas sem limite restrito de idade).

**Características:**
- Renda mensal estabelecida (CLT, prestação de serviços, bolsas de pesquisa ou transição de carreira).
- Pouca ou nenhuma experiência prática com controle rigoroso de caixa e mercado financeiro.
- Desejo de sair da inércia, criar uma reserva de emergência e começar a investir de forma segura.
- Acesso a um dispositivo básico (computador ou smartphone) para gerenciar suas finanças.

**Exemplos de usuários:**
- Recém-formado buscando organizar o primeiro salário.
- Profissional de 35 anos que percebeu a necessidade de criar uma reserva de emergência e não sabe por onde começar.
- Pessoa que recebeu um acerto trabalhista ou bônus e quer planejar o uso desse dinheiro de forma inteligente, sem gastar tudo por impulso.


---


## Membros da Equipe e Dinâmica de Trabalho

- Elder Nunes Gonçalves
- Felipe dos Santos Rodrigues
- Guilherme Giuliangeli Monteiro

Para garantir a participação integral e o desenvolvimento de todas as competências de engenharia por todos os membros, a equipe adotou uma dinâmica de **Liderança Rotativa e Fatiamento Vertical**. Todos os integrantes participarão ativamente da codificação, documentação e desenho arquitetural em todas as fases do projeto.

**Sprint 1: Engenharia de Requisitos (22/05 a 26/05)**
- Felipe: Responsável por liderar a redação e estruturação das Histórias de Usuário e Critérios de Aceite.
- Elder: Responsável por liderar a Elicitação (pesquisa de mercado e regras de negócio de investimentos/orçamento).
- Guilherme: Responsável por conduzir a Validação dos requisitos (identificação de ambiguidades e conflitos).
*(Ajuste de escopo: revisão cruzada para garantir validação de todos os artefatos gerados em conjunto)*

**Sprint 2: Projeto e Arquitetura (29/05 a 02/06)**
Nesta sprint, o trabalho foi dividido em fatias verticais para atender ao requisito de participação integral em todos os tópicos exigidos:
- **Felipe:**
  - *Padrões de Qualidade:* Documentação das regras de *Clean Code*, estabelecendo a padronização de um código estritamente funcional (ausência de comentários e cabeçalhos descritivos nos arquivos Python, garantindo legibilidade exclusiva por nomes de variáveis e funções).
  - *Arquitetura:* Desenho e justificativa de *trade-offs* da Camada de Lógica de Negócios (Core).
  - *Padrões de Projeto:* Desenho UML e documentação do padrão **Strategy** (Módulo de Alocação).
  - *Codificação Inicial:* Implementação do esqueleto estrutural do motor de investimentos na CLI.
- **Elder:**
  - *Padrões de Qualidade:* Documentação das regras de controle de versão (Git Flow simplificado e *commits* semânticos).
  - *Arquitetura:* Desenho e justificativa de *trade-offs* da Camada de Interface (CLI).
  - *Padrões de Projeto:* Desenho UML e documentação do padrão **Facade** (orquestração de menus e comunicação com a lógica).
  - *Codificação Inicial:* Implementação do *loop* principal da interface do terminal e funções de captação de *inputs*.
- **Guilherme:**
  - *Padrões de Qualidade:* Documentação das diretrizes de tipagem (*Type Hinting*) e tratamento de erros.
  - *Arquitetura:* Desenho e justificativa de *trade-offs* da Camada de Persistência Local (arquivos estruturados).
  - *Padrões de Projeto:* Desenho UML e documentação do padrão **Singleton** (gerenciamento de estado e controle de acesso a arquivos locais).
  - *Codificação Inicial:* Implementação dos esqueletos de persistência de dados e validação primária de entradas no terminal.

**Sprint 3: Desenvolvimento Base (09/06 a 12/06)**

**1. Resumo do Briefing**
O objetivo na Sprint 3 será entregar um fluxo funcional, limpo e defensável: **Orçamento → Perfil → Alocação → Projeção → Relatório `.txt`**. A decisão central é não aumentar o escopo por volume, mas extrair máxima qualidade arquitetural, isolando I/O do terminal, implementando persistência atômica, e utilizando *dataclasses* (DTOs) para trânsito de informações entre as camadas.

**User Review Required**
> [!IMPORTANT]
> - A estrutura de revisão cruzada exigirá que cada membro da equipe teste o módulo do outro.
> - As constantes de taxas de rentabilidade serão isoladas em `config.py` e requerem aprovação final dos valores numéricos.

**2. Decisões Técnicas Tomadas**
- **DTOs (Data Transfer Objects):** A `InvestPlanFacade` retornará um objeto `ResultadoSimulacao` consolidado. O `main.py` será estritamente um *entrypoint*.
- **I/O Isolado:** Toda a interação e validação textual de dados migrará para o módulo `cli_utils.py`.
- **Projeção Desacoplada:** Os juros compostos habitarão o `projecao.py`, não interferindo na coesão do *Strategy* de alocação original.
- **Alta Robustez (Atomicidade):** Salvamento atômico (escrita em `.tmp` seguida por `os.replace`) implantado em `persistencia.py` e `relatorio.py`.
- **Fail-fast (Regra de Negócio):** Respostas no questionário que acusam resgate imediato ou aversão forçam o perfil *Conservador*, interrompendo o cálculo de score.
- **Prevenção de Quebras:** Bloqueio amigável de tela (déficit) se gastos passarem da renda.

**3. Riscos Restantes e Mitigação**
> [!WARNING]
> - **Risco de Integração:** O alto desacoplamento gerará muitos arquivos novos simultaneamente. **Mitigação:** O desenvolvimento deve ser puxado da e para a `develop` constantemente, evitando *Big Bang merges*.
> - **Risco de Apresentação:** Um membro "travar" ao explicar o código de outro. **Mitigação:** Seguir rigorosamente o cronograma de *Revisão Cruzada Obrigatória*, com ensaios de defesa interna.

**Proposed Changes**

Arquitetura física final preentedida para o Sprint 3. Manter isolamento para facilitar refatorações da Sprint 4 (testes `unittest`).

### [MODIFY] [main.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/main.py)
Remoção de lógicas de I/O e validações de float. Fica responsável apenas pela instanciação da Facade e pelo loop infinito do menu principal.
### [MODIFY] [facade.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/facade.py)
Deixa de ser uma rota de passagem e passa a orquestrar de fato as chamadas para as classes de orçamento, avaliação de risco, motor e relatório, gerando o DTO final de saída.
### [MODIFY] [persistencia.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/persistencia.py)
Adoção das funções `os.fsync` e `os.replace` para proteger o salvamento do `dados_usuario.json` contra falhas de sistema.
### [MODIFY] [motor_investimento.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/motor_investimento.py)
Nenhuma grande reescrita algorítmica, apenas readequações em assinaturas para suportar as entradas da nova Facade.
### [NEW] [cli_utils.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/cli_utils.py)
Funções dedicadas para desenhar telas e bloquear formatações incorretas sem lançar *tracebacks* (ex: `ler_float_obrigatorio`, `exibir_sucesso`, etc).
### [NEW] [modelos.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/modelos.py)
Declaração das `@dataclass` que trafegam entre as camadas, como `ResultadoSimulacao` e `ResultadoOrcamento`.
### [NEW] [excecoes.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/excecoes.py)
Definições semânticas de exceções da aplicação, como `OrcamentoEstouradoError` e `ErroExportacaoRelatorio`.
### [NEW] [config.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/config.py)
Constantes `TAXAS_ANUAIS_POR_PERFIL` (0.08, 0.10, 0.12) e `CATEGORIAS_OBRIGATORIAS`.
### [NEW] [orcamento.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/orcamento.py)
Lógica matemática para absorver renda bruta, descontar CLT/PJ (RN-04) e processar as oito categorias, detectando déficit.
### [NEW] [perfil_risco.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/perfil_risco.py)
Lógica computacional das 3 perguntas fundamentais (RN-06), processando pontuações.
### [NEW] [projecao.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/projecao.py)
Funções matemáticas puras para computar os juros compostos em cenários de 1, 5 e 10 anos.
### [NEW] [relatorio.py](file:///C:/Users/felip/Downloads/Projeto-Engenharia-de-Software-1/codigo/relatorio.py)
Formatador string que consome o `ResultadoSimulacao` e grava de forma atômica o plano em `plano_investplan.txt`.

---

## Verification Plan

### Divisão de Tarefas Dinâmica (Defesa Cruzada)
| Módulos Atribuídos | Desenvolvedor Principal | Revisor Obrigatório | Responsável por Apresentar |
|:---|:---|:---|:---|
| `orcamento.py`, `persistencia.py`, `projecao.py` | **Guilherme** | Felipe | Elder |
| `perfil_risco.py`, `relatorio.py`, `facade.py` | **Elder** | Guilherme | Felipe |
| `motor_investimento.py`, `cli_utils.py`, `main.py` | **Felipe** | Elder | Guilherme |

*Regra de Ouro da Equipe: Nenhum *merge* vai para a branch principal sem que o desenvolvedor dono explique a lógica para o seu Revisor.*

### Plano de Demonstração (Review de 12/06)
1. **O Cenário Perfeito (Happy Path):** Demonstrar a viabilidade inserindo uma Renda CLT razoável, 8 despesas balanceadas e obtendo um relatório perfeitamente formatado.
2. **Robustez - Tratamento I/O (HU-05):** Inserir textos em locais que pedem dinheiro. Demonstrar a proteção do `cli_utils.py`.
3. **Robustez - Regra de Negócio (RN-05):** Inserir despesas estouradas. Demonstrar o diagnóstico negativo bloqueando o usuário educadamente, sem derrubar a aplicação.

**Sprint 4: Testes Automatizados e Refatoração (16/06 a 19/06)**

- **Divisão de Testes (unittest):** 
  - **Felipe:** Escrita de testes unitários para a classe `motor_investimento.py` (Sucesso, Falha, Borda).
  - **Guilherme:** Escrita de testes unitários para a classe `orcamento.py` e `projecao.py` (Sucesso, Falha, Borda).
  - **Elder:** Escrita de testes unitários para a classe `perfil_risco.py` (Sucesso, Falha, Borda).
- **Documentação de Qualidade:** Todos os membros preencherão o arquivo `docs/testes.md` documentando a estratégia utilizada e as lacunas (testes de UI/CLI) que ficaram de fora.

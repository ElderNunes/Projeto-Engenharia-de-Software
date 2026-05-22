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

Para garantir a participação integral e o desenvolvimento de todas as competências de engenharia por todos os membros, a equipe adotou uma dinâmica de **Liderança Rotativa por Sprint**. Todos os integrantes participarão ativamente da codificação, documentação e testes em todas as fases do projeto, com a seguinte divisão de responsabilidade pelas entregas críticas:

**Sprint 1: Engenharia de Requisitos (22/05 a 26/05)**
- Felipe: Responsável por liderar a redação e estruturação das Histórias de Usuário e Critérios de Aceite.
- Elder: Responsável por liderar a Elicitação (pesquisa de mercado e regras de negócio de investimentos/orçamento).
- Guilherme: Responsável por conduzir a Validação dos requisitos (identificação de ambiguidades e conflitos).

**Sprint 2: Projeto e Arquitetura (29/05 a 02/06)**
- Felipe: Responsável pelo Diagrama de Arquitetura e justificativa de *trade-offs*.
- Elder: Responsável por liderar a implementação do esqueleto funcional no Terminal (CLI).
- Guilherme: Responsável pela documentação dos Padrões de Projeto e Padrões de Qualidade.

**Sprint 3: Desenvolvimento Base (09/06 a 12/06)**
- Todos os membros: Implementação balanceada das funcionalidades em Python. Cada membro assumirá o ciclo completo (lógica, testes e integração) de pelo menos um módulo do sistema (ex: Módulo de Gastos, Módulo de Alocação, Módulo de Relatório). Qualquer membro estará apto a explicar qualquer parte do código-fonte durante as revisões.

**Sprint 4: Testes e Refatoração (16/06 a 19/06)**
- Felipe: Responsável pela estratégia e configuração inicial dos Testes Automatizados utilizando o módulo `unittest`.
- Elder: Responsável por liderar as rodadas de Refatoração do código para melhoria de design.
- Guilherme: Responsável pela revisão da documentação final e fechamento do repositório.

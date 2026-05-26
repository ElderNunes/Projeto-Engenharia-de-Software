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

# Seção 1 - Elicitação de Requisitos
## InvestPlan - Planejador Financeiro para Iniciantes

---

## 1.1 Análise de Similares

| # | Nome/Sistema | O que Faz | Público-Alvo | Pontos Fortes | Pontos Fracos/Lacunas | Diferencial do InvestPlan |
|---|---|---|---|---|---|---|
| 1 | **Nubank App** (Módulo de Gastos) | Rastreia gastos por categoria, gera relatórios mensais, oferece insights de despesas | Usuários brasileiros com conta bancária | Interface móvel intuitiva, integração com transações reais, instantâneo | Não oferece recomendação de investimento; foco apenas em gasto, não em poupança | Recomenda alocação de investimentos baseado na poupança calculada |
| 2 | **GuiaBolso** | Agregador de contas bancárias + análise de orçamento + dicas de economia | Classe média brasileira interessada em educação financeira | Conexão com múltiplos bancos, análise comparativa de gastos, metas customizáveis | Interface complexa; muitas features secundárias; recomendações genéricas de investimento sem personalização | Sistema estruturado E2E focado em cálculo preciso de poupança + alocação personalizada por perfil de risco |
| 3 | **Calculadoras Online Genéricas** (sites tipo Quanto Invisto, Simulador XP Investimentos) | Simulam crescimento de investimento com taxa fixa inserida manualmente | Investidores já iniciados buscando projetar rentabilidade | Instantâneas, sem necessidade de cadastro | Não ajudam a calcular capacidade de poupança; assumem que o usuário já sabe quanto consegue poupar mensalmente | Integra orçamento → poupança → simulação em uma única ferramenta |
| 4 | **Aplicativos de Foco em Renda Fixa** (Tesouro Direto, CDB) | Interface do provedor para compra de títulos, consultoria simplificada | Investidores iniciados que já decidiram o produto | Acesso direto, taxas competitivas, explicações sobre cada título | Não ajudam a estruturar orçamento, não comparam produtos, não indicam para qual ativo alocar | Recomenda tipo de ativo (Tesouro vs CDB vs ETF) baseado em perfil e tempo |
| 5 | **Planilhas Excel/Google Sheets Customizadas** | Controle manual de gastos com fórmulas de cálculo de poupança e projeção | DIY investors, contadores, planejadores financeiros | Totalmente customizáveis, sem dependência de terceiros | Requer conhecimento técnico de planilhas; difícil de manter; recomendações manuais/subjetivas | Automatiza as regras de negócio em Python; não requer expertise em Excel; saída estruturada e consistente |
| 6 | **Aplicativos de Micro-Investimento** (Nubank Investimentos, BTG Pactual Digital) | Permitem aportes automáticos pequenos, simulam rentabilidade | Usuários que já resolveram o problema de poupança; investidores iniciados com renda já organizada | Gamificação, automação de aportes, interface amigável | Não ajudam a diagnosticar orçamento; pressupõem que o usuário já sabe quanto poupar | Diagnóstico completo antes de sugerir automação |

---

## 1.2 Regras de Negócio (RN)

### **Categoria: Coleta e Validação de Dados**

**RN-01 (Validação de Renda):**
- A renda mensal bruta informada pelo usuário deve ser um valor numérico positivo >= R$ 1.000,00.
- Se o usuário informar renda abaixo de R$ 1.000, o sistema exibe mensagem de aviso: "Sua renda é muito baixa. O sistema foi pensado para usuários com renda >= R$ 1.000/mês. Deseja continuar?"
- Valor máximo aceito: R$ 1.000.000,00/mês (para evitar erros de entrada).

**RN-02 (Categorização de Gastos):**
- Os gastos devem ser categorizados em exatamente 8 categorias obrigatórias:
  1. Moradia (aluguel, condomínio, IPTU)
  2. Alimentação (supermercado, restaurante)
  3. Transporte (combustível, ônibus, uber)
  4. Saúde (médico, farmácia, plano saúde)
  5. Educação (escola, cursos, livros)
  6. Lazer e Cultura (cinema, streaming, viagens)
  7. Contas Fixas (água, energia, internet, telefone)
  8. Outros (compras não classificadas)
- O usuário pode informar o gasto de cada categoria individualmente ou como "Não tenho este gasto" (valor = 0).

**RN-03 (Validação de Gastos por Categoria):**
- Cada gasto por categoria deve ser um valor numérico positivo >= R$ 0,00.
- Gasto máximo por categoria: R$ 999.999,99.
- A soma total de gastos não pode ultrapassar a renda mensal bruta. Se ultrapassar, o sistema avisa: "Seus gastos somam R$ X, que é maior que sua renda de R$ Y. Revise seus dados."

**RN-04 (Cálculo de Carga Tributária Estimada):**
- Para CLT: desconto automático de 11,5% sobre a renda bruta (INSS + IR médio estimado).
- Para PJ/Autônomo: desconto automático de 20% sobre a renda bruta (estimativa de impostos + contribuições).
- Usuário escolhe seu regime (CLT / PJ) no início.
- A renda líquida = renda bruta - carga tributária estimada.

---

### **Categoria: Cálculo de Poupança e Saúde Financeira**

**RN-05 (Cálculo de Poupança Real):**
- Poupança Mensal = Renda Líquida (RN-04) - Soma Total de Gastos (RN-02/RN-03).
- Se Poupança Mensal <= R$ 0, o sistema indica que o usuário está "Déficit Orçamentário" e não pode iniciar investimentos. Recomendação: "Reduza seus gastos em pelo menos R$ X ou aumente sua renda."
- Se Poupança Mensal > 0, o sistema calcula a taxa de poupança (%) = (Poupança / Renda Líquida) * 100.

**RN-06 (Diagnóstico de Saúde Financeira):**
- **Gasto com Moradia**: Não deve exceder 30% da renda líquida. Se exceder: aviso "Seu gasto com moradia está acima do recomendado (30%)."
- **Gasto Total com Essenciais** (Moradia + Alimentação + Transporte + Contas Fixas): Não deve exceder 60% da renda líquida. Se exceder: aviso "Você está gastando mais de 60% em despesas essenciais. Pouca margem para poupança."
- **Taxa de Poupança Mínima para Investir**: O sistema recomenda que o usuário tenha pelo menos 10% de sua renda líquida disponível para poupar. Se tiver menos: "Sua capacidade de poupança é baixa (X%). Considere cortar gastos antes de investir."

**RN-07 (Composição da Reserva de Emergência):**
- Antes de sugerir investimentos, o sistema valida se o usuário tem uma reserva de emergência (Tesouro Direto + CDB) igual a 3-6 meses de gastos totais.
- Cálculo: Meses de Gastos Cobertos = Reserva Existente / Gasto Mensal Total.
- Se Meses Cobertos < 3: o sistema marca como prioritário "Construir Reserva de Emergência (3 meses mínimo)" antes de alocar em ativos de risco.

---

### **Categoria: Perfil de Risco e Objetivos**

**RN-08 (Classificação de Perfil de Risco):**
- O sistema apresenta um questionário com 5 perguntas (ex: "Se seu investimento caísse 20% em um mês, você venderia?").
- Baseado nas respostas, classifica o usuário em:
  - **Conservador**: <= 30% em ativos de risco (prioriza renda fixa).
  - **Moderado**: 30-60% em ativos de risco (equilíbrio entre renda fixa e ativos de risco).
  - **Agressivo**: > 60% em ativos de risco (maior exposição a ações/ETFs).
- A classificação é persistida como atributo do usuário para cálculos posteriores.

**RN-09 (Objetivos Financeiros Mapeados):**
- O usuário pode registrar até 3 objetivos principais com:
  - Nome (ex: "Fundo de Emergência", "Primeira Viagem", "Aposentadoria").
  - Valor alvo em R$.
  - Prazo em meses.
  - Prioridade (1 = máxima, 3 = mínima).
- Cada objetivo terá uma recomendação de alocação separada (RN-10).

---

### **Categoria: Recomendação de Alocação de Investimentos**

**RN-10 (Estratégia de Alocação por Perfil):**

Para um usuário com Poupança Mensal P e Perfil de Risco F:

- **Se F = Conservador:**
  - 70% → Renda Fixa (Tesouro SELIC + CDB de 100% do CDI).
  - 30% → Renda Fixa de Longo Prazo (Tesouro Prefixado 5+ anos ou CDB pós-fixado).
  - 0% → Ações/ETFs.

- **Se F = Moderado:**
  - 50% → Renda Fixa (Tesouro SELIC + CDB).
  - 30% → Renda Fixa de Longo Prazo (Tesouro Prefixado ou fundos de renda fixa).
  - 20% → Ações/ETFs diversificados (ex: Fundo de Índice do Ibovespa ou S&P 500).

- **Se F = Agressivo:**
  - 30% → Renda Fixa (Tesouro SELIC).
  - 20% → Renda Fixa de Longo Prazo (Tesouro Prefixado).
  - 50% → Ações/ETFs (diversificados entre setores e geografias).

**RN-11 (Alocação Mensal de Poupança):**
- A poupança mensal é alocada automaticamente conforme os percentuais de RN-10.
- Exemplo: Se poupança = R$ 1.000 e perfil = Moderado:
  - R$ 500 → Renda Fixa Curta.
  - R$ 300 → Renda Fixa Longa.
  - R$ 200 → Ações/ETFs.

**RN-12 (Priorização de Objetivos):**
- Se o usuário tem múltiplos objetivos (RN-09), a alocação é ajustada por prioridade:
  - Objetivo Prioridade 1: recebe 50% da poupança.
  - Objetivo Prioridade 2: recebe 30% da poupança.
  - Objetivo Prioridade 3: recebe 20% da poupança.
- A recomendação de ativo (RN-10) ainda prevalece (ex: "Dos 50% para Objetivo 1, 70% em renda fixa se perfil = Conservador").

**RN-13 (Validação de Viabilidade de Objetivos):**
- Para cada objetivo, o sistema calcula: "Meses para atingir meta" = Meta / Alocação Mensal para Esse Objetivo.
- Se Meses Calculados > Prazo Informado: aviso "Este objetivo é inviável com sua poupança atual. Você precisaria poupar R$ X/mês em vez de R$ Y/mês."
- Recomendação: "Aumente sua renda, reduza seus gastos ou estenda o prazo."

---

### **Categoria: Projeções de Crescimento**

**RN-14 (Taxas de Retorno Assumidas):**
- **Renda Fixa Curta (Tesouro SELIC, CDB até 2 anos):** 10% a.a. (estimativa conservadora).
- **Renda Fixa Longa (Tesouro Prefixado 5+ anos):** 12% a.a.
- **Ações/ETFs:** 9% a.a. (retorno histórico do Ibovespa ajustado para conservadorismo).
- Essas taxas são parametrizáveis, mas têm valores padrão.

**RN-15 (Cálculo de Projeção de Patrimônio):**
- Função: Patrimônio_Futuro = Aporte_Inicial + (Poupança_Mensal * Meses) + Juros_Acumulados.
- Para cada mês, o cálculo é feito com juros compostos:
  - Juros_Mês = Saldo_Anterior * (Taxa_Anual / 12).
  - Saldo_Novo = Saldo_Anterior + Poupança_Mês + Juros_Mês.
- A projeção é calculada para prazos: 1 ano, 5 anos, 10 anos, 20 anos.

**RN-16 (Cenários de Simulação):**
- O sistema gera 3 cenários:
  - **Pessimista:** -20% das taxas de retorno assumidas.
  - **Base:** Taxas nominais de RN-14.
  - **Otimista:** +20% das taxas de retorno assumidas.
- Cada cenário é exibido no relatório final para transparência.

---

### **Categoria: Relatório e Saída**

**RN-17 (Estrutura do Relatório Final):**
- O relatório deve conter, na ordem:
  1. Diagnóstico de Saúde Financeira (incluindo alertas de RN-06).
  2. Recomendação de Alocação (detalhando RN-10, RN-11).
  3. Cronograma de Objetivos (prazo vs meta, aviso de inviabilidade se aplicável).
  4. Projeção de Patrimônio em 3 cenários (1, 5, 10, 20 anos).
  5. Próximos Passos Recomendados (ex: "Abra uma conta no Tesouro Direto" ou "Considere cortar gastos com lazer").
- Formato: texto estruturado + tabelas + possível JSON para processamento posterior.

**RN-18 (Persistência de Dados):**
- Todos os dados de entrada (renda, gastos, perfil, objetivos) são salvos em um arquivo estruturado (JSON ou CSV) para que o usuário possa reutilizar / atualizar seu plano em futuras execuções.
- Arquivo padrão: `dados_usuario.json` ou similar.

**RN-19 (Mensagens de Aviso e Validação):**
- Sempre que uma validação falhar (RN-01, RN-03, RN-06, RN-13), o sistema exibe mensagem clara em português e oferece a opção de corrigir dados antes de prosseguir.
- Exemplo: "Erro: Renda informada (R$ 50.000) é maior que o máximo permitido (R$ 1.000.000). Revise."

---

## 1.3 Resumo das Regras de Negócio por Área

| Área | Regras |
|------|--------|
| **Coleta e Validação** | RN-01, RN-02, RN-03, RN-04 |
| **Cálculo e Diagnóstico** | RN-05, RN-06, RN-07 |
| **Perfil e Objetivos** | RN-08, RN-09 |
| **Recomendação** | RN-10, RN-11, RN-12, RN-13 |
| **Projeção** | RN-14, RN-15, RN-16 |
| **Saída e Persistência** | RN-17, RN-18, RN-19 |

---

## 1.4 Fluxo de Entrada de Dados (Alto Nível)

```
INÍCIO
   ↓
[MODO: CLT ou PJ?] → Aplica RN-04 (Carga Tributária)
   ↓
[RENDA BRUTA?] → Valida RN-01
   ↓
[GASTOS POR CATEGORIA] → Valida RN-02, RN-03
   ↓
[CALCULA: Renda Líquida, Poupança] → Aplica RN-05, RN-06
   ↓
[PERFIL DE RISCO?] → Aplica RN-08 (Questionário)
   ↓
[OBJETIVOS FINANCEIROS?] → Registra RN-09 (até 3 objetivos)
   ↓
[VALIDA OBJETIVOS] → Aplica RN-13 (inviabilidade?)
   ↓
[ALOCA INVESTIMENTOS] → Aplica RN-10, RN-11, RN-12
   ↓
[PROJETA CRESCIMENTO] → Aplica RN-14, RN-15, RN-16
   ↓
[GERA RELATÓRIO] → Aplica RN-17, RN-18
   ↓
RELATÓRIO EXIBIDO NO TERMINAL
   ↓
[SALVA DADOS] → RN-18
   ↓
FIM
```

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

# Requisitos — InvestPlan

> **Responsabilidades de preenchimento:**
> - **Elder** → Seção 1 (Elicitação)
> - **Felipe** → Seção 2 (Histórias de Usuário)
> - **Guilherme** → Seção 3 (Validação)

---

## 1. Síntese da Elicitação

> _Responsável: **Elder**_

### 1.1 Técnicas de Elicitação Utilizadas

<!-- Descreva quais técnicas foram usadas para levantar os requisitos.
     Ex: análise de similares, pesquisa de mercado, questionário informal, etc. -->

### 1.2 Análise de Similares

<!-- Liste os sistemas similares analisados (ex: GuiaBolso, Mobills, planilhas do Me Poupe).
     Para cada um, descreva brevemente o que foi observado e o que o InvestPlan faz diferente ou melhor. -->

| Sistema Analisado | O que faz | Limitação identificada | O que o InvestPlan resolve |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

### 1.3 Regras de Negócio Identificadas

<!-- Liste as regras de negócio que o sistema deve seguir.
     Ex: cálculo de reserva de emergência, critérios de perfil de risco, regras de alocação por perfil, etc.
     Numere cada regra para facilitar o rastreamento nas HUs. -->

- **RN-01:**
- **RN-02:**
- **RN-03:**
- **RN-04:**
- **RN-05:**

### 1.4 Fontes Consultadas na Elicitação

<!-- Liste as fontes (já presentes no README ou novas) que embasaram as regras de negócio acima. -->

---

## 2. Histórias de Usuário

> _Responsável: **Felipe**_
>
> **Legenda de prioridade:** Alta = essencial para o fluxo principal / Média = importante mas não bloqueante / Baixa = desejável
>
> **Legenda de sprint:** Sprint 3 = desenvolvimento principal / Sprint 4 = refinamento

---

### HU-01 — Otimização Orçamentária e Cálculo de Sobra

**Como** um adulto em fase de organização financeira,
**Quero** inserir minha renda mensal e despesas básicas no terminal,
**Para** descobrir minha capacidade real de poupança mensal.

**Regras de negócio relacionadas:** RN-XX (Aguardando Elicitação)

**Critérios de Aceite:**
- [ ] CA-01: O sistema deve solicitar a entrada do valor da renda mensal líquida.
- [ ] CA-02: O sistema deve permitir que o usuário insira o valor total estimado de gastos.
- [ ] CA-03: O sistema deve calcular a diferença (Renda - Gastos) e exibir a sobra disponível.
- [ ] CA-04: Se a sobra calculada for menor ou igual a zero, o sistema deve emitir um aviso de "Orçamento Estourado", bloquear o avanço para a etapa de investimentos e orientar o corte de gastos.

**Prioridade:** Alta | **Sprint prevista:** Sprint 3

---

### HU-02 — Definição do Perfil de Risco

**Como** um iniciante em investimentos,
**Quero** responder a um questionário rápido sobre prazos e tolerância a perdas,
**Para** que o sistema identifique adequadamente o meu perfil de investidor.

**Regras de negócio relacionadas:** RN-XX (Aguardando Elicitação)

**Critérios de Aceite:**
- [ ] CA-01: O sistema deve exibir perguntas de múltipla escolha diretamente no terminal.
- [ ] CA-02: Se o usuário selecionar opções que indicam aversão total à perda de capital ou prazo menor que 1 ano, o perfil deve ser forçado para "Conservador".
- [ ] CA-03: O sistema deve registrar e exibir o perfil final (Conservador, Moderado ou Arrojado).

**Prioridade:** Alta | **Sprint prevista:** Sprint 3

---

### HU-03 — Recomendação de Alocação de Recursos (Strategy)

**Como** um usuário com capacidade de poupança positiva,
**Quero** receber uma sugestão detalhada de onde investir meu dinheiro,
**Para** começar a investir com segurança de acordo com o meu perfil.

**Regras de negócio relacionadas:** RN-XX (Aguardando Elicitação)

**Critérios de Aceite:**
- [ ] CA-01: O sistema deve processar a "sobra mensal" (HU-01) e o perfil (HU-02) para injetar na estratégia correta de cálculo.
- [ ] CA-02: Para o perfil "Conservador", a sugestão deve ser a alocação de 100% da sobra em Renda Fixa (ex: Tesouro Selic / CDB).
- [ ] CA-03: A saída no terminal deve exibir os valores recomendados em Reais (R$), mostrando a divisão exata baseada na sobra do usuário.

**Prioridade:** Alta | **Sprint prevista:** Sprint 3

---

### HU-04 — Geração de Relatório Financeiro

**Como** um usuário que concluiu a análise,
**Quero** que o sistema consolide todas as informações em um relatório,
**Para** que eu tenha um registro claro do meu plano de ação financeiro.

**Regras de negócio relacionadas:** RN-XX (Aguardando Elicitação)

**Critérios de Aceite:**
- [ ] CA-01: O sistema deve gerar um resumo contendo: Renda, Gastos, Sobra, Perfil de Risco e a Estratégia de Alocação recomendada.
- [ ] CA-02: O sistema deve oferecer a opção de salvar esse relatório em um arquivo de texto estruturado (ex: `.txt` ou `.csv`) no diretório local.

**Prioridade:** Média | **Sprint prevista:** Sprint 3

---

### HU-05 — Tratamento de Entradas Inválidas no Terminal

**Como** um usuário interagindo com uma interface de texto,
**Quero** ser alertado caso eu digite um formato de dado incorreto,
**Para** que o sistema não trave inesperadamente (crash) e eu possa corrigir a informação.

**Regras de negócio relacionadas:** N/A (Requisito Não-Funcional / Engenharia)

**Critérios de Aceite:**
- [ ] CA-01: Se o sistema pedir um número (ex: Renda) e o usuário digitar letras ou símbolos, o sistema deve exibir a mensagem de erro "Entrada inválida. Por favor, digite apenas números."
- [ ] CA-02: Após o erro, o sistema deve repetir a pergunta original sem encerrar a execução do programa.

**Prioridade:** Alta | **Sprint prevista:** Sprint 4

---

### 2.1 Backlog Priorizado

| # | História | Prioridade | Sprint |
|---|---|---|---|
| HU-01 | Otimização Orçamentária e Cálculo de Sobra | Alta | Sprint 3 |
| HU-02 | Definição do Perfil de Risco | Alta | Sprint 3 |
| HU-03 | Recomendação de Alocação de Recursos | Alta | Sprint 3 |
| HU-05 | Tratamento de Entradas Inválidas no Terminal | Alta | Sprint 4 |
| HU-04 | Geração de Relatório Financeiro | Média | Sprint 3 |

---

## 3. Validação dos Requisitos

> _Responsável: **Guilherme**_

### 3.1 Ambiguidades Encontradas

| ID | HU(s) afetada(s) | Descrição da ambiguidade | Resolução adotada |

|---|---|---|---|

| AMB-01 |HU-01|O termo "Gastos Básicos/Estimados" na descrição da HU não deixa claro se o usuário digita um valor único consolidado ou se deve detalhar por categorias.|Ficou definido que a interface CLI solicitará obrigatoriamente os gastos divididos nas 8 categorias descritas na RN-02, realizando a soma de forma automática para o cálculo da sobra.|

| AMB-02 |HU-02|O critério de aceite CA-02 fala em "opções que indicam aversão total à perda". Quais opções ou pesos exatos no questionário definem isso?|O questionário terá 5 perguntas com pontuações de 1 a 3. Se a pergunta específica de tolerância a quedas receber a resposta de peso mínimo (aversão total), o perfil será forçado para Conservador, independente da soma das outras respostas.|

| AMB-03 |HU-04|O CA-02 menciona "salvar em arquivo de texto estruturado (ex: .txt ou .csv)", deixando o formato definitivo em aberto.|Para manter o alinhamento com a RN-18 (Persistência) e com o escopo do projeto, o sistema exportará um arquivo legível .txt para o usuário e salvará o estado interno em um arquivo estruturado .json.|

### 3.2 Conflitos Identificados

| ID | HUs em conflito | Descrição do conflito | Resolução adotada |

|---|---|---|---|

| CONF-01 |HU-01 vs RN-01|A HU-01 (CA-04) diz que se a sobra for menor ou igual a zero o sistema bloqueia o avanço. Contudo, a RN-06 diz que o sistema exige no mínimo 10% de capacidade de poupança para recomendar investimentos.|O bloqueio total e aviso de "Déficit Orçamentário" ocorrerá se a sobra for $\le 0$. Se a sobra for positiva, mas menor que 10% da renda líquida, o sistema emitirá o alerta reflexivo da RN-06, mas permitirá que o usuário prossiga se ele assim desejar.|

| CONF-02 |HU-03 vs RN-10|A HU-03 (CA-02) prevê uma saída simplificada no terminal calculando e exibindo apenas o valor global de 100% em Renda Fixa. No entanto, a RN-10 exige uma granularidade maior, subdividindo esse montante em Renda Fixa Curta (70%) e Longa (30%). Embora ambos sejam Renda Fixa, há uma divergência no nível de detalhamento do cálculo e da exibição.|Foi definido que a RN-10 orientará a implementação do Módulo de Recomendação. O critério de aceite CA-02 da HU-03 será refinado para que a interface de texto detalhe as subcategorias de prazo em Reais (R$), garantindo que o comportamento do código reflita fielmente o algoritmo matemático completo da regra de negócio.|

### 3.3 Questões em Aberto

| ID | Descrição da questão | Impacto | Responsável | Prazo |

|---|---|---|---|---|

| QA-01 |Como o sistema deve se comportar caso o arquivo de persistência local (dados_usuario.json) esteja corrompido ou com formato inválido na inicialização?|Pode causar um crash no sistema logo na inicialização, violando o princípio de robustez do terminal.|Guilherme|02/06 (Sprint 2)|

| QA-02 |As taxas de retorno assumidas na RN-14 (10%, 12% e 9% a.a.) serão estáticas no código (hardcoded) ou carregadas de um arquivo de configuração parametrizável?|Impacta a facilidade de manutenção e refatoração do código na Sprint 4.|Elder|09/06 (Sprint 3)|

| QA-03 |Se o usuário cadastrar múltiplos objetivos (RN-12) cujas somas das metas ultrapassem drasticamente a projeção de patrimônio máximo, o sistema deve sugerir o reajuste de todos ou priorizar apenas o Objetivo 1?|Afeta a lógica algorítmica do Módulo de Recomendação/Relatório.|Felipe|09/06 (Sprint 3)|

### 3.4 Protótipo de Fluxo no Terminal

======================================================================
                     INVESTPLAN - SIMULADOR FINANCEIRO                
======================================================================

[1] Identificação do Regime de Trabalho:
Selecione seu regime:
(1) CLT (Desconto estimado de 11.5%)
(2) PJ / Autônomo (Desconto estimado de 20.0%)
Escolha: 1

[2] Coleta de Dados Financeiros:
Digite sua renda mensal bruta (R$): 5000.00
--- Carga tributária aplicada. Renda Líquida estimada: R$ 4425.00 ---

Informe seus gastos mensais por categoria:
1. Moradia (Aluguel, IPTU, Condomínio): R$ 1200.00
2. Alimentação (Supermercado, Restaurantes): R$ 600.00
3. Transporte (Combustível, Transporte Público): R$ 300.00
4. Saúde (Plano de Saúde, Farmácia): R$ 200.00
5. Educação (Faculdade, Cursos): R$ 400.00
6. Lazer e Cultura (Streaming, Viagens): R$ 300.00
7. Contas Fixas (Água, Luz, Internet): R$ 250.00
8. Outros Gastos: R$ 150.00

======================================================================
                        DIAGNÓSTICO FINANCEIRO                        
======================================================================
Soma Total de Gastos: R$ 3400.00
Sobra Mensal Disponível (Poupança Real): R$ 1025.00
Taxa de Poupança: 23.16% da renda líquida.

[ALERTA] Gasto com Moradia compromete 27.12% da renda líquida (Limite: 30%).
[OK] Gasto com Essenciais compromete 53.11% da renda líquida (Limite: 60%).
[OK] Capacidade de poupança adequada para iniciar investimentos (> 10%).

Deseja responder ao questionário de Perfil de Risco? (S/N): S

======================================================================
                         QUESTIONÁRIO DE PERFIL                       
======================================================================
Pergunta 1: Se seu investimento caísse 20% em um mês, o que você faria?
(1) Venderia imediatamente para evitar mais perdas.
(2) Manteria o investimento aguardando a recuperação.
(3) Compraria mais unidades aproveitando o preço baixo.
Escolha: 1

[... demais perguntas ...]

Seu Perfil de Investidor é: CONSERVADOR

======================================================================
                       ESTRATÉGIA DE ALOCAÇÃO                         
======================================================================
Com base na sua sobra de R$ 1025.00 e perfil CONSERVADOR, aloque:

- Renda Fixa Curta (70%): R$ 717.50 / mês
  -> Sugestão: Tesouro SELIC ou CDB 100% CDI com liquidez diária.
  
- Renda Fixa Longo Prazo (30%): R$ 307.50 / mês
  -> Sugestão: Tesouro IPCA+ ou CDB Pós-fixado.

- Ativos de Risco / Ações (0%): R$ 0.00 / mês

======================================================================
                  PROJEÇÃO DE PATRIMÔNIO (CENÁRIO BASE)               
======================================================================
Mantendo o aporte constante de R$ 1025.00/mês:
- Em 1 ano:  R$ 12.981,25
- Em 5 anos: R$ 81.110,43
- Em 10 anos: R$ 221.750,18

Deseja exportar o relatório detalhado (.txt)? (S/N): S
[Sucesso] Relatório salvo como 'plano_investplan.txt' no diretório local.

Obrigado por utilizar o InvestPlan! Finalizando o sistema...
======================================================================
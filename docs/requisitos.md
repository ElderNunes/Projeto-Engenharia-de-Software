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

<!-- Liste termos ou situações nas HUs que podem ser interpretados de mais de uma forma.
     Para cada ambiguidade, registre como a equipe decidiu resolvê-la. -->

| ID | HU(s) afetada(s) | Descrição da ambiguidade | Resolução adotada |
|---|---|---|---|
| AMB-01 |  |  |  |
| AMB-02 |  |  |  |
| AMB-03 |  |  |  |

### 3.2 Conflitos Identificados

<!-- Liste situações em que duas ou mais HUs se contradizem ou criam inconsistências entre si.
     Registre como o conflito foi ou será resolvido. -->

| ID | HUs em conflito | Descrição do conflito | Resolução adotada |
|---|---|---|---|
| CONF-01 |  |  |  |
| CONF-02 |  |  |  |

### 3.3 Questões em Aberto

<!-- Liste dúvidas que ainda não foram resolvidas e que podem impactar o desenvolvimento.
     Registre o responsável por resolver cada uma e o prazo. -->

| ID | Descrição da questão | Impacto | Responsável | Prazo |
|---|---|---|---|---|
| QA-01 |  |  |  |  |
| QA-02 |  |  |  |  |
| QA-03 |  |  |  |  |

### 3.4 Protótipo de Fluxo no Terminal

<!-- Descreva ou ilustre (em texto/ASCII) como seria a interação do usuário com o sistema no terminal.
     Isso ajuda a validar se as HUs fazem sentido na prática. -->

```
Exemplo de estrutura (substituir pelo fluxo real):

=== InvestPlan ===
[1] Cadastrar renda e gastos
[2] Ver diagnóstico financeiro
[3] Definir perfil de risco
[4] Ver recomendações de alocação
[5] Gerar relatório
[0] Sair

Escolha uma opção: _
```
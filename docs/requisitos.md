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

### HU-01 — [Título da História]

**Como** [tipo de usuário],
**Quero** [ação ou funcionalidade],
**Para** [objetivo ou benefício].

**Regras de negócio relacionadas:** RN-XX

**Critérios de Aceite:**
- [ ] CA-01:
- [ ] CA-02:
- [ ] CA-03:

**Prioridade:** | **Sprint prevista:**

---

### HU-02 — [Título da História]

**Como** [tipo de usuário],
**Quero** [ação ou funcionalidade],
**Para** [objetivo ou benefício].

**Regras de negócio relacionadas:** RN-XX

**Critérios de Aceite:**
- [ ] CA-01:
- [ ] CA-02:
- [ ] CA-03:

**Prioridade:** | **Sprint prevista:**

---

### HU-03 — [Título da História]

**Como** [tipo de usuário],
**Quero** [ação ou funcionalidade],
**Para** [objetivo ou benefício].

**Regras de negócio relacionadas:** RN-XX

**Critérios de Aceite:**
- [ ] CA-01:
- [ ] CA-02:
- [ ] CA-03:

**Prioridade:** | **Sprint prevista:**

---

### HU-04 — [Título da História]

**Como** [tipo de usuário],
**Quero** [ação ou funcionalidade],
**Para** [objetivo ou benefício].

**Regras de negócio relacionadas:** RN-XX

**Critérios de Aceite:**
- [ ] CA-01:
- [ ] CA-02:
- [ ] CA-03:

**Prioridade:** | **Sprint prevista:**

---

### HU-05 — [Título da História]

**Como** [tipo de usuário],
**Quero** [ação ou funcionalidade],
**Para** [objetivo ou benefício].

**Regras de negócio relacionadas:** RN-XX

**Critérios de Aceite:**
- [ ] CA-01:
- [ ] CA-02:
- [ ] CA-03:

**Prioridade:** | **Sprint prevista:**

---

### HU-06 — [Título da História] _(opcional)_

**Como** [tipo de usuário],
**Quero** [ação ou funcionalidade],
**Para** [objetivo ou benefício].

**Regras de negócio relacionadas:** RN-XX

**Critérios de Aceite:**
- [ ] CA-01:
- [ ] CA-02:
- [ ] CA-03:

**Prioridade:** | **Sprint prevista:**

---

### 2.1 Backlog Priorizado

<!-- Após escrever todas as HUs, liste-as aqui em ordem de prioridade de implementação. -->

| # | História | Prioridade | Sprint |
|---|---|---|---|
| HU-01 |  |  |  |
| HU-02 |  |  |  |
| HU-03 |  |  |  |
| HU-04 |  |  |  |
| HU-05 |  |  |  |
| HU-06 |  |  |  |

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
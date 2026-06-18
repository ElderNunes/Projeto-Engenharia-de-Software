# Estratégia de Testes Automatizados — InvestPlan

> Este documento atende aos requisitos da **Sprint 4** da disciplina de Engenharia de Software. Aqui registramos nossa abordagem para garantir a qualidade matemática e a robustez do núcleo do sistema, bem como a cobertura e as lacunas deixadas.

---

## 1. Estratégia e Ferramental Escolhido

Para a suíte de testes do InvestPlan, optamos pela biblioteca nativa do Python **`unittest`**. A escolha arquitetural se baseou em dois fatores principais:

- **Integração direta com a linguagem**, sem exigir dependências externas;
- **Forte adequação ao padrão de testes orientados a objetos** (xUnit).

O foco da nossa abordagem foi o **Teste de Caixa Branca** isolado nas regras de negócio (*Domain Layer*). O objetivo principal foi garantir a testabilidade das funções matemáticas puras e dos algoritmos de classificação do sistema. Ao isolar o núcleo da aplicação da interface de usuário, garantimos que os testes rodem em milissegundos e validem estritamente a lógica financeira do projeto.

---

## 2. Cobertura e Prevenção de Falhas Críticas

A divisão da cobertura foi realizada para blindar os módulos críticos de decisão e cálculo do software. Para cada classe testada, aplicamos a **tríade de validação**: Sucesso, Borda e Falha.

### `motor_investimento.py` — Felipe

| Tipo | Descrição |
|------|-----------|
| ✅ Sucesso | Validação da distribuição percentual correta da carteira com base nos perfis de risco. |
| ⚠️ Borda | Comportamento do motor com valores de investimento muito baixos (frações de centavos). |
| ❌ Falha | Bloqueio de envio de dados incompatíveis ou valores nulos. |

### `orcamento.py` e `projecao.py` — Guilherme

| Tipo | Descrição |
|------|-----------|
| ✅ Sucesso | Cálculo preciso de sobras orçamentárias e juros compostos ao longo do tempo. |
| ⚠️ Borda | Simulações com taxa de juros zerada ou meses de projeção equivalentes a zero. |
| ❌ Falha | Tratamento de despesas maiores que a receita (saldo negativo) e prevenção de divisão por zero. |

### `perfil_risco.py` — Elder

| Tipo | Descrição |
|------|-----------|
| ✅ Sucesso | Validação do caminho feliz para as classificações de **Conservador**, **Moderado** e **Arrojado**. |
| ⚠️ Borda | Teste dos limites matemáticos exatos de transição entre perfis (ex: nota-limite entre Moderado e Arrojado) e acionamento da regra de negócio de *Fail-Fast* para aversão a risco. |
| ❌ Falha | Disparo de `ValueError` e `AttributeError` via injeção de listas vazias, quantidades incorretas de respostas e tipos de dados incompatíveis. |

---

## 3. Lacunas Não Cobertas e Tratamento de Exceções

Para esta Sprint, tomamos a **decisão arquitetural consciente** de não realizar testes automatizados nas camadas de Interface do Usuário (CLI) e de Persistência de Dados (File I/O).

### Camada CLI — `main.py`

Não foram implementados testes que simulam o input do teclado (`input()`) ou capturam os prints no console. A interface é volátil e testes de UI neste momento gerariam alto custo de manutenção.

### Camada de Arquivos — `relatorio.py`

A geração de arquivos `.txt` (como o `plano_investplan.txt`) não é coberta pelo `unittest`.

### Justificativa e Mitigação

Para suprir a ausência de testes automatizados na manipulação de arquivos, adotamos duas técnicas no código de produção:

1. **Tratamento de exceções robusto** via `try/except`;
2. **Escrita atômica**: o sistema gera um arquivo temporário (`.tmp`) durante a escrita do relatório e só o substitui via `os.replace()` em caso de sucesso absoluto.

Essa abordagem mitiga os riscos de corrupção de arquivos em caso de falha de hardware, sem a necessidade de simular esses eventos extremos via testes automatizados.
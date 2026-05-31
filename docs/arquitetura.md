# Projeto da Aplicação e Arquitetura — InvestPlan

## 1. Registro de Decisões Arquiteturais (ADR) e Histórico

Para garantir o rastreamento das decisões e o alinhamento com os requisitos de engenharia, todas as mudanças estruturais e padronizações estão registradas abaixo:

| Data | Decisão / Alteração | Motivo e Trade-offs | Responsável |
|---|---|---|---|
| 30/05/2026 | Definição do Padrão Strategy para Alocação | Necessidade de evitar estruturas condicionais complexas e permitir fácil expansão de novos perfis no futuro. | Felipe |
| 30/05/2026 | Isolamento da Lógica de Negócios (Core) | Separar a matemática financeira da interface do terminal (CLI) para viabilizar testes automatizados isolados na Sprint 4. | Felipe |
| 30/05/2026 | Adoção de Clean Code funcional | Proibição de comentários inline para forçar a equipe a usar nomes de variáveis autodescritivas. | Felipe |
| 31/05/2026 | Adopção do Git Flow Simplificado e Commits Semânticos | Garantir a integridade do código em desenvolvimento paralelo e padronizar o histórico de alterações para auditoria rápida. | Elder |
| 31/05/2026 | Escolha de Interface via Linha de Comando (CLI) | Maximizar a velocidade de desenvolvimento e portabilidade a custo zero, aceitando o trade-off de uma experiência visual limitada (UX). | Elder |
| 31/05/2026 | Implementação do Padrão Facade na Interface | Desacoplar a camada visual das regras de negócio, centralizando o fluxo e permitindo futuras trocas de interface sem impactar o Core. | Elder |

---

## 2. Padrões de Codificação e Gestão de Qualidade

> **Responsável:** Felipe (Clean Code), Elder (Controle de Versão), Guilherme (Tipagem e Tratamento de Erros)

### 2.1 Diretrizes de Clean Code e Nomenclatura (Felipe)
O código base do InvestPlan deve focar na clareza estrutural e ser autodocumentado. Para garantir o mais alto nível de legibilidade e manutenção, a equipe deve seguir rigorosamente as seguintes regras na escrita do código Python:

* **Proibição de Comentários em Linha (Uso restrito a Docstrings):** O código não deve conter comentários explicativos em linha (`#`) para justificar lógicas complexas. Se um trecho de código precisa de um comentário em linha para ser entendido, ele deve ser refatorado. No entanto, o uso de *docstrings* (`"""`) é permitido e encorajado exclusivamente para documentar o propósito de classes, contratos de interfaces públicas e retornos de funções.
* **Nomenclatura Autodescritiva:** A clareza do sistema dependerá da escolha dos nomes. Variáveis, funções e classes devem revelar exatamente sua intenção (ex: usar `calcular_capacidade_poupanca()` em vez de `calc_cp()`).
* **Funções de Responsabilidade Única (SRP):** Cada função deve realizar apenas uma operação. Funções extensas devem ser quebradas em métodos menores.

### 2.2 Diretrizes de Controle de Versão e Git Flow Simplificado (Elder)
Para garantir a integridade do código e permitir o desenvolvimento paralelo sem conflitos destrutivos, a equipe adotará um modelo derivado do Git Flow, simplificado para a dinâmica do projeto:

* **Estrutura de Branches:**
  * `main`: Produção. Contém apenas código 100% estável e testado. Protegida contra commits diretos.
  * `develop`: Integração. Branch de consolidação do trabalho da equipe onde ocorrem as preparações para entregas de sprint.
  * `feature/*`: Desenvolvimento de funcionalidades (ex: `feature/calculo-orcamento`, `feature/interface-cli`). Criadas a partir de `develop` e mescladas via Pull Request (PR) após revisão por outro membro da equipe.
* **Padronização de Commits (Commits Semânticos):** Mensagens de commit devem ser claras e usar prefixos normatizados para facilitar a leitura automática do histórico:
  * `feat:` Quando uma nova funcionalidade é adicionada (ex: `feat: implementa loop principal da CLI`).
  * `fix:` Quando uma correção de bug é realizada (ex: `fix: corrige validacao de input de renda`).
  * `refactor:` Mudança no código que não altera comportamento (ex: `refactor: renomeia variaveis para clareza`).
  * `docs:` Alterações exclusivas na documentação (ex: `docs: atualiza adr da arquitetura`).

*(Espaço reservado para o Guilherme adicionar Type Hinting)*

---

## 3. Diagrama de Arquitetura e Trade-offs

A arquitetura do InvestPlan adota uma separação por camadas estruturais (Layered Architecture) para isolar a interface de texto, a lógica financeira e a persistência de arquivos.

```mermaid
flowchart TD
    A[Camada de Interface / CLI] -->|Usa| B(Camada de Lógica de Negócios / Core)
    B -->|Lê / Salva| C[(Camada de Persistência / JSON)]
```

### 3.1 Camada de Lógica de Negócios / Core (Responsável: Felipe)
Esta camada é o "motor" do InvestPlan, responsável por processar os cálculos orçamentários, avaliar os pesos do questionário de risco e aplicar a matemática de alocação e projeção de juros (conforme regras RN-01 a RN-08).

* **Trade-off Justificado:** Optamos por um isolamento total e rigoroso desta camada em relação à camada de interface (CLI). Nenhuma classe de negócios possui comandos de `print()` ou `input()`. O *trade-off* dessa decisão é um leve aumento na verbosidade estrutural, exigindo a passagem de objetos e retornos formatados entre os arquivos. No entanto, essa escolha é justificada porque permite que toda a matemática financeira seja testada de forma isolada através do módulo `unittest` na Sprint 4, garantindo a confiabilidade dos cálculos do sistema sem depender da interação do usuário.

### 3.2 Camada de Interface / CLI (Responsável: Elder)
Esta camada é a porta de entrada da aplicação, encarregada unicamente de capturar as entradas textuais do usuário, exibir menus estruturados no terminal e renderizar os outputs de forma limpa e amigável.

* **Trade-off Justificado:** A escolha por uma interface em Linha de Comando (CLI) textual foi tomada em detrimento de uma interface gráfica (GUI) ou Web para este estágio do projeto. O *trade-off* negativo é uma experiência de usuário (UX) mais árida e limitada visualmente. Contudo, o impacto positivo é massivo na velocidade de desenvolvimento, na portabilidade imediata (roda em qualquer terminal Python sem dependências de sistema operacional) e no custo de infraestrutura zero. Essa simplicidade na camada visual permitiu concentrar o esforço de engenharia na robustez dos algoritmos financeiros e na qualidade arquitetural do Core.

*(Espaço reservado para o Guilherme justificar a Persistência Local)*

---

## 4. Padrões de Projeto

O sistema faz uso intencional de Padrões de Projeto (Design Patterns) para resolver problemas recorrentes de engenharia de software de forma limpa e escalável.

### 4.1 Padrão Strategy: Módulo de Alocação (Responsável: Felipe)
O padrão comportamental **Strategy** foi escolhido para encapsular os diferentes algoritmos de recomendação de investimentos do InvestPlan.

* **Problema a ser resolvido:** O sistema precisa recomendar alocações percentuais diferentes baseadas na sobra financeira e no perfil de risco do usuário (Conservador, Moderado, Arrojado). Fazer isso através de longas cadeias de `if/else` tornaria o código frágil e difícil de testar.
* **Solução e Classes Reais:** Criamos uma interface base/classe abstrata chamada `EstrategiaAlocacao` que define o contrato obrigatório `calcular_alocacao(sobra: float)`. Criamos classes concretas que herdam dessa base: `AlocacaoConservadora`, `AlocacaoModerada` e `AlocacaoArrojada`. Cada uma possui sua própria regra matemática injetada. O contexto do sistema avalia o resultado do questionário do usuário (HU-02) e instancia dinamicamente apenas a estratégia correta (HU-03).
* **Benefício Arquitetural:** O módulo fica aberto para extensão e fechado para modificação (Princípio OCP do SOLID). Se no futuro decidirmos criar um perfil "Ultra-Arrojado", basta adicionar uma nova classe, sem risco de quebrar o código dos perfis já existentes.

### 4.1.1 Diagrama de Classes UML (Strategy)

```mermaid
classDiagram
    class ContextoAlocacao {
        -_estrategia: EstrategiaAlocacao
        +definir_estrategia(estrategia: EstrategiaAlocacao) void
        +executar_alocacao(sobra: float) dict
    }
    class EstrategiaAlocacao {
        <<abstract>>
        +calcular_alocacao(sobra: float)* dict
    }
    class AlocacaoConservadora {
        +calcular_alocacao(sobra: float) dict
    }
    class AlocacaoModerada {
        +calcular_alocacao(sobra: float) dict
    }
    class AlocacaoArrojada {
        +calcular_alocacao(sobra: float) dict
    }

    ContextoAlocacao --> EstrategiaAlocacao : mantém_referência
    EstrategiaAlocacao <|-- AlocacaoConservadora : implementa
    EstrategiaAlocacao <|-- AlocacaoModerada : implementa
    EstrategiaAlocacao <|-- AlocacaoArrojada : implementa
```

### 4.1.2 Detalhamento dos Módulos e Atributos Reais do Código

* **`ContextoAlocacao`:** Classe que interage com a interface de comando. Contém o estado da alocação e delega a computação dos percentuais à estratégia ativa que foi injetada após a avaliação do questionário.
* **`EstrategiaAlocacao`:** Interface abstrata que dita o contrato padrão para todos os algoritmos de cálculo. Garante que qualquer nova estratégia implemente o método de cálculo de forma consistente.
* **Classes Concretas (`AlocacaoConservadora`, `AlocacaoModerada`, `AlocacaoArrojada`):** Contêm os coeficientes matemáticos específicos de cada perfil de risco (conforme a regra RN-07), processando o valor numérico da sobra orçamentária e devolvendo um dicionário estruturado com as quantias exatas destinadas a cada ativo.

### 4.2 Padrão Facade: Orquestrador de Interface e Fluxo (Responsável: Elder)
O padrão estrutural **Facade** (Fachada) foi adotado como o ponto central de controle da interface textual, atuando como um mediador unificado entre o loop do terminal e o ecossistema de lógica de negócios.

* **Problema a ser resolvido:** A Camada de Interface precisa gerenciar múltiplos menus (Orçamento, Questionário de Risco, Simulação de Alocação) e disparar chamadas para diversas regras de negócio diferentes. Se a lógica da CLI fizesse chamadas diretas a todas as classes do Core, o código da interface ficaria altamente acoplado à implementação das classes de negócio. Qualquer mudança em um método financeiro exigiria alterar a tela do terminal.
* **Solução e Classes Reais:** Criamos a classe `InvestPlanFacade`. Ela expõe métodos de alto nível para o loop do terminal (como `orquestrar_fluxo_orcamento()` ou `gerar_diagnostico_completo()`). Por trás dos panos, o Facade instancia as classes de negócio do Core, passa os parâmetros, consolida as respostas do motor econômico e devolve os dados mastigados para a CLI apenas exibir.
* **Benefício Arquitetural:** Alto desacoplamento (Princípio de Segregação de Interfaces). A CLI conversa apenas com o Facade. Se no futuro o InvestPlan migrar de terminal (CLI) para a Web (FastAPI/Django), o Core e as telas não sofrerão impactos; bastará plugar a nova interface na mesma Fachada (`InvestPlanFacade`).

### 4.2.1 Diagrama de Classes UML (Facade)

```mermaid
classDiagram
    class MenuTerminal {
        +iniciar_sistema() void
        -exibir_menu_principal() void
        -capturar_opcao() int
    }
    class InvestPlanFacade {
        -_gerenciador_orcamento: GerenciadorOrcamento
        -_avaliador_risco: AvaliadorRisco
        -_contexto_alocacao: ContextoAlocacao
        +processar_orcamento(dados: dict) dict
        +avaliar_perfil(respostas: list) string
        +calcular_investimentos(sobra: float, perfil: string) dict
    }
    class GerenciadorOrcamento {
        +validar_renda(bruta: float) bool
        +calcular_liquida(bruta: float, tipo: string) float
    }
    class AvaliadorRisco {
        +computar_score(respostas: list) string
    }

    MenuTerminal --> InvestPlanFacade : usa_unicamente
    InvestPlanFacade --> GerenciadorOrcamento : orquestra
    InvestPlanFacade --> AvaliadorRisco : orquestra
```

*(Espaço reservado para o Guilherme documentar o Singleton)*

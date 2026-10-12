# Registro do uso de IA

## Ferramenta

Codex, modelo GPT-6, utilizado como assistente de desenvolvimento em 12/10/2026.
A aplicação não chama modelos de IA nem exige chaves de API.

## Modo adotado no MVP

O MVP adota o **Modo 1 — IA como copiloto de desenvolvimento**, recomendado
para a base no material fornecido. A IA auxilia planejamento, implementação,
testes, revisão e documentação; as decisões são revisadas pelo aluno.

O **Modo 2 — IA durante a execução para sugerir prioridades** permanece como
evolução futura. Também está previsto, sem implementação nesta versão, um
fallback local para quando não houver chave de API. Esse fallback poderá usar
regras determinísticas, sem chamadas externas ou custos de serviços de IA;
não deve ser apresentado como inferência de um modelo.

Antes dessa evolução, definir critérios de prioridade, formato da sugestão e
justificativa, confirmação pelo usuário e testes dos modos remoto e local.
O MVP atual não sugere nem atribui prioridades automaticamente.

## Etapas

As solicitações e decisões do aluno estão organizadas em
[prompts do projeto](prompts-utilizados.md), com redação adaptada ao modelo da
apostila: Contexto, Objetivo, Estilo e Resposta.

1. Leitura das capturas da apostila: identificação dos quatro projetos e dos critérios de entrega.
2. Comparação de opções: recomendação inicial de RAG, seguida pela escolha do aluno de adaptar
   a API de tarefas para projetos de montagem de clientes.
3. Definição de requisitos e arquitetura mínima em camadas.
4. Geração de código da API e interface, com SQLite e contratos validados.
5. Geração de testes baseados nos requisitos e verificação automatizada dos resultados.
6. Documentação de instalação, exemplos, limitações e fluxo Git.

## Decisões revisadas

- Manter o escopo em projetos e tarefas, sem transformar o MVP em ERP.
- Calcular status do projeto, evitando conclusão incompatível com as tarefas.
- Rejeitar atualizações nulas e campos desconhecidos.
- Bloquear exclusão de projeto com tarefas.
- Renderizar textos do usuário com `textContent`, sem interpretar HTML.
- Testar isolamento e persistência com bancos temporários.

## Evidências

Histórico Git, suíte em `tests/`, workflow de CI e requisitos em `docs/requisitos.md`.
Na primeira execução local, os 40 testes passaram. O Ruff foi executado após a formatação.
O fluxo web foi exercitado em Edge headless com criação de projeto e três tarefas, mudança
de status, cálculo de 33% de progresso, filtro, bloqueio de exclusão e remoção final dos dados fictícios.
Foram inspecionadas capturas em 1440 px e 390 px, sem transbordamento horizontal ou erros JavaScript.
As capturas em `docs/images/` mostram somente os dados fictícios desse teste.
O material fornecido não exige percentual mínimo de cobertura; não foi atribuída uma meta fictícia.

Em 12/10/2026, o aluno confirmou o aceite final e a persistência após reiniciar o servidor.
Esse registro é a declaração do aluno, complementada pelos testes automatizados existentes;
não equivale à aprovação ou nota atribuída pelos professores.

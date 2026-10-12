# Registro do uso de IA

## Ferramenta

Codex, modelo GPT-6, utilizado como assistente de desenvolvimento em 12/10/2026.
A aplicação não chama modelos de IA nem exige chaves de API.

## Etapas

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

O aluno ainda deve revisar a aplicação e validar seu atendimento ao contexto de montagem
antes da entrega acadêmica final. O uso de IA não substitui essa revisão.

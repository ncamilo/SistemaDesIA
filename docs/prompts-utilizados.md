# Prompts do projeto

Pedidos da conversa organizados no formato da apostila, com redação adaptada.

## Prompt 1 — Análise da apostila e proposta inicial

```text
Contexto: Estou desenvolvendo um trabalho de pós-graduação em IA. Forneci um documento com o padrão do miniprojeto. Use Python e FastAPI, GitHub, versionamento, aplique engenharia de software e testes.
Objetivo: Examinar a documentação, listar os projetos sugeridos e recomendar uma opção relacionada ao meu histórico disponível. Identificar os requisitos, orientar o desenvolvimento e os testes.
Estilo: Analítico e organizado, separando exigências da apostila de recomendações.
Resposta: Lista dos projetos, comparação fundamentada, recomendação e requisitos de desenvolvimento, versionamento e testes.
```

## Prompt 2 — Escolha do domínio e limite do MVP

```text
Contexto: Após comparar os projetos, escolhi gerenciar tarefas relacionadas a pedidos de montagem de clientes. Preciso de MVP simples e funcional.
Objetivo: Adaptar o miniprojeto para permitir criar projetos de montagem, cadastrar tarefas por projeto e acompanhar sua execução, respeitando a documentação.
Estilo: Prático, com escopo delimitado e requisitos verificáveis.
Resposta: Proposta de MVP com funcionalidades essenciais, limites de escopo e sequência de implementação.
```

## Prompt 3 — Relato de interação e processo de engenharia

```text
Contexto: Cadastrei um projeto e tarefas, mas não percebi nenhuma mudança ao clicar no nome do projeto. Desenvolver planejamento, testes e commits incrementais.
Objetivo: Investigar o comportamento do clique e verificar se há planejamento, testes e histórico Git adequados para tratar o projeto.
Estilo: Diagnóstico técnico com evidências e passos verificáveis.
Resposta: Diagnóstico, lacunas de teste, plano de correção e registros de validação e versionamento.
```

## Prompt 4 — Esclarecimento da expectativa sobre status

```text
Contexto: Funcionamento: ao clicar em "Seus projetos" permite alterar o status do projeto de pendente para em andamento e depois finalizado.
Objetivo: Esclarecer como o status deve funcionar e recomendar uma solução simples e coerente com o escopo.
Estilo: Explicativo, usando exemplos do projeto.
Resposta: Explicação da regra de status recomendada, justificativa e orientação de uso na interface.
```

## Prompt 5 — Conferência do escopo e inicialização do servidor

```text
Contexto: Veja as diretrizes em um documento de escopo contendo objetivo, requisitos funcionais, não funcionais e fora de escopo. Quero usar novamente a aplicação.
Objetivo: Verificar se essas diretrizes estão documentadas e iniciar novamente o FastAPI quando necessário.
Estilo: Verificação objetiva por critério.
Resposta: Situação de cada item, indicação do documento de escopo e confirmação de acesso ao aplicativo.
```

## Prompt 6 — Healthcheck, contrato HTTP e testabilidade

```text
Contexto: Forneci documentos sobre qualidade de código e testabilidade. Eles mencionam tipagem, modularidade, pytest, healthcheck, CRUD, validação de payload e priorização assistida.
Objetivo: Adicionar uma rota healthcheck no ponto de entrada da aplicação e conferir a existência do contrato HTTP e dos critérios mostrados nas imagens.
Estilo: Técnico, com rastreabilidade entre critérios, código e testes.
Resposta: Rota e contrato do healthcheck, testes correspondentes e quadro de critérios atendidos e pendentes.
```

## Prompt 7 — Entendimento da priorização assistida

```text
Contexto: A avaliação de testabilidade mencionou priorização assistida, uma funcionalidade que ainda precisamos pensar.
Objetivo: Explicar o conceito e como poderia ser aplicado às tarefas de montagem deste projeto.
Estilo: Conceitual e prático, com exemplos relacionados ao domínio.
Resposta: Definição, exemplo de uso, proposta de escopo pequeno e implicações para implementação e testes.
```

## Prompt 8 — Decisão de evitar custos de IA no MVP

```text
Contexto: A priorização assistida pode exigir serviços com custo. O MVP deve continuar sem gerar custos de serviços de IA.
Objetivo: Deixar a priorização assistida prevista para uma atualização futura, sem integração paga agora.
Estilo: Planejamento enxuto, distinguindo o que existe do que será futuro.
Resposta: Registro da decisão, limites da versão atual e previsão da melhoria futura, sem apresentar funcionalidade inexistente como pronta.
```

## Prompt 9 — Organização das entregas

```text
Contexto: Estamos organizando o produto final e precisamos acertar a divisão em core, qualidade e release.
Objetivo: Explicar se essa organização se aplica ao projeto e apresentar o conteúdo e a situação de cada etapa.
Estilo: Comparativo e resumido.
Resposta: Quadro com core, qualidade e release, seus conteúdos e pendências, diferenciando etapas de versões publicadas.
```

## Prompt 10 — Preparação dos PRs pendentes

```text
Contexto: O desenvolvimento gerou pull requests ainda pendentes. Realinhe os requisitos para torná-los prontos.
Objetivo: Revisar os PRs, tratar apontamentos e dependências e verificar sua prontidão para integração.
Estilo: Revisão técnica orientada a evidências.
Resposta: Situação dos PRs, correções necessárias, verificações executadas e resultado da integração quando concluída.
```

## Prompt 11 — Retomada da revisão

```text
Contexto: Solicito continuar o trabalho de revisão já iniciado.
Objetivo: Retomar a revisão pendente e prosseguir com as verificações e correções necessárias.
Estilo: Continuação objetiva, sem reiniciar o planejamento do zero.
Resposta: Atualização do trabalho retomado, problemas encontrados, resultados dos testes e situação final dos PRs.
```

## Prompt 12 — Verificação do backlog e conclusão do core

```text
Contexto: O gerenciador já foi implementado verifique o backlog.md e se o core está concluído.
Objetivo: Verificar a existência do backlog e comparar as funcionalidades entregues com o escopo aprovado.
Estilo: Auditoria curta, baseada em arquivos e evidências.
Resposta: Confirmação sobre o backlog, estado do core e eventuais pendências.
```

## Prompt 13 — Consolidação do backlog e autorização da release

```text
Contexto: Quero consolidar o planejamento em backlog.md e gerar a release se o core estiver correto.
Objetivo: Consolidar o backlog, verificar a prontidão e publicar a release caso os critérios estejam atendidos.
Estilo: Operacional, com explicações curtas sobre cada etapa.
Resposta: Backlog organizado, explicação da release, resultados das verificações e links da versão publicada.
```

## Prompt 14 — Investigação de mensagem de erro

```text
Contexto: Vi uma mensagem de erro no Codex durante o trabalho, mas ainda não forneci o texto exato.
Objetivo: Investigar o que ocorreu e verificar se houve impacto no aplicativo ou nos arquivos do projeto.
Estilo: Diagnóstico baseado em evidências disponíveis.
Resposta: Verificações realizadas, situação do aplicativo e solicitação de detalhes adicionais se necessários.
```

## Prompt 15 — Esclarecimento da mensagem de erro

```text
Contexto: Em resposta ao pedido de detalhes, informo que a mensagem foi: o arquivo não pode ser acessado.
Objetivo: Refinar a investigação para problemas de acesso ou exibição do arquivo.
Estilo: Diagnóstico específico e conciso.
Resposta: Confirmação da existência e leitura do arquivo, hipótese fundamentada e alternativa de acesso se disponível.
```

## Prompt 16 — Entendimento do Mermaid

```text
Contexto: Foi apresentado um diagrama Mermaid na documentação, implemente ele.
Objetivo: Criar Mermaid e mostrar como ele se relaciona com a apresentação e documentação do projeto.
Estilo: Introdução simples com exemplo visual.
Resposta: Definição breve, exemplo de diagrama e indicação de onde ele aparece no projeto.
```

## Prompt 17 — Auditoria de prontidão e histórico

```text
Contexto: Quero saber, segundo a documentação, o que está pronto do core, qualidade e release se estão concluídos e se o GitHub fornece evidências para avaliação.
Objetivo: Confrontar a entrega com a documentação e verificar as evidências de desenvolvimento e validação.
Estilo: Auditoria estruturada com distinção entre conclusão técnica e avaliação acadêmica.
Resposta: Matriz de atendimento, situação das etapas, pendências e links para histórico, PRs, testes e release.
```

## Prompt 18 — Aceite final e esclarecimento dos requisitos acadêmicos

```text
Contexto: Confirmo que a priorização assistida não é obrigatória quando prevista como melhoria futura. Também confirmo o aceite final, a persistência após reiniciar e que toda a exigência está na documentação fornecida.
Objetivo: Rever a prontidão da entrega considerando essas confirmações e conferir se todos os itens foram contemplados.
Estilo: Conferência rastreável, diferenciando evidência técnica de declaração do aluno.
Resposta: Checklist final com evidências e atualização dos registros de aceite e pendências.
```

## Prompt 19 — Preparação do texto de submissão

```text
Contexto: A conferência da documentação e o registro do aceite foram concluídos. Solicitei continuar, sem acrescentar novos requisitos.
Objetivo: Dar continuidade à preparação da entrega a partir do trabalho concluído.
Estilo: Síntese organizada para apresentação do trabalho.
Resposta: Texto de acompanhamento da entrega com descrição do projeto, tecnologias, testes e links.
```

## Prompt 20 — Documento específico de arquitetura

```text
Contexto: O projeto precisa de um arquivo arquitetura-componentes.md com diagrama Mermaid.
Objetivo: Criar o documento de arquitetura de componentes de acordo com a implementação existente.
Estilo: Documentação técnica em Markdown com Mermaid.
Resposta: Arquivo docs/arquitetura-componentes.md com diagrama, responsabilidades dos componentes e explicação do fluxo.
```

## Prompt 21 — Registro dos prompts da conversa

```text
Contexto: Apresentei uma imagem intitulada Prompt 5 — Revisão de planejamento e solicitei um documento com os prompts usados neste chat.
Objetivo: Organizar os pedidos e decisões da conversa em um documento rastreável para apresentar o uso da IA no desenvolvimento.
Estilo: Registro documental organizado por etapa.
Resposta: Conteúdo de docs/prompts-utilizados.md, com título e bloco de Contexto, Objetivo, Estilo e Resposta para cada prompt.
```

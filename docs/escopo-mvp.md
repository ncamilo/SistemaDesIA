# Escopo do MVP — Gerenciador de projetos de montagem

## Contexto

Miniprojeto acadêmico de desenvolvimento assistido por IA. Adapta a micro-API de
tarefas da apostila para organizar pedidos de montagem de clientes. A aplicação
utiliza Python, FastAPI e SQLite, com interface web simples.

O cenário é o acompanhamento interno de montagens. Esta versão atende a uma
operação local, sem contas de usuário nem acesso compartilhado pela rede.

## Objetivo

Permitir cadastrar um projeto para um pedido de cliente, dividir a montagem em
tarefas e acompanhar sua execução até a conclusão. O MVP deve ser simples de
executar, testável e documentado, demonstrando o uso de IA no ciclo de desenvolvimento.

## Requisitos funcionais

Os identificadores seguem o documento [requisitos e arquitetura](requisitos.md),
que contém os critérios de aceitação detalhados.

| ID | Requisito |
| --- | --- |
| RF01 | Cadastrar e consultar projetos com título e cliente obrigatórios, referência de pedido e descrição opcionais. |
| RF02 | Editar projetos e excluir somente aqueles que não possuem tarefas. |
| RF03 | Cadastrar e listar tarefas vinculadas a um projeto existente, sem misturar projetos. |
| RF04 | Editar e excluir tarefas; alterar seu status entre pendente, em andamento e concluída. |
| RF05 | Filtrar as tarefas de um projeto por status. |
| RF06 | Calcular automaticamente o progresso e o status do projeto a partir das tarefas. |
| RF07 | Persistir projetos e tarefas entre reinicializações da aplicação. |
| RF08 | Oferecer interface web para cadastro e acompanhamento, além da API REST. |
| RF09 | Ao selecionar um projeto por clique ou teclado, mostrar seus detalhes e tarefas, com foco e rolagem adequados. |

### Regras de negócio

- Projeto sem tarefas ou com todas pendentes: Pendente, com progresso de 0%.
- Projeto com alguma tarefa iniciada ou concluída, mas não todas concluídas: Em andamento.
- Projeto com todas as tarefas concluídas: Concluído, com progresso de 100%.
- Progresso: quantidade de tarefas concluídas dividida pelo total, em percentual inteiro truncado.
- Reabrir ou adicionar tarefas recalcula o status; não há edição manual do status do projeto.
- A exclusão de projeto com tarefas é bloqueada. Não há exclusão automática em cascata.

## Requisitos não funcionais

| ID | Requisito | Critério de verificação |
| --- | --- | --- |
| RNF01 | Reprodutibilidade | Documentar instalação e execução no README e fixar dependências em arquivos requirements. |
| RNF02 | Manutenibilidade | Separar rotas, validação, serviços e persistência; manter regras de negócio fora da interface. |
| RNF03 | Testabilidade | Manter testes unitários, de integração e de navegador, com bancos temporários isolados dos dados de uso. |
| RNF04 | Qualidade contínua | Executar testes e análise estática no CI; integrar alterações após aprovação das verificações. |
| RNF05 | Integridade dos dados | Validar entradas, rejeitar campos desconhecidos ou inválidos e preservar vínculos entre tarefas e projetos. |
| RNF06 | Usabilidade | Exibir status e progresso claramente; permitir navegação por teclado nos cartões e uso em larguras de desktop e celular. |
| RNF07 | Operação local | Executar em localhost, sem credenciais externas; excluir banco local, arquivos temporários e segredos do Git. |
| RNF08 | Documentação e rastreabilidade | Manter escopo, arquitetura, exemplos, limitações, registro de uso da IA e histórico de commits significativos. |

Os requisitos acima refletem o MVP atual. Não há meta formal de latência,
carga simultânea, disponibilidade ou cobertura percentual. Os testes de interface
não representam uma auditoria completa de acessibilidade.

## Fora de escopo

- Login, perfis de acesso, múltiplas empresas e colaboração simultânea em rede.
- Responsáveis, prazos, dependências entre tarefas e notificações.
- Estoque, compras, orçamento, faturamento e emissão fiscal.
- Anexos, integração com equipamentos e execução automática de montagens.
- IA integrada à aplicação em tempo de execução; a IA auxilia o desenvolvimento.
- Priorização assistida: adiada por decisão do aluno para manter o MVP sem custos de serviços de IA.
- Hospedagem pública, alta disponibilidade, backup automático e metas de desempenho.
- Paginação e migrações de banco, previstas somente para evolução posterior.

## Critérios de entrega

Fluxo de projeto e tarefas funcional; persistência verificada; testes e lint aprovados;
README com instalação e exemplos; repositório público com commits incrementais;
créditos, licença e versão identificada. A entrega acadêmica final depende da revisão
do aluno e da conferência dos requisitos completos do curso.

## Referências internas

- [Requisitos, regras e arquitetura](requisitos.md)
- [Análise da apostila](analise-apostila.md)
- [Correção da navegação e testes de regressão](correcao-navegacao.md)
- [Registro do uso de IA](uso-ia.md)

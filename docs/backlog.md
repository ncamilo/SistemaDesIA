# Backlog do MVP

Atualizado em 12/10/2026. Versão de referência: **v1.0.0**.
Este arquivo acompanha execução e pendências; [escopo](escopo-mvp.md) e
[requisitos](requisitos.md) definem os comportamentos aceitos.

## Concluído — core

| Item | Requisito | Evidência |
| --- | --- | --- |
| Cadastro, consulta e edição de projetos por cliente/pedido | RF01, RF02 | `tests/test_api.py`: CRUD e validação |
| Exclusão protegida de projeto com tarefas | RF02 | Teste de conflito 409 e exclusão após remoção das tarefas |
| Tarefas vinculadas ao projeto, edição e exclusão | RF03, RF04 | Ciclo de execução e isolamento entre projetos |
| Filtro por status | RF05 | Testes de filtro e status inválido |
| Progresso e status automático, conclusão e reabertura | RF06 | `tests/test_progress.py` e testes de API/navegador |
| Persistência após reiniciar | RF07 | Teste com duas instâncias sobre o mesmo banco temporário |
| Interface responsiva e navegação por clique/teclado | RF08, RF09 | `browser_tests/test_project_navigation.py` |

**Core concluído para o escopo aprovado.** Priorização assistida não faz parte
desta versão, por decisão do aluno de evitar custos de serviços de IA.

## Concluído — qualidade

- [x] Arquitetura em rotas, schemas, serviços e repositório.
- [x] Tipagem explícita de funções públicas, lint e formatação com Ruff.
- [x] 44 testes unitários/API e quatro testes de navegador.
- [x] Contrato HTTP, erros documentados e OpenAPI/Swagger UI.
- [x] Healthcheck independente do banco, inclusive com falha de acesso no startup.
- [x] CI com testes de API e navegador; correção do achado de revisão do PR #4.
- [x] Escopo, requisitos não funcionais, licença, dependências fixadas e registro de uso de IA.

Evidências: [PR #1](https://github.com/ncamilo/SistemaDesIA/pull/1),
[PR #2](https://github.com/ncamilo/SistemaDesIA/pull/2),
[PR #3](https://github.com/ncamilo/SistemaDesIA/pull/3) e
[PR #4](https://github.com/ncamilo/SistemaDesIA/pull/4).
Os testes não equivalem a uma auditoria completa de segurança ou acessibilidade.

## Release — v1.0.0

Esta entrega marca a versão estável do **MVP local**, com código identificado pela
tag e notas de alterações no GitHub. Não representa hospedagem pública da aplicação
nem aprovação acadêmica. Não altera o esquema do banco de uso.

Critérios de publicação: testes e lint aprovados, PR integrado à `main`, tag no commit
integrado e notas de release com limitações explícitas.

Artefatos: [notas de versão](../CHANGELOG.md) e
[release v1.0.0](https://github.com/ncamilo/SistemaDesIA/releases/tag/v1.0.0).

## Pendente — entrega acadêmica

- [ ] Aluno executar e registrar a aceitação final com um pedido representativo.
- [ ] Confirmar com o curso se priorização assistida é obrigatória; se for, revisar
  o escopo antes de declarar atendimento integral ao roteiro.
- [ ] Conferir a rubrica completa e preparar os materiais de apresentação exigidos pelo curso.

Essas pendências não bloqueiam a publicação técnica deste MVP; não devem ser
apresentadas como requisitos acadêmicos já cumpridos.

## Evoluções futuras — sem compromisso nesta release

| Item | Observação |
| --- | --- |
| Priorização assistida | Adiada. Sem modelo, chave, endpoint ou chamadas pagas. Definir regras/fornecedor e critérios antes de implementar. |
| Remover aviso de depreciação do TestClient/HTTPX | Suíte passa; avaliar atualização compatível do adaptador de testes. |
| Autenticação e autorização | Necessárias antes de considerar acesso compartilhado em rede. |
| Responsáveis, prazos e dependências entre tarefas | Exigem ampliar requisitos de negócio. |
| Paginação, migrações e backup | Planejar conforme volume e forma de operação. |
| Readiness e recuperação automática do banco | Hoje falha no startup exige corrigir o acesso e reiniciar. |

## Como manter este backlog

Ao iniciar um item, registrar seu critério de aceitação e referência ao PR.
Marcar concluído somente com implementação, validação e integração comprovadas.
Novas funcionalidades exigem revisão explícita do escopo; não mover itens futuros
para o core apenas para justificar uma entrega.

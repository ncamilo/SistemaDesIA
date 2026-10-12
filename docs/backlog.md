# Backlog do MVP

Atualizado em 12/10/2026. Versão de referência: **v1.0.1**.
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
- [x] 46 testes unitários/API e seis testes de navegador.
- [x] Contrato HTTP, erros documentados e OpenAPI/Swagger UI.
- [x] Healthcheck independente do banco, inclusive com falha de acesso no startup.
- [x] CI com testes de API e navegador; correção do achado de revisão do PR #4.
- [x] Escopo, requisitos não funcionais, licença, dependências fixadas e registro de uso de IA.

Evidências: [PR #1](https://github.com/ncamilo/SistemaDesIA/pull/1),
[PR #2](https://github.com/ncamilo/SistemaDesIA/pull/2),
[PR #3](https://github.com/ncamilo/SistemaDesIA/pull/3) e
[PR #4](https://github.com/ncamilo/SistemaDesIA/pull/4).
Os testes não equivalem a uma auditoria completa de segurança ou acessibilidade.

## Release — v1.0.1

Esta entrega marca a versão estável do **MVP local**, com código identificado pela
tag e notas de alterações no GitHub. Não representa hospedagem pública da aplicação
nem aprovação acadêmica. Não altera o esquema do banco de uso.

Critérios de publicação: testes e lint aprovados, PR integrado à `main`, tag no commit
integrado e notas de release com limitações explícitas.

Artefatos: [notas de versão](../CHANGELOG.md) e
[release v1.0.1](https://github.com/ncamilo/SistemaDesIA/releases/tag/v1.0.1).

## Concluído — conferência de entrega

- [x] Aceite final confirmado pelo aluno em 12/10/2026.
- [x] Persistência após reiniciar o servidor confirmada pelo aluno, além do teste automatizado.
- [x] Aluno confirmou que a priorização assistida não é obrigatória se prevista como melhoria futura.
- [x] Checklist da apostila fornecida reconferido; ver [conferência de entrega](conferencia-entrega.md).
- [x] Arquitetura de componentes e diagrama Mermaid documentados; PR #7 integrado.
- [x] Prompts organizados no formato da apostila e revisados pelo aluno; ver [registro](prompts-utilizados.md).

Não há pendências de implementação identificadas no material fornecido, consideradas
as confirmações do aluno. Resta encaminhar os links de entrega pelo canal do curso.
A avaliação e a nota cabem aos professores.

## Concluído — empacotamento da Unidade V

- [x] Listagens com fluxo Controller → Service → Repository.
- [x] Tratamento de falhas de banco durante operação e erros sem JSON na interface.
- [x] Testes de regressão e scripts para Windows/macOS.
- [x] README com participação da IA, lições aprendidas e exemplos curl.
- [x] Roteiro de demonstração com SQLite separado dos dados reais.
- [x] Código e documentação reunidos na versão v1.0.1.

## Evoluções futuras — sem compromisso nesta release

| Item | Observação |
| --- | --- |
| Priorização assistida — Modo 2 | Futura. Definir sugestão com justificativa e confirmação do usuário; planejar IA durante a execução e fallback local por regras sem chave de API. Testar os dois modos antes da entrega da funcionalidade. Sem modelo, endpoint ou chamadas pagas no MVP atual, que adota o Modo 1 de IA como copiloto de desenvolvimento. |
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

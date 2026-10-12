# Conferência de entrega — v1.0.0

Data: 12/10/2026. Referência: 12 capturas da apostila fornecida, em especial
a seção 2.3.4 (capturas 104750 e 104802), e as imagens posteriores de qualidade/testabilidade.
O aluno confirmou que esse material contém todas as exigências aplicáveis.

## Matriz de atendimento

| Critério | Evidência | Resultado |
| --- | --- | --- |
| MVP pequeno e claro, pertinente ao aluno | `docs/escopo-mvp.md`, RF01–RF09 em `docs/requisitos.md` | Atendido |
| Arquitetura mínima, módulos e fluxo de dados | Diagrama Mermaid e descrição em `docs/requisitos.md`; rotas, schemas, serviços e repositório | Atendido |
| Dependências e reprodução | Python 3.14, `requirements.txt`, `requirements-browser.txt`, comandos no README; CI instala ambiente limpo | Atendido |
| Git, .gitignore e histórico incremental | Commits de planejamento, funcionalidades, testes, correções e release; PRs #1–#5 integrados | Atendido |
| Repositório público | https://github.com/ncamilo/SistemaDesIA | Atendido |
| README detalhado | Descrição, instalação, execução, exemplos, tecnologias, assistente/modelo, limitações, próximos passos, créditos e licença | Atendido |
| Testes executáveis e passando | 44 testes unitários/API e quatro de navegador; CI aprovado na versão publicada | Atendido |
| Qualidade: tipagem, modularidade e consistência | Anotações públicas, validação Pydantic e Ruff lint/format no CI | Atendido |
| Healthcheck, CRUD e validação de payload | Testes incluindo startup com banco indisponível, erros HTTP e persistência | Atendido |
| Priorização assistida | Documentada no backlog como evolução futura; dispensa de implementação confirmada pelo aluno | Atendido como planejamento futuro |
| Release/tag | v1.0.0 publicada, notas de release e CHANGELOG | Atendido |
| Aceite final e persistência ao reiniciar | Confirmação explícita do aluno em 12/10/2026; teste de persistência já existente | Confirmado |

## Resultado

Core, qualidade e release concluídos para o escopo acordado e para o material fornecido,
consideradas as confirmações do aluno. Não foi identificada funcionalidade obrigatória
pendente. Resta a submissão pelo canal do curso; avaliação e nota são decisões dos professores.

Core, qualidade e release são etapas rastreáveis, não três tags exigidas pelo material.
As tags publicadas são `v0.1.0` e `v1.0.0`. Não foram criadas marcações retroativas
para simular etapas de desenvolvimento.

## Links para avaliação

- [Código e README](https://github.com/ncamilo/SistemaDesIA)
- [Release v1.0.0](https://github.com/ncamilo/SistemaDesIA/releases/tag/v1.0.0)
- [Histórico](https://github.com/ncamilo/SistemaDesIA/commits/main/)
- [Pull requests integrados](https://github.com/ncamilo/SistemaDesIA/pulls?q=is%3Apr+is%3Amerged)
- [Testes no GitHub Actions](https://github.com/ncamilo/SistemaDesIA/actions)

Este registro de aceite é posterior à publicação da release. Não altera o código
da v1.0.0, sua tag, o banco local ou as notas históricas da versão.

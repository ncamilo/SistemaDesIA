# Conferência de entrega — v1.0.2

Data: 12/10/2026. Referência: 12 capturas da apostila fornecida, em especial
a seção 2.3.4 (capturas 104750 e 104802), as imagens posteriores de qualidade/testabilidade
e as oito capturas da Unidade V fornecidas em Entrega do Sistema.zip.
O aluno confirmou que esse material contém todas as exigências aplicáveis.

## Matriz de atendimento

| Critério | Evidência | Resultado |
| --- | --- | --- |
| MVP pequeno e claro, pertinente ao aluno | `docs/escopo-mvp.md`, RF01–RF09 em `docs/requisitos.md` | Atendido |
| Arquitetura mínima, módulos e fluxo de dados | `docs/arquitetura-componentes.md`, diagrama Mermaid, responsabilidades e fluxo; PR #7 integrado | Atendido |
| Dependências e reprodução | Python 3.11, `requirements.txt`, `requirements-browser.txt`, comandos no README; CI instala ambiente limpo | Atendido |
| Git, .gitignore e histórico incremental | Commits de planejamento, funcionalidades, testes, correções e release; PRs #1–#5 integrados | Atendido |
| Repositório público | https://github.com/ncamilo/SistemaDesIA | Atendido |
| README detalhado | Descrição, instalação, execução, exemplos, tecnologias, assistente/modelo, limitações, próximos passos, créditos e licença | Atendido |
| Testes executáveis e passando | 48 testes unitários/API e de automação e seis de navegador; CI aprovado na versão publicada | Atendido |
| Qualidade: tipagem, modularidade e consistência | Anotações públicas, validação Pydantic e Ruff lint/format no CI | Atendido |
| Healthcheck, CRUD e validação de payload | Testes incluindo startup com banco indisponível, erros HTTP e persistência | Atendido |
| Modos de uso de IA e priorização assistida | Modo 1 adotado: IA como copiloto de desenvolvimento, conforme material fornecido. Modo 2 e fallback local por regras previstos no backlog, sem implementação atual | Modo 1 atendido; Modo 2 como evolução futura |
| Release/tag | Versão de entrega v1.0.2, notas e CHANGELOG; publicação após CI aprovado | Conferir publicação no link da release abaixo |
| Aceite final e persistência ao reiniciar | Confirmação explícita do aluno em 12/10/2026; teste de persistência já existente | Confirmado |
| Registro dos prompts | `docs/prompts-utilizados.md`, revisado pelo aluno no formato da apostila; referências no README e no registro de uso de IA | Documentado |

## Resultado

Core, qualidade e release concluídos para o escopo acordado e para o material fornecido,
consideradas as confirmações do aluno. Não foi identificada funcionalidade obrigatória
pendente. Resta a submissão pelo canal do curso; avaliação e nota são decisões dos professores.

Core, qualidade e release são etapas rastreáveis, não três tags exigidas pelo material.
O histórico de versões inclui `v0.1.0`, `v1.0.0`, `v1.0.1` e a entrega `v1.0.2`. Não foram criadas marcações retroativas
para simular etapas de desenvolvimento.

## Links para avaliação

- [Código e README](https://github.com/ncamilo/SistemaDesIA)
- [Release v1.0.2](https://github.com/ncamilo/SistemaDesIA/releases/tag/v1.0.2)
- [Histórico](https://github.com/ncamilo/SistemaDesIA/commits/main/)
- [Pull requests integrados](https://github.com/ncamilo/SistemaDesIA/pulls?q=is%3Apr+is%3Amerged)
- [Testes no GitHub Actions](https://github.com/ncamilo/SistemaDesIA/actions)

## Conferência da Unidade V

- Scripts Windows e macOS incluídos, com instalação e testes em ambiente limpo no CI.
- README inclui objetivo, instalação, uso, exemplos, limites, participação da IA e lições aprendidas.
- Roteiro em [demonstracao.md](demonstracao.md), com dados fictícios e banco separado.
- A release v1.0.2 reúne código e documentação, incluindo arquitetura e prompts revisados pelo aluno.
- A validação local passou com 48 testes unitários/API e de automação e seis de navegador.
- A revisão de segurança deve considerar o uso local sem autenticação; não representa certificação de segurança.

O aceite do aluno registrado em 12/10/2026 refere-se ao MVP. As correções posteriores
preservam o escopo e o esquema SQLite. O aviso do TestClient permanece como evolução futura.

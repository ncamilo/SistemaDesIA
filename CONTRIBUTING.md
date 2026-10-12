# Fluxo de desenvolvimento

- Manter `main` utilizável; mudanças em branches curtas (`feat/`, `fix/`, `docs/`).
- Vincular cada incremento a um requisito e critério de aceitação.
- Fazer commits pequenos e significativos, em Conventional Commits: `docs`, `chore`, `feat`, `test`, `fix`, `refactor`.
- Não fabricar commits só para atingir quantidade: o histórico deve representar a evolução real.
- Revisar código e testes gerados por IA. Registrar decisões, limitações e resultados de validação.
- Executar os testes relevantes antes de integrar mudanças. Adicionar CI após existir uma suíte executável.
- Não versionar credenciais, bancos locais, manuais privados ou arquivos de referência do curso.
- Criar pull requests com descrição do comportamento, requisitos atendidos e verificações feitas.
- Marcar `v1.0.0` somente após cumprir os critérios de entrega.

## Definição de pronto

Funcionalidade atende aos critérios de aceitação, tem testes relevantes passando e documentação
atualizada. A entrega final acrescenta dependências reproduzíveis, README completo, licença,
histórico consistente e repositório público conforme a apostila.

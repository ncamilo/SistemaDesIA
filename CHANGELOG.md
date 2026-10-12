# Histórico de versões

## v1.0.0 — 12/10/2026

Primeira versão estável do MVP local de projetos e tarefas de montagem.

### Funcionalidades

- Projetos por cliente e referência de pedido; CRUD de tarefas vinculadas.
- Status de execução, filtro, progresso automático e reabertura.
- Persistência SQLite e interface responsiva com navegação por teclado.
- API REST, contratos de entrada/saída, erros e documentação OpenAPI.
- Healthcheck `/health`; falha do banco na inicialização mantém a aplicação acessível
  e retorna 503 nas operações de dados até corrigir o acesso e reiniciar.

### Qualidade e documentação

- 48 testes automatizados: 44 unitários/API e quatro de navegador.
- CI com lint, formatação, testes de API e testes em Chromium.
- Escopo, backlog, arquitetura, contrato HTTP, instruções de execução e licença MIT.

### Limitações

Uso local sem autenticação; não expor diretamente à internet. Sem paginação,
migrações, recuperação automática de banco ou hospedagem da aplicação.
Priorização assistida adiada; sem custos de serviços de IA no MVP.
Aviso conhecido de depreciação do TestClient com HTTPX, sem falha nos testes.
Publicação técnica não equivale à aceitação acadêmica.

### Atualização

Não há alteração de esquema em relação à v0.1.0. Preserve o arquivo local
`montagem.db`, pare o servidor, atualize o código/dependências e inicie novamente.
Código-fonte distribuído pela release não inclui cadastros ou credenciais.

## v0.1.0

Primeiro MVP de projetos e tarefas com interface web, persistência e testes.

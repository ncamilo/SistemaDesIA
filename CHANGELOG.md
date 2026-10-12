# Histórico de versões

## v1.0.2 — 12/10/2026

- Adota Python 3.11 nos scripts, CI, lint e documentação.
- Substitui a sintaxe genérica de Python 3.12+ por TypeVar compatível com 3.11.
- Scripts recusam ambiente virtual de outra versão; README orienta a recriação segura.
- Dependências fixadas mantidas após instalação e validação em Python 3.11.
- SQLite, esquema, cadastros e funcionalidades preservados.
- Validação: 48 testes unitários/API e de automação e seis de navegador; CI em Windows, macOS e Linux.


## v1.0.1 — 12/10/2026

- Listagens passam pelo serviço antes do repositório.
- Falhas SQLAlchemy durante operações retornam 503 em JSON, sem expor SQL ou dados.
- Interface tolera respostas de erro sem JSON.
- 52 testes: 46 unitários/API e seis de navegador, incluindo novas regressões.
- Scripts Windows/macOS para instalar, executar, testar, formatar e demonstrar.
- CI de instalação e testes em Windows, macOS e Linux.
- README final, roteiro de demonstração, arquitetura e prompts incluídos no snapshot.
- SQLite preservado; sem migração de esquema. Manter o arquivo montagem.db ao atualizar.
- Permanecem uso local sem autenticação, IA apenas no desenvolvimento e aviso do TestClient.


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

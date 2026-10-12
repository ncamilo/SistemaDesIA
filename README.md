# Montagem · Projetos e tarefas

Gerenciador simples de pedidos de montagem de clientes, desenvolvido em Python e FastAPI
como miniprojeto de pós-graduação com auxílio de IA.

## Funcionalidades

- Criar, listar, editar e excluir projetos com cliente, título, pedido e descrição.
- Cadastrar, editar e excluir tarefas vinculadas a um projeto.
- Alterar tarefas entre pendente, em andamento e concluída; filtrar por status.
- Calcular automaticamente o progresso e o status do projeto.
- Usar pela interface web ou pela API REST documentada no Swagger UI.
- Persistir os dados em SQLite entre execuções.

Projeto sem tarefas fica pendente com 0%. Todas as tarefas concluídas resultam em 100%.
Reabrir uma tarefa ou adicionar uma etapa pendente recalcula o progresso.
Projetos com tarefas não podem ser excluídos antes da remoção das tarefas.

![Interface com dados fictícios de demonstração](docs/images/desktop.png)

## Executar no Windows (PowerShell)

Pré-requisitos: Python 3.14 e Git. Execute a partir da raiz do projeto.

```powershell
git clone https://github.com/ncamilo/SistemaDesIA.git
cd SistemaDesIA
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Abra http://127.0.0.1:8000 para a interface ou http://127.0.0.1:8000/docs para o Swagger UI.
Para encerrar, pressione Ctrl+C no terminal. Não é necessário ativar o ambiente virtual.

Linux/macOS: use `python3.14 -m venv .venv` e substitua `.venv\Scripts\python.exe`
por `.venv/bin/python` nos comandos seguintes.

O banco `montagem.db` é criado na pasta de execução e ignorado pelo Git.
Não apague esse arquivo para atualizar a aplicação. Para usar outro arquivo SQLite:

```powershell
$env:DATABASE_URL = 'sqlite:///./outro-banco.db'
```

## Automação no Windows e macOS

Com Python 3.14 instalado, após clonar o projeto:

```powershell
# Windows: a política vale apenas para este processo.
powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 install
powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 run
```

```bash
# macOS: Python 3.14 disponível como python3.14.
bash scripts/dev.sh install
bash scripts/dev.sh run
```

Os scripts usam a `.venv` do projeto e funcionam a partir de qualquer pasta.
No macOS, `PYTHON=/caminho/python3.14 bash scripts/dev.sh install` permite indicar
o interpretador. SQLite permanece local, sem instalação de servidor de banco.

| Comando | Resultado |
| --- | --- |
| `install` | Cria ambiente se necessário, instala versões fixadas e confere dependências |
| `run` | Inicia em localhost:8000; Ctrl+C encerra |
| `demo` | Inicia em localhost:8001 com `demo.db`, separado dos cadastros reais |
| `test` | Executa testes unitários e de API |
| `check` | Confere lint, formatação e dependências |
| `format` | Formata código com Ruff |
| `browser-install` | Instala dependências de navegador e Chromium |
| `browser-test` | Executa testes de navegador com banco temporário |

Substitua `run` pelo comando desejado. Não há exclusão automática de bancos.
O CI executa `install`, `check` e `test` em Windows, macOS e Linux.

## Exemplo de uso da API

Com o servidor em execução, em outro terminal PowerShell:

```powershell
$projeto = Invoke-RestMethod 'http://127.0.0.1:8000/api/projects' -Method Post -ContentType 'application/json' -Body '{"title":"Montagem de painel","customer":"Cliente exemplo","order_reference":"PED-001"}'
$tarefa = Invoke-RestMethod "http://127.0.0.1:8000/api/projects/$($projeto.id)/tasks" -Method Post -ContentType 'application/json' -Body '{"title":"Conferir componentes"}'
Invoke-RestMethod "http://127.0.0.1:8000/api/tasks/$($tarefa.id)" -Method Patch -ContentType 'application/json' -Body '{"status":"done"}'
Invoke-RestMethod "http://127.0.0.1:8000/api/projects/$($projeto.id)"
```

O último comando retorna projeto concluído com progresso de 100%.

Equivalente inicial com curl no macOS/Linux:

```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/api/projects -H 'Content-Type: application/json' -d '{"title":"Painel demonstrativo","customer":"Cliente exemplo"}'
curl http://127.0.0.1:8000/api/projects
# Substitua 1 pelo id retornado ao criar o projeto.
curl -X POST http://127.0.0.1:8000/api/projects/1/tasks -H 'Content-Type: application/json' -d '{"title":"Conferir componentes"}'
```

| Método | Rota | Operação |
| --- | --- | --- |
| GET / POST | `/api/projects` | Listar / criar projetos |
| GET / PATCH / DELETE | `/api/projects/{id}` | Consultar / editar / excluir projeto |
| GET / POST | `/api/projects/{id}/tasks` | Listar / criar tarefas |
| PATCH / DELETE | `/api/tasks/{id}` | Editar / excluir tarefa |

Para filtrar, acrescente `?status=pending`, `?status=in_progress` ou `?status=done` à listagem de tarefas.
Erros: 404 para recurso inexistente, 409 para exclusão de projeto com tarefas e 422 para entrada inválida.
PATCH altera somente os campos enviados; campos nulos, desconhecidos e corpo vazio são rejeitados.

## Testes e qualidade

Falhas de banco na inicialização ou durante operações retornam 503 em JSON,
sem expor SQL ou dados. A interface também tolera erros sem JSON.

Healthcheck: `GET /health` retorna `200` com `{"status":"ok"}` e indica que o processo
está respondendo, sem testar o banco. Veja o [contrato HTTP e avaliação das diretrizes](docs/contrato-http.md).

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\ruff.exe check app tests
.\.venv\Scripts\ruff.exe format --check app tests
```

A suíte unitária/API contém 46 casos, cobrindo healthcheck, falha do banco na inicialização, contrato HTTP, cálculo do progresso, CRUD, validação, isolamento entre projetos,
filtros, reabertura, exclusão protegida e persistência após recriar a aplicação.
Cada teste de API usa seu próprio banco temporário. Os testes não alteram o banco de uso.
GitHub Actions executa os mesmos comandos em pushes e pull requests.

Há também seis testes de interação em navegador real, em `browser_tests/`, cobrindo
clique no projeto já selecionado em desktop e celular, seleção pelo teclado, troca de
projeto, limpeza do filtro e mudança automática do status conforme a execução das tarefas.
Também verificam mensagens amigáveis para erros sem JSON.
Eles usam um servidor e banco temporários próprios.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-browser.txt
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe -m pytest browser_tests -q
```

Para usar o Edge instalado no Windows, defina `$env:PLAYWRIGHT_CHANNEL = 'msedge'`
e dispense o comando de instalação do Chromium. O CI executa esses testes em Chromium.

A versão instalada do Starlette emite aviso de depreciação ao utilizar TestClient com HTTPX;
a suíte continua funcional. Uma atualização futura do adaptador de testes poderá remover o aviso.

## Arquitetura e documentos

Diagrama Mermaid e responsabilidades: [arquitetura de componentes](docs/arquitetura-componentes.md).

- `app/api.py`: rotas HTTP e injeção de sessão.
- `app/schemas.py`: contratos e validação de dados.
- `app/services.py`: regras de negócio e cálculo de progresso.
- `app/repositories.py`: consultas e persistência.
- `app/models.py` e `app/database.py`: esquema relacional e configuração SQLite.
- `app/static/`: interface HTML, CSS e JavaScript sem framework.
- `tests/`: testes unitários e de integração.

Veja [escopo do MVP](docs/escopo-mvp.md), [requisitos e arquitetura](docs/requisitos.md), [análise da apostila](docs/analise-apostila.md),
[fluxo de contribuição](CONTRIBUTING.md) e [uso da IA](docs/uso-ia.md).

Conferência final e aceite do aluno: [matriz de atendimento da apostila](docs/conferencia-entrega.md).

Registro da interação com a IA: [prompts utilizados no chat](docs/prompts-utilizados.md).

Tecnologias: Python 3.14, FastAPI, Pydantic, SQLAlchemy, SQLite, Uvicorn, pytest, HTTPX e Ruff.
As versões resolvidas, incluindo dependências transitivas, estão em `requirements.txt`.

## Limitações e próximos passos

MVP destinado a uso local, sem autenticação nem autorização. Não o exponha diretamente à internet.
Não inclui estoque, anexos, responsáveis, prazos, notificações, faturamento ou controle de usuários.
Listagens ainda não têm paginação. O schema é criado na inicialização; mudanças futuras precisam de migrações.
O MVP adota o **Modo 1: IA como copiloto de desenvolvimento**. O **Modo 2**, com
IA durante a execução sugerindo prioridades e fallback local por regras quando
não houver chave de API, permanece como evolução futura. Nenhum desses mecanismos
de sugestão está implementado. Veja os [modos de uso da IA](docs/uso-ia.md).
Não há implantação em serviço de hospedagem.

Versão estável do MVP local: **v1.0.1**. Veja o [backlog](docs/backlog.md) e as
[notas de versão](CHANGELOG.md). A publicação técnica não substitui a revisão
de aceitação do aluno nem a conferência da rubrica acadêmica.
Possíveis evoluções: autenticação, responsáveis e prazos, paginação e migrações com Alembic.

## Como a IA ajudou e o que foi revisado

Codex participou do planejamento, código, testes e documentação. O aluno definiu
o domínio de montagem, o limite do MVP, revisou os prompts e confirmou o aceite.

- **Desafios:** os testes de navegação ajudaram a corrigir foco e rolagem ao clicar
  em um projeto. A revisão do healthcheck identificou dependência indevida do
  banco na inicialização. Na revisão final, uma falha de banco durante a execução
  revelou resposta sem JSON e motivou testes de regressão e mensagem amigável.
- **Decisões:** SQLite reduz configuração; status derivado das tarefas evita
  estados contraditórios; camadas Controller, Service e Repository separam
  HTTP, regras e persistência. As listagens também passam pelo serviço.
- **Produtividade:** a IA auxiliou a produção de código repetitivo, casos de teste
  e documentação. Não houve medição de tempo; não atribuímos percentuais de ganho.
- **Lições aprendidas:** código gerado precisa de revisão humana e testes;
  execução feliz não comprova tratamento de falhas. Prompts claros e pequenos
  critérios verificáveis ajudaram a manter o escopo. IA no desenvolvimento não
  significa que o aplicativo possui um modelo de IA em execução.

Evidências: [registro de IA](docs/uso-ia.md), [prompts](docs/prompts-utilizados.md),
[histórico](https://github.com/ncamilo/SistemaDesIA/commits/main/) e testes no CI.

## Demonstração e entrega

O [roteiro de demonstração](docs/demonstracao.md) apresenta problema, CRUD,
validações, persistência, arquitetura, testes e participação da IA em 5–7 minutos.
Usa dados fictícios em `demo.db`, sem alterar o banco de uso.

Entregar o [repositório](https://github.com/ncamilo/SistemaDesIA) e a
[release v1.0.1](https://github.com/ncamilo/SistemaDesIA/releases/tag/v1.0.1).
Seu snapshot reúne código e documentação finais. Para atualizar, preserve
`montagem.db`, pare o servidor, atualize o código, execute `install` e reinicie.
A versão não altera o esquema SQLite. Não inclui cadastros nem credenciais.

## Créditos e licença

Autor: Nelson Camilo. Desenvolvimento assistido por Codex, com modelo GPT-6.
Base acadêmica: Unidades II e V da apostila fornecida pelo aluno; as capturas ficam fora do repositório.
Código disponibilizado sob [licença MIT](LICENSE). Dependências mantêm suas respectivas licenças.

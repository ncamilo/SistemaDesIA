# Contrato HTTP do MVP

Base local: `http://127.0.0.1:8000`. Corpos de requisição e resposta usam JSON,
exceto respostas 204, que não possuem corpo. Não há autenticação neste MVP local.
O contrato executável e atualizado é [OpenAPI](http://127.0.0.1:8000/openapi.json),
com interface [Swagger UI](http://127.0.0.1:8000/docs).

## Operações

| Método | Rota | Sucesso | Erros previstos |
| --- | --- | --- | --- |
| GET | `/health` | 200, `{"status":"ok"}` | Sem erros de negócio |
| GET | `/api/projects` | 200, lista de projetos | — |
| POST | `/api/projects` | 201, projeto criado | 422 |
| GET | `/api/projects/{id}` | 200, projeto | 404, 422 |
| PATCH | `/api/projects/{id}` | 200, projeto atualizado | 404, 422 |
| DELETE | `/api/projects/{id}` | 204 | 404, 409, 422 |
| GET | `/api/projects/{id}/tasks` | 200, lista de tarefas | 404, 422 |
| POST | `/api/projects/{id}/tasks` | 201, tarefa criada | 404, 422 |
| PATCH | `/api/tasks/{id}` | 200, tarefa atualizada | 404, 422 |
| DELETE | `/api/tasks/{id}` | 204 | 404, 422 |

### Healthcheck

`GET /health` é uma verificação de **liveness**: confirma que a aplicação responde.
Não consulta o banco, não altera dados e não garante disponibilidade das dependências.
O ponto de entrada deste projeto é `app/main.py`, equivalente ao `app.py` mencionado
no roteiro. A rota está registrada nesse módulo; não há um segundo aplicativo.

### Projetos

POST exige `title` e `customer`, textos de 1 a 120 caracteres após remoção de espaços
nas extremidades. `order_reference` aceita até 80 caracteres e `description` até 2000;
ambos são opcionais e assumem texto vazio.

```json
{"title":"Montagem de painel","customer":"Cliente exemplo","order_reference":"PED-01"}
```

Resposta segue `ProjectRead`: campos de cadastro, `id`, `created_at`, `status`,
`total_tasks`, `completed_tasks` e `progress`. Status e progresso são calculados,
não são aceitos como entrada de projeto.

### Tarefas

POST exige `title` com as mesmas regras do projeto; `description` é opcional,
limitada a 2000 caracteres. A nova tarefa começa como `pending`.
Resposta segue `TaskRead`: `id`, `project_id`, `title`, `description`, `status`, `created_at`.

PATCH permite alterar título, descrição e status. Status válidos: `pending`,
`in_progress` e `done`. A listagem aceita o filtro opcional `?status=done`, com
os mesmos três valores. Sem filtro, retorna todas as tarefas daquele projeto.

```json
{"status":"in_progress"}
```

### Validação e erros

- PATCH exige pelo menos um campo; campos omitidos permanecem inalterados.
- Campos desconhecidos e valores nulos são rejeitados.
- IDs de caminho devem ser inteiros. Recurso inexistente retorna 404.
- Projeto com tarefas não pode ser excluído: retorna 409.
- Payload, parâmetro ou filtro inválido retorna 422, sem persistir a alteração.

Erros de negócio usam `ErrorResponse`, com `detail` textual:

```json
{"detail":"Remova as tarefas antes de excluir o projeto."}
```

Erros 422 usam o formato de validação do FastAPI: `detail` é uma lista de erros,
com localização (`loc`), mensagem (`msg`) e tipo (`type`). O esquema correspondente
é `HTTPValidationError` no OpenAPI. Não se deve tratar todo `detail` como texto.

## Aderência às imagens fornecidas

| Critério | Situação e evidência |
| --- | --- |
| Tipagem explícita em funções públicas | Anotações em rotas, serviços, repositório, fábrica e schemas; Ruff verifica presença de anotações. Não substitui um verificador estático completo de tipos. |
| Organização modular mínima | `api.py` contém o router; `schemas.py`, `services.py` e `repositories.py` separam contratos, regras e persistência. |
| Padrão consistente | Ruff lint e formatação executados localmente e no CI. |
| pytest | Suítes unitária/API e de navegador existentes. |
| Healthcheck | Teste de resposta 200, corpo exato, Content-Type e independência da sessão do banco. |
| CRUD básico | Criação, consulta, edição e exclusão de projetos/tarefas; inclui bloqueio de exclusão e recursos inexistentes. |
| Validações de payload | Testes para campos ausentes, vazios, nulos, desconhecidos, limites de tamanho e status inválidos. |
| Resposta de priorização assistida | **Não implementada nem testada.** Não integra o escopo aprovado; confirmar obrigatoriedade no curso antes de definir contrato, regras e critérios de aceitação. |

“Cobertura mínima” na imagem descreve fluxos a testar, sem definir percentual.
Não foi realizada medição percentual de cobertura. A aplicação não pode ser considerada
integralmente aderente à segunda imagem enquanto a aplicabilidade da priorização
assistida não for resolvida. Não há endpoint fictício para representar essa funcionalidade.

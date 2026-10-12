# Roteiro de demonstração e submissão

Duração sugerida: 5 a 7 minutos. Usar somente nomes e pedidos fictícios.

## Preparação

Instalar conforme o README. Iniciar `demo` pelo script do seu sistema:

- Windows: `powershell -ExecutionPolicy Bypass -File scripts/dev.ps1 demo`
- macOS: `bash scripts/dev.sh demo`

Abrir http://127.0.0.1:8001. O modo demo utiliza `demo.db`, separado de
`montagem.db`, e preserva os dados entre execuções. O arquivo é ignorado pelo Git.
Não apague seu banco real para preparar a demonstração. Se já houver dados de uma
demonstração anterior, use outro nome de projeto ou exclua tarefas/projeto pela interface.

## Apresentação

1. **Problema e solução (30 s):** acompanhar etapas de montagem de um pedido de
   cliente. Mostrar o escopo enxuto, uso local e SQLite.
2. **Fluxo principal (2 min):** criar projeto “Painel demonstrativo”, cliente
   “Cliente exemplo”, pedido “DEMO-001”. Criar “Conferir componentes” e “Montar
   painel”. Iniciar uma tarefa: projeto em andamento. Concluir uma: 50%.
   Concluir ambas: 100%. Reabrir uma: projeto volta a andamento. Mostrar filtro.
3. **Validação (1 min):** tentar excluir projeto com tarefas: operação bloqueada.
   Em http://127.0.0.1:8001/docs, executar POST /api/projects com título vazio:
   resposta 422. Consultar /health: 200. Não provocar falhas no banco real.
4. **Persistência (30 s):** parar com Ctrl+C e iniciar novamente `demo`.
   Mostrar que projeto e tarefas continuam cadastrados.
5. **Arquitetura e qualidade (1 min):** mostrar o diagrama, explicar Controller →
   Service → Repository → SQLite, Pydantic e os testes. Abrir o CI aprovado no
   GitHub e o histórico dos PRs. Diferenciar testes de API e de navegador.
6. **IA e revisão humana (1 min):** explicar o Modo 1, mostrar os prompts e a
   revisão do tratamento de erros. Modo 2 e fallback são futuros. Não atribuir
   ganhos numéricos de produtividade sem medição.
7. **Encerramento (30 s):** mostrar README, limitações, licença e release v1.0.2.

## Material a submeter

- Repositório: https://github.com/ncamilo/SistemaDesIA
- Versão final: https://github.com/ncamilo/SistemaDesIA/releases/tag/v1.0.2
- Código e documentação do snapshot: https://github.com/ncamilo/SistemaDesIA/tree/v1.0.2
- Testes e histórico: abas Actions e Pull requests do repositório.

Texto sugerido: “Entrega do MVP de gerenciamento de projetos e tarefas de montagem,
desenvolvido em Python/FastAPI com SQLite e IA como copiloto de desenvolvimento.
A release v1.0.2 reúne código, instruções de instalação, testes, arquitetura,
registro de prompts e roteiro de demonstração. Uso local, sem autenticação e sem
serviços pagos de IA em execução.”

O material fornecido não exige explicitamente vídeo ou slides. Se o canal do curso
solicitar um formato adicional, utilizar este roteiro para a apresentação.

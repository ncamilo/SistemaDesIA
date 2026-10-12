# Correção de navegação do projeto

## Relato e reprodução

O aluno relatou que clicar no nome do projeto não produzia mudança visível.
Na reprodução em 12/10/2026, havia um único projeto já selecionado, com 10 tarefas.
O clique recarregou os detalhes do mesmo projeto, sem erros JavaScript.
Nenhum cadastro do aluno foi alterado durante a investigação.

## Lacuna de verificação

A suíte inicial de 40 casos cobre regras de negócio e integração/API. O teste web
somente verifica entrega de HTML, CSS e JavaScript, sem executar cliques.
O teste exploratório inicial de navegador não foi incorporado à suíte versionada.

## Plano incremental

1. Confirmar se o clique deve mostrar tarefas ou editar cadastro.
2. Adicionar teste de regressão em navegador, com banco temporário isolado.
3. Executar o teste antes da correção e registrar o resultado.
4. Corrigir a interação conforme o comportamento esperado.
5. Executar testes unitários/API e de navegador, incluindo largura de celular.
6. Incluir os testes de navegador no CI, abrir pull request e integrar após validação.

Branch: `fix/navegacao-projeto`. Commits separados para planejamento, teste e correção.
Os testes não utilizarão o banco de dados real do aluno.

## Comportamento adotado

O aluno esclareceu que esperava alterar manualmente o status do projeto no cartão.
Para manter o MVP simples, recomenda-se preservar a regra já definida em RF06: status
derivado das tarefas. A tela agora explica explicitamente essa regra; um teste de navegador
acompanha Pendente → Em andamento → Concluído → Pendente ao executar/reabrir uma tarefa.
Não foi acrescentado um segundo controle de status independente.

Clique no cartão abre/destaca as tarefas; o botão Editar continua alterando o cadastro.
O cartão passa a indicar "Abrir tarefas". Após carregar os dados, o foco e a rolagem
vão ao título dos detalhes do projeto, inclusive quando já estava selecionado.
Ao trocar de projeto, o filtro de status é limpo. Respostas obsoletas não movem o foco.

## Regressão

Antes da correção, os três testes novos falharam na asserção de foco no painel:
desktop (1440 px), celular (390 px) e troca de projeto usando Enter.
Isso confirma a ausência do comportamento adotado; não é falha de persistência.
Os testes são versionados em `browser_tests/` e integram um job próprio no CI.

Após o ajuste de navegação, os 40 testes anteriores e os três novos passaram localmente.
Foi acrescentado ainda o teste do ciclo automático de status após o esclarecimento do aluno.

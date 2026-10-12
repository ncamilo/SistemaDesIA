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

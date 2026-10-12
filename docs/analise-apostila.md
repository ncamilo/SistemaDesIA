# Análise da apostila

## Fonte e alcance

Foram examinadas as 12 imagens do arquivo `Apostila Mini Sistema.zip`, em ordem de horário
(104600 a 104813), referentes à Unidade II: Ideação, Arquitetura Mínima e Git/GitHub para o Projeto.
Não foi fornecida a apostila completa nem uma rubrica de avaliação separada.
Os prompts, comandos e versões apresentados nas capturas são exemplos didáticos.

## Projetos sugeridos na Tabela 2

| Projeto | Escopo descrito | Tecnologias sugeridas no material |
| --- | --- | --- |
| Micro-API de Gerenciamento de Tarefas (To-Do List) | Criar, ler, atualizar e excluir tarefas; possível conclusão e filtro por status; persistência | Python/FastAPI/SQLAlchemy ou Node.js/Express/Prisma/Sequelize; SQLite ou PostgreSQL |
| Chatbot de perguntas e respostas (Retrieval Augmented Generation, RAG) | Responder com base em um documento específico, como PDF ou documentação de produto | Python, LangChain, OpenAI API ou Claude API; Streamlit/Gradio para interface |
| Dashboard de monitoramento de clima | Consumir API meteorológica, mostrar temperatura, umidade e previsão por cidade; possível busca | React/Vue, Tailwind CSS, Fetch API/Axios; exemplo de serviço: OpenWeatherMap |
| Gerador de senhas seguras | Gerar senhas conforme tamanho e inclusão de números, caracteres especiais e letras | Python/Click/Argparse ou JavaScript/Node.js; HTML/CSS para web |

O uso de FastAPI no RAG é uma adaptação à escolha tecnológica do aluno. O material não exige
que todos os projetos tenham IA em execução: ela pode ser usada no processo de desenvolvimento.

## Padrão de trabalho descrito

- MVP com escopo limitado, claro e testável. O texto menciona 30 horas como exemplo de período prático.
- Uso da IA em várias etapas: código, testes, documentação e refatoração.
- Relevância pessoal e familiaridade tecnológica.
- Arquitetura mínima com módulos, dependências e fluxo de dados; diagramas Mermaid/PlantUML são sugeridos.
- Separação entre controller, service e repository aparece como exemplo de arquitetura.
- Git desde o início, `.gitignore` adequado e commits claros no padrão Conventional Commits.

## Submissão final (seção 2.3.4)

| Item | O que o material diz |
| --- | --- |
| Repositório | Público no GitHub, acessível para revisão, sem credenciais expostas |
| Histórico | Consistente; recomenda um mínimo de 5 a 10 commits significativos em Conventional Commits |
| README | Título, descrição, instalação, execução, exemplos, tecnologias e modelos/assistentes de IA utilizados, limitações, próximos passos, créditos e licença |
| Dependências | Arquivo que permita reproduzir o ambiente, por exemplo requirements.txt |
| Testes | Testes unitários ou de integração presentes, executáveis e passando |
| Release/tag | Boa prática recomendada para marcar a versão final, por exemplo v1.0.0 |

O trecho recebido não fixa cobertura mínima, número de testes, TDD obrigatório, frontend obrigatório,
serviço de hospedagem da aplicação nem fornecedor obrigatório de IA.

## Recomendação

Recomenda-se o chatbot RAG aplicado a um manual técnico. A afinidade foi inferida dos projetos
e conversas técnicas visíveis sobre ESP32, CAN, eletrônica e automação; isso não equivale a
uma análise de todo o histórico do aluno.

| Opção | Afinidade estimada | Complexidade relativa | Avaliação |
| --- | --- | --- | --- |
| RAG de manual técnico | Alta | Maior | Mais interessante pelo reaproveitamento em consultas técnicas e pelo estudo de IA |
| API de tarefas de bancada | Alta | Menor | Melhor alternativa para priorizar engenharia de software e previsibilidade da entrega |
| Dashboard meteorológico | Moderada | Intermediária | Permite explorar dados, mas o exemplo enfatiza frontend e uma API externa |
| Gerador de senhas | Menor | Menor | Escopo pequeno e testável, com menor ligação ao contexto técnico observado |

A recomendação depende de manter o RAG restrito a um documento e de dispor de tempo para avaliar
recuperação e respostas. Se o prazo for curto, a API de tarefas é a opção mais segura em escopo.

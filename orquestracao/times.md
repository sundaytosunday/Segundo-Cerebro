# Times de IA — quem faz o quê

Regra de distribuição de carga: **o modelo mais forte pensa, divide e julga; os outros executam.** Não se usa o modelo mais caro para criar um botão de sim ou não. Dividir também reparte os limites de uso entre provedores.

Marque com ✅ o que você assina hoje; a IA orquestradora só delega para quem estiver marcado.

## Papéis

| Papel | O que faz | Quem (padrão) | Assina? |
|---|---|---|---|
| Orquestrador e juiz | Entende o pedido, consulta a memória, divide em tarefas, escolhe quem faz cada uma e revisa tudo antes de entregar. Devolve o que ficou fraco | Claude Fable 5.1 (o mais capaz) ou Opus 5.5 | |
| Executor principal | A parte mais difícil: código central, texto importante, análise | Claude Opus 5.5 (Claude Code) | |
| Executor paralelo | Uma frente independente ao mesmo tempo (ex.: back-end enquanto o outro faz o front-end) | Codex (OpenAI) ou um subagente Claude Sonnet 5.5 | |
| Tarefas com passo a passo claro | Deploy, renomear, formatar, converter, preencher modelo | Claude Haiku 5.5, Sonnet 5.5 ou Gemini (Antigravity) | |
| Navegador | Operar sites sem API (Google Flow, painéis, formulários) | Claude na extensão do Chrome | ✅ |
| Imagem e vídeo | Gerar mídia | Google Flow (Nano Banana, Veo) | ✅ |
| Pesquisa longa | Ler muitas fontes e fazer um relatório | Claude com pesquisa na web ou NotebookLM | |

## Como escolher

1. **Tem passo a passo escrito (uma skill)?** Vai para o modelo mais barato que der conta.
2. **Exige julgamento ou é a parte que, se sair errada, estraga o resto?** Vai para o executor principal.
3. **São partes independentes?** Rodam em paralelo, cada uma com um executor.
4. **Quem revisa nunca é quem fez.** O orquestrador confere contra o critério de aceite da tarefa.
5. **Tarefa pequena não precisa de time.** Abaixo de uns 15 minutos de trabalho, uma IA só resolve.

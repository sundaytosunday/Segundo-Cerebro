# Protocolo de orquestração

Como várias IAs trabalham juntas sem perder o fio. Vale com uma ferramenta de orquestração (Maestri, subagentes do Claude Code, várias abas de terminal) ou à mão, colando entre chats.

## 1. Abrir a tarefa
O orquestrador cria `orquestracao/tarefas/AAAA-MM-DD-<slug>.md` a partir do `_modelo.md`, com:
- o pedido do usuário, palavra por palavra;
- o contexto: só os links para os arquivos da memória e as skills que importam (nunca o conteúdo copiado);
- as frentes de trabalho, cada uma com o executor (de `times.md`), a entrega e o critério de aceite;
- o que é decisão do usuário e precisa de resposta antes de começar.

## 2. Delegar
Cada executor recebe um pedido independente, que funciona sem a conversa anterior:
> Objetivo · arquivos para ler · o que entregar e onde · critério de aceite · o que NÃO fazer.

IAs sem acesso aos arquivos (ChatGPT, Gemini e Claude na web, Claude no Chrome) recebem o contexto exportado por `scripts/exportar_contexto.py`.

## 3. Revisar
O orquestrador confere cada entrega contra o critério de aceite. Se reprovar, devolve ao mesmo executor com o motivo exato. Só entrega ao usuário o que passou.

## 4. Fechar
- Marcar a tarefa como concluída, com o resultado e o tempo gasto.
- Gravar em `decisoes/registro.md` o que foi decidido no caminho.
- Se o mesmo tipo de tarefa já apareceu 3 vezes, propor uma skill (regra dos 3).

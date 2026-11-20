# Segundo cérebro

Um sistema de IA em 4 camadas que vale para todos os seus projetos e todas as suas IAs. Assim você para de explicar quem é, como trabalha e o que já decidiu a cada conversa nova.

| Camada | O que resolve | Onde |
|---|---|---|
| 1. Memória | A IA sabe quem você é | `eu/`, `negocios/`, `pessoas/`, `projetos/`, `marca/`, `conhecimento/`, `decisoes/` |
| 2. Habilidades | A IA sabe como você faz | `skills/` |
| 3. Orquestração | Um time de IAs, não uma só | `orquestracao/` |
| 4. Braços | A IA age nas suas ferramentas | `bracos/ferramentas.md` |

Baseado no vídeo do Felipe Tâmbara ([análise](conhecimento/videos/essa-e-a-stack-perfeita-de-ia-em-2026-so-me-copie-qGGkQORaVzY.md)), adaptado para funcionar com várias IAs e sem guardar segredos.

## Instalar (uma vez, no Mac)

```bash
cd ~                                     # ou onde preferir guardar
git clone https://github.com/sundaytosunday/segundo-cerebro.git
cd segundo-cerebro
bash scripts/instalar.sh
```

O `instalar.sh` liga o segundo cérebro ao Claude Code, ao Codex e ao Gemini CLI **em qualquer pasta** do computador:
- acrescenta uma linha de importação em `~/.claude/CLAUDE.md`, `~/.gemini/GEMINI.md` e `~/.codex/AGENTS.md`;
- cria atalhos das skills em `~/.claude/skills/` e `~/.codex/skills/`.

Ele não apaga nada e faz backup do que muda. Rode de novo sempre que criar uma skill nova.

**Obsidian (opcional):** "Open folder as vault" → escolha a pasta `segundo-cerebro`. Serve só para ver a teia crescer; as IAs leem os arquivos direto.

## Primeiro uso: montar a camada 1

Abra o Claude Code em qualquer pasta e diga:

> Monta meu segundo cérebro.

A skill `segundo-cerebro` faz uma entrevista em blocos curtos (você, negócios, marcas, voz, projetos, pessoas, IAs, preferências) e grava cada resposta no arquivo certo. Leva uns 20 minutos e dá para parar e continuar depois. No fim de cada mudança, a IA faz commit e push, para as outras IAs e as sessões na nuvem enxergarem a memória atualizada.

## Como cada IA usa

| IA | Como lê o segundo cérebro |
|---|---|
| Claude Code (Mac) | Automático, em qualquer pasta, depois do `instalar.sh` |
| Claude Code na nuvem (claude.ai/code, celular) | Adicione o repositório `sundaytosunday/segundo-cerebro` à sessão ou ao ambiente; ele lê o `CLAUDE.md` |
| Codex | Automático depois do `instalar.sh` (`~/.codex/AGENTS.md`) |
| Gemini CLI / Antigravity | `~/.gemini/GEMINI.md`; o Antigravity também lê o `AGENTS.md` de um projeto aberto |
| Cursor, Copilot e outros editores | Leem o `AGENTS.md` quando o segundo cérebro está aberto no workspace |
| ChatGPT, Gemini, claude.ai e Claude no Chrome | `python3 scripts/exportar_contexto.py [arquivos extras]` e cole o texto nas instruções personalizadas, num Projeto ou num Gem |

## Rotina

- **No dia a dia:** fale normalmente. Quando aparecer um fato novo ("fechei com o João", "meu preço agora é R$ X"), a IA anota no lugar certo e avisa em uma linha.
- **Regra dos 3:** fez a mesma coisa 3 vezes? A IA propõe uma skill e não existe a quarta vez.
- **Tarefa grande:** "Faz X usando a divisão de carga". A IA abre uma tarefa em `orquestracao/tarefas/`, divide entre os modelos de `orquestracao/times.md`, revisa e só então entrega.
- **Uma vez por mês:** "Faz a manutenção do segundo cérebro" (juntar duplicatas, pausar projetos parados, procurar segredos).

## Regras

- **Nunca** guardar senhas, tokens, chaves de API ou cartões aqui. `bracos/ferramentas.md` diz onde a credencial mora, nunca o valor.
- Repositório **privado**.
- Projeto mora no projeto: aqui ficam só o resumo, as decisões e o link para o repositório ou a pasta.

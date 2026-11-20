@AGENTS.md

## Específico do Claude

- As skills estão em `.claude/skills/` (um atalho para `skills/`), e o Claude Code as carrega sozinho.
- Para tarefas grandes, siga `orquestracao/protocolo.md`: subagentes para partes independentes, modelo mais barato para tarefas com passo a passo claro e o modelo principal como revisor.
- No Chrome, o Claude da extensão não lê este repositório. Gere o contexto com `python3 scripts/exportar_contexto.py` e cole no início da conversa.

#!/usr/bin/env bash
# Liga o segundo cérebro a todas as IAs de linha de comando deste computador (Mac ou Linux).
# Uso: bash scripts/instalar.sh        (rode de novo quando criar uma skill nova)
# Não apaga nada: só acrescenta uma linha de importação e cria atalhos; o que já existia ganha backup.
set -euo pipefail
CEREBRO="$(cd "$(dirname "$0")/.." && pwd)"
echo "Segundo cérebro em: $CEREBRO"

importar() {  # arquivo, linha
  local arq="$1" linha="$2"
  mkdir -p "$(dirname "$arq")"
  touch "$arq"
  if grep -qF "$linha" "$arq"; then
    echo "  já ligado: $arq"
  else
    cp "$arq" "$arq.bak.$(date +%Y%m%d%H%M%S)"
    printf '\n# Segundo cérebro (todas as conversas, todos os projetos)\n%s\n' "$linha" >> "$arq"
    echo "  ligado: $arq"
  fi
}

echo "1. Memória global"
importar "$HOME/.claude/CLAUDE.md" "@$CEREBRO/AGENTS.md"        # Claude Code
importar "$HOME/.gemini/GEMINI.md" "@$CEREBRO/AGENTS.md"        # Gemini CLI
# O Codex não importa arquivos: o AGENTS.md global aponta para o mapa.
importar "$HOME/.codex/AGENTS.md" "Antes de qualquer tarefa, leia o mapa do segundo cérebro do usuário em $CEREBRO/AGENTS.md e siga-o."

echo "2. Skills globais"
for destino in "$HOME/.claude/skills" "$HOME/.codex/skills"; do
  mkdir -p "$destino"
  for skill in "$CEREBRO"/skills/*/; do
    nome="$(basename "$skill")"
    alvo="$destino/$nome"
    if [ -L "$alvo" ] || [ ! -e "$alvo" ]; then
      ln -sfn "${skill%/}" "$alvo"
      echo "  $alvo"
    else
      echo "  pulado (já existe uma pasta de verdade): $alvo"
    fi
  done
done

echo "Pronto. Abra uma conversa nova em qualquer pasta e pergunte: \"o que você sabe sobre mim?\""

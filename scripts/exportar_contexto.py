#!/usr/bin/env python3
"""Exporta o contexto do segundo cérebro para IAs que não leem arquivos.

Serve para o ChatGPT (instruções personalizadas ou Projetos), os Gems do Gemini, os Projetos do
claude.ai e o Claude na extensão do Chrome. Junta perfil, preferências e voz com os arquivos
que você indicar, num texto só, pronto para colar.

Uso:
  python3 scripts/exportar_contexto.py                       # só você (perfil, preferências, voz)
  python3 scripts/exportar_contexto.py projetos/x.md marca/y.md
  python3 scripts/exportar_contexto.py --curto               # versão enxuta para campos com limite

Saída: exportes/contexto.md (ignorado pelo git) e o texto no terminal.
"""

import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BASE = ["eu/perfil.md", "eu/preferencias.md", "eu/voz.md"]


def limpar(texto, curto):
    # Tira as citações de instrução dos modelos ("> Preenchido por…") e os campos em branco.
    # Campo em branco = só o rótulo, ou o rótulo seguido da dica entre parênteses.
    vazio = re.compile(r"\s*-\s*(\*\*[^*]+:\*\*)?\s*(\([^)]*\))?\s*")
    linhas = [l for l in texto.splitlines()
              if not l.startswith(">") and not vazio.fullmatch(l) and not l.startswith("Cole aqui")]
    texto = re.sub(r"\n{3,}", "\n\n", "\n".join(linhas)).strip()
    # Seções que ficaram sem conteúdo.
    texto = re.sub(r"^##+ [^\n]*\n+(?=##|\Z)", "", texto + "\n", flags=re.M).strip()
    if curto:
        texto = re.sub(r"## Exemplos aprovados.*", "", texto, flags=re.S).strip()
    return texto


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivos", nargs="*", help="arquivos extras do segundo cérebro (projeto, marca, negócio)")
    ap.add_argument("--curto", action="store_true", help="sem exemplos longos, para campos com limite")
    args = ap.parse_args()

    partes = ["# Contexto do usuário (segundo cérebro)",
              "Use isto como memória sobre quem eu sou e como trabalho. Se algo aqui contradizer o que eu "
              "disser na conversa, vale o que eu disser; me avise para eu atualizar o segundo cérebro."]
    for rel in BASE + args.arquivos:
        arq = (RAIZ / rel).resolve()
        if RAIZ not in arq.parents or not arq.is_file():
            sys.exit(f"Arquivo não encontrado no segundo cérebro: {rel}")
        partes += ["", "---", "", limpar(arq.read_text(encoding="utf-8"), args.curto)]

    texto = "\n".join(partes).strip() + "\n"
    destino = RAIZ / "exportes" / "contexto.md"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text(texto, encoding="utf-8")
    print(texto)
    print(f"--- {len(texto):,} caracteres · salvo em {destino.relative_to(RAIZ)}", file=sys.stderr)


if __name__ == "__main__":
    main()

# Segundo cérebro — mapa para qualquer IA

Este repositório é a memória, as habilidades, as regras de orquestração e o registro de ferramentas do usuário. Vale para todos os projetos e todas as IAs (Claude, Codex, Gemini, Antigravity, Cursor e o que vier).

**Todos os caminhos abaixo são relativos à pasta onde este arquivo está**, mesmo quando você estiver trabalhando em outro projeto (o arquivo é importado globalmente). **Leia só o que o pedido precisa.** Este mapa diz onde está cada coisa; não varra as pastas. Responda sempre em português do Brasil.

## As 4 camadas

| Camada | Pergunta que responde | Onde |
|---|---|---|
| 1. Memória | Quem é o usuário e o que ele já decidiu? | `eu/`, `negocios/`, `pessoas/`, `projetos/`, `marca/`, `conhecimento/`, `decisoes/` |
| 2. Habilidades | Como ele faz cada coisa? | `skills/<nome>/SKILL.md` |
| 3. Orquestração | Que IA faz qual parte e quem revisa? | `orquestracao/` |
| 4. Braços | Em que ferramentas a IA pode agir? | `bracos/ferramentas.md` |

## Onde procurar

| Se o pedido envolve… | Leia |
|---|---|
| Escrever em nome do usuário (post, e-mail, proposta, roteiro) | `eu/voz.md` e, se for de uma marca, `marca/<marca>.md` |
| Como ele gosta de trabalhar, formato de resposta, o que evitar | `eu/preferencias.md` |
| Quem é ele, o que faz, objetivos | `eu/perfil.md` |
| Uma empresa, serviço, preço | `negocios/<negocio>.md` |
| Uma pessoa pelo nome (cliente, sócio, fornecedor) | `pessoas/<nome>.md` |
| Um projeto (código, canal, cliente) | `projetos/README.md` → `projetos/<projeto>.md` |
| Cores, fontes, logo, tom de uma marca | `marca/<marca>.md` |
| Algo que já foi estudado (vídeo, artigo, curso) | `conhecimento/README.md` |
| "Já decidimos isso?" | `decisoes/registro.md` |
| Uma tarefa grande, com várias partes | `orquestracao/times.md` e `orquestracao/protocolo.md` |
| Usar uma ferramenta externa (Drive, Gmail, redes sociais, geração de imagem) | `bracos/ferramentas.md` |

## Skills disponíveis

| Skill | Para quê |
|---|---|
| `skills/segundo-cerebro` | Montar a memória (entrevista inicial), capturar fatos novos, aplicar a regra dos 3, manter tudo limpo |
| `skills/aprender-video` | Transformar vídeos do YouTube em processos e guardar em `conhecimento/` |

Uma IA que não carrega skills automaticamente deve abrir o `SKILL.md` da skill certa e seguir o passo a passo.

## Regras que valem sempre

1. **Captura contínua.** Fato novo e durável dito numa conversa (pessoa, preço, preferência, decisão) vai para o arquivo certo na mesma hora, seguindo a skill `segundo-cerebro`. Se não existir arquivo, crie a partir do `_modelo.md` da pasta. Se o fato for ambíguo, pergunte antes de gravar.
2. **Regra dos 3.** Se uma tarefa foi feita à mão 3 vezes, proponha transformá-la em skill. Não existe a quarta vez.
3. **Uma fonte da verdade.** Cada fato mora num lugar só; os outros arquivos apontam para ele com um link.
4. **Nada de segredo aqui.** Senhas, tokens, chaves de API e números de cartão nunca entram neste repositório. `bracos/ferramentas.md` diz onde a credencial mora, nunca o valor.
5. **Datar o que muda.** Decisões e números têm data (`AAAA-MM-DD`).
6. **Projeto mora no projeto.** Código e arquivos de um projeto ficam no repositório dele; aqui fica só o resumo, as decisões e o link.

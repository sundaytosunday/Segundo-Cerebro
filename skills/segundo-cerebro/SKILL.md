---
name: segundo-cerebro
description: Mantém o segundo cérebro do usuário (memória em arquivos de texto, skills, orquestração e ferramentas). Use para montar a memória pela primeira vez ("monta meu segundo cérebro", "entrevista"), sempre que surgir na conversa um fato durável sobre o usuário, um negócio, uma pessoa, um projeto, uma marca ou uma decisão ("fechei com o João", "meu preço agora é", "decidi que"), quando ele corrigir o jeito de trabalhar de uma IA, quando uma tarefa se repetir pela terceira vez, quando pedir para organizar ou limpar a memória, ou para dividir uma tarefa grande entre várias IAs.
---

# Segundo cérebro

A memória sabe quem o usuário é; as skills sabem como ele faz. Esta skill cuida das duas e liga as camadas de orquestração e de ferramentas. O mapa geral está no `AGENTS.md` da raiz.

## 1. Montar pela primeira vez (entrevista)

Quando `eu/perfil.md` estiver vazio ou o usuário pedir para montar:

1. Entreviste em blocos curtos, no máximo 4 perguntas por vez, e grave a cada bloco (não espere o fim):
   - **Você:** nome, o que faz, objetivos de 12 meses, rotina, se trabalha mais pelo computador ou pelo celular → `eu/perfil.md`.
   - **Negócios:** cada empresa ou fonte de renda, serviços, preços, público → `negocios/<negocio>.md`.
   - **Marcas:** cores, fontes, tom, onde estão os arquivos → `marca/<marca>.md`.
   - **Voz:** peça 3 a 5 textos reais dele e extraia o tom, as expressões e o que ele nunca diria → `eu/voz.md`.
   - **Projetos ativos:** onde moram e o próximo passo de cada um → `projetos/<projeto>.md` e o índice `projetos/README.md`.
   - **Pessoas-chave:** sócios, clientes principais → `pessoas/<nome>.md`.
   - **IAs e ferramentas:** o que ele assina e o que já está conectado → marcar em `orquestracao/times.md` e `bracos/ferramentas.md`.
   - **Preferências:** como gosta das respostas, o que irrita, o que nunca fazer → `eu/preferencias.md`.
2. Pode pular o que ele não souber agora; deixe o campo em branco, não invente.
3. No fim, mostre o que ficou gravado em 5 linhas e sugira o primeiro processo candidato a skill.

## 2. Captura contínua (em toda conversa)

Quando aparecer um fato durável:

1. **Classifique:** pessoa, negócio, projeto, marca, preferência, voz ou decisão. Conversa passageira ("hoje estou cansado") não entra.
2. **Procure antes de criar:** veja se já existe o arquivo (nome parecido, apelido). Duplicata é o pior defeito de uma memória.
3. **Ambíguo? Pergunte uma vez**, curto: "Quem é o João? Cliente da Sunday?". Não grave chute.
4. **Grave no lugar certo**, a partir do `_modelo.md` da pasta se o arquivo for novo. Fatos que mudam levam data (`AAAA-MM-DD`).
5. **Decisão** vai para `decisoes/registro.md` (só acrescentar linhas) e, se mudar uma regra, também no arquivo da regra.
6. **Correção de comportamento** ("não faça mais X", "prefiro Y") vai para `eu/preferencias.md` na hora.
7. Diga em uma linha o que foi gravado e onde ("Anotei o João em `pessoas/joao-silva.md`").

Nunca grave senhas, tokens, chaves, números de cartão ou documentos pessoais de terceiros.

## 3. Regra dos 3 (habilidades)

- Ao terminar uma tarefa, pergunte-se: é a terceira vez que este tipo de tarefa aparece (veja `orquestracao/tarefas/` e `decisoes/registro.md`)? Se for, proponha a skill: nome, quando dispara e os passos.
- Com o sim do usuário, crie `skills/<nome>/SKILL.md` com:
  - frontmatter com `name` e uma `description` que diga quando usar, com as frases que ele costuma dizer;
  - o passo a passo;
  - **onde buscar contexto na memória** ("leia `marca/<marca>.md` antes de criar qualquer peça");
  - exemplos aprovados em `skills/<nome>/exemplos/` e as regras do que não fazer.
- Registre a skill na tabela do `AGENTS.md` e lembre o usuário de rodar `bash scripts/instalar.sh` no Mac.
- Se a skill já existe e falhou, corrija a skill, não só o resultado.

## 4. Orquestração (tarefas grandes)

Para uma tarefa com várias partes, siga `orquestracao/protocolo.md`: abra o arquivo da tarefa, divida conforme `orquestracao/times.md`, delegue com pedidos independentes, revise contra o critério de aceite e feche gravando as decisões. Tarefa pequena não precisa de time.

## 5. Braços (ferramentas)

Antes de usar uma ferramenta externa, confira em `bracos/ferramentas.md` o que pode sem perguntar. Ferramenta nova conectada entra na tabela no mesmo dia.

## 6. Manutenção (quando pedir ou uma vez por mês)

- Juntar duplicatas e trocar o texto repetido por links.
- Marcar projetos parados há mais de 60 dias como pausados.
- Conferir se cada skill da pasta está na tabela do `AGENTS.md`.
- Procurar qualquer coisa com cara de segredo e avisar o usuário.
- Mostrar um resumo do que mudou e pedir confirmação antes de apagar qualquer coisa.

## 7. Salvar

Toda mudança na memória termina em commit e push (mensagem curta dizendo o que foi gravado), para as outras IAs e as sessões na nuvem enxergarem.

> O [README](../../README.md) em inglês é a referência; tradução baseada no commit `83b0bc1`.

## Início rápido em 60 segundos

Você precisa do **Python 3.11 ou mais recente** e de um navegador. Não há mais nada a instalar: o Runesmith usa apenas a biblioteca padrão do Python.

### 1. Obtenha o Runesmith

Nesta página, clique em **Code → Download ZIP** e descompacte o arquivo, ou clone o repositório com o Git.

### 2. Inicie o Studio

| Sistema | Como |
|---|---|
| **Windows** | Clique duas vezes em `Runesmith.cmd`. Se o Python não estiver instalado, ele abrirá a página de download; marque "Add python.exe to PATH" no instalador. |
| **macOS** | No Terminal, dentro da pasta do Runesmith: `sh Runesmith.command` |
| **Linux** | Em um terminal, dentro da pasta do Runesmith: `sh runesmith.sh` |

O navegador abre o Runesmith Studio. Ele funciona apenas neste computador, por meio de um link privado. Se o navegador não abrir, copie o link exibido na janela do inicializador. Mantenha essa janela aberta enquanto trabalha. Para parar, feche-a ou pressione <kbd>Ctrl</kbd>+<kbd>C</kbd>.

Os inicializadores abrem a pasta que você usou da última vez ou uma nova pasta `My first project` dentro de `~/Runesmith`. Para trabalhar em uma pasta sua:

- **Windows:** arraste e solte a pasta sobre `Runesmith.cmd`.
- **macOS e Linux:** `sh runesmith.sh path/to/folder`
- **Qualquer sistema, a partir da pasta do Runesmith:** `python -m runesmith up path/to/folder` (`python3` no macOS e no Linux).
- **Instalado:** execute `pip install .` uma vez, em um ambiente virtual se o sistema solicitar. Depois execute `runesmith` em qualquer pasta.

Para iniciar com um clique duplo no macOS ou no Linux, primeiro torne o inicializador executável: `chmod +x Runesmith.command runesmith.sh`.

### 3. Dê um nome ao que você vai criar

Na primeira inicialização, uma breve abertura é exibida e pode ser pulada. Em seguida, o Runesmith pergunta **What will you create?** (O que você vai criar?). Dê um nome ao projeto. A descrição é opcional. Escolha o tipo de trabalho: *Build something new* (Criar algo novo), *Improve my code* (Melhorar meu código), *Tend my documents* (Cuidar dos meus documentos), *Keep an eye on my numbers* (Acompanhar meus números) ou *Just explore* (Apenas explorar). Você pode mudar tudo isso depois.

### 4. Forneça um modelo (Thinking power — Capacidade de raciocínio)

Até você adicionar um modelo, o Runesmith pode mapear e monitorar sua pasta, mas não pode planejar nem construir. Abra **Thinking power** (Capacidade de raciocínio) no menu à esquerda (ou pressione <kbd>6</kbd>) e clique em **Add thinking power** (Adicionar capacidade de raciocínio).

**Uma chave gratuita do Google AI Studio ou da NVIDIA**

1. Em **With a key** (Com uma chave), escolha **Google Gemini** (a modalidade gratuita do Google AI Studio) ou **NVIDIA** (muitos modelos com um endpoint gratuito, entre eles Nemotron e Kimi).
2. Clique em **Get a key** (Obter uma chave). Isso abre [aistudio.google.com/apikey](https://aistudio.google.com/apikey) ou [build.nvidia.com/models](https://build.nvidia.com/models). Crie uma chave e cole-a no Runesmith.
3. Ao colar a chave, o Runesmith pergunta ao provedor quais modelos ele oferece atualmente, preenche um modelo recomendado (para Gemini, o modelo flash mais recente) e oferece alguns outros como botões. Mantenha-o ou digite outro. **List models** (Listar modelos) faz a consulta novamente. Se um provedor responder que um modelo não está mais disponível e indicar seu substituto, o Runesmith o mostrará como um botão; ele nunca faz a troca silenciosamente.
4. Deixe os papéis marcados e clique em **Save and test** (Salvar e testar). Uma chamada rápida confirma que o modelo responde.

Se quiser, adicione ambos. Em **Who does what** (Quem faz o quê), o primeiro modelo de cada papel é o preferido e os demais são alternativas.

Sua chave é salva em um arquivo na pasta `.runesmith` do próprio Runesmith, dentro da pasta do projeto. Ela nunca é exibida novamente e é enviada somente ao provedor ao qual pertence. O arquivo não é criptografado: ele depende das permissões de arquivo da sua conta. A pasta `.runesmith` ignora a si mesma no controle de versão, para não ser incluída em um commit por acidente.

**Um modelo no seu próprio computador (Ollama, LM Studio, llama.cpp)**

- **Ollama:** instale a partir de [ollama.com](https://ollama.com) e execute `ollama pull qwen2.5-coder:7b`.
- **LM Studio:** carregue um modelo com comprimento de contexto de pelo menos 16384 tokens e selecione **Developer: Start Server** (Desenvolvedor: iniciar servidor).
- **llama.cpp:** `llama-server -m model.gguf --ctx-size 16384`

Com um servidor em execução, Thinking power o mostra em **On this computer** (Neste computador). Clique em **Use it** (Usar). É gratuito e privado, e nada sai do seu computador.

**Sem nenhuma chave**

Escolha **A chat window (copy and paste)** (Uma janela de chat, copiar e colar) em **No key needed** (Não precisa de chave). O Runesmith mostra cada solicitação. Você a cola em qualquer modelo de chat ao qual tenha acesso e cola a resposta de volta. Isso serve para papéis que precisam de poucas chamadas, como Checker (Verificador), Improver (Aperfeiçoador) e a elaboração de um plano. Cada chamada espera por você, portanto não é um trabalho autônomo.

**Os papéis.** O **Worker** (Trabalhador) corrige código. O **Planner** (Planejador) elabora planos e os primeiros arquivos e escreve as construções. O **Checker** (Verificador) propõe verificações de aceitação e usa o modelo do Planner, a menos que você escolha outro. O **Improver** (Aperfeiçoador) melhora o próprio Runesmith.

### 5. Planeje e construa

Abra **Goals & plan** (Objetivos e plano) (<kbd>4</kbd>). Escreva um objetivo, adicione um resumo se quiser e clique em **Draft a plan** (Elaborar um plano). Em seguida, use **Draft first files** (Criar os primeiros arquivos) em um marco, ou **Build next step** (Construir a próxima etapa) no cartão Build continuation (Continuação da construção). Os rascunhos aguardam sua leitura em **Work & proposals → Drafts** (Trabalho e propostas → Rascunhos), e nada é gravado nos seus arquivos até você clicar em **Write these files** (Gravar estes arquivos).

Verifique sua configuração a qualquer momento em **Settings → Health** (Configurações → Saúde) ou com `python -m runesmith doctor`. Para corrigir projetos Python existentes e executar a demonstração pela linha de comando, instale também o pytest: `python -m pip install pytest`. O Studio constrói e verifica projetos sem ele.

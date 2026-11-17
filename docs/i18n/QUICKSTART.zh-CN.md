> 英文 [README](../../README.md) 是参考版本；译自提交 `83b0bc1`。

## 60 秒快速入门

你需要 **Python 3.11 或更高版本**和一个网页浏览器。无需安装其他任何东西：Runesmith 只使用 Python 标准库。

### 1. 获取 Runesmith

在此页面点击 **Code → Download ZIP** 并解压，或者使用 Git 克隆仓库。

### 2. 启动 Studio

| 系统 | 方法 |
|---|---|
| **Windows** | 双击 `Runesmith.cmd`。如果没有安装 Python，它会打开下载页面；在安装程序中勾选 "Add python.exe to PATH"。 |
| **macOS** | 在终端中进入 Runesmith 文件夹，运行：`sh Runesmith.command` |
| **Linux** | 在终端中进入 Runesmith 文件夹，运行：`sh runesmith.sh` |

浏览器会打开 Runesmith Studio。它通过私有链接仅在这台计算机上运行。如果浏览器没有打开，请复制启动器窗口中显示的链接。工作时请保持该窗口打开。关闭窗口或按 <kbd>Ctrl</kbd>+<kbd>C</kbd> 即可停止。

启动器会打开上次使用的文件夹，或者打开 `~/Runesmith` 下的新 `My first project` 文件夹。如需在自己的文件夹中工作：

- **Windows：** 将文件夹拖放到 `Runesmith.cmd` 上。
- **macOS 和 Linux：** `sh runesmith.sh path/to/folder`
- **任何系统，从 Runesmith 文件夹运行：** `python -m runesmith up path/to/folder`（macOS 和 Linux 上使用 `python3`）。
- **安装后：** 运行一次 `pip install .`；如果系统要求使用虚拟环境，请在其中运行。然后在任意文件夹中运行 `runesmith`。

如果想在 macOS 或 Linux 上通过双击启动，请先使启动器可执行：`chmod +x Runesmith.command runesmith.sh`。

### 3. 为你要创建的内容命名

首次启动时会播放一段简短的开场，可以跳过。然后 Runesmith 会询问 **What will you create?**（你要创建什么？）为它起个名字。描述是可选的。选择工作类型：*Build something new*（创建新内容）、*Improve my code*（改进我的代码）、*Tend my documents*（整理我的文档）、*Keep an eye on my numbers*（关注我的数字）或 *Just explore*（随便探索）。之后可以更改所有这些设置。

### 4. 为它提供模型（Thinking power，思考能力）

在添加模型之前，Runesmith 可以为你的文件夹建立映射并监视它，但无法规划或构建。在左侧菜单中打开 **Thinking power**（思考能力）（或按 <kbd>6</kbd>），然后点击 **Add thinking power**（添加思考能力）。

**来自 Google AI Studio 或 NVIDIA 的免费密钥**

1. 在 **With a key**（使用密钥）下，选择 **Google Gemini**（Google AI Studio 的免费层级）或 **NVIDIA**（许多模型提供免费端点，包括 Nemotron 和 Kimi）。
2. 点击 **Get a key**（获取密钥）。它会打开 [aistudio.google.com/apikey](https://aistudio.google.com/apikey) 或 [build.nvidia.com/models](https://build.nvidia.com/models)。创建密钥并将其粘贴到 Runesmith 中。
3. 粘贴密钥后，Runesmith 会向提供商查询目前提供哪些模型，然后填入一个推荐模型（Gemini 为最新的 flash 模型），并以按钮形式提供另外几个模型。可以保留它，也可以输入其他模型。**List models**（列出模型）会再次查询。如果提供商回复某个模型不再可用并给出替代模型，Runesmith 会将替代模型显示为一个按钮；它绝不会悄悄切换。
4. 保持角色的勾选状态，然后点击 **Save and test**（保存并测试）。一次简短的调用会确认模型是否响应。

如果愿意，可以两者都添加。在 **Who does what**（各司其职）下，每个角色的第一个模型是首选，其余为备用模型。

你的密钥保存在项目文件夹内 Runesmith 自己的 `.runesmith` 文件夹中的一个文件里。它不会再次显示，并且只会发送给所属的提供商。该文件未加密：它依赖你账户的文件权限。`.runesmith` 文件夹会在版本控制中忽略自身，因此不会被意外提交。

**本机模型（Ollama、LM Studio、llama.cpp）**

- **Ollama：** 从 [ollama.com](https://ollama.com) 安装，然后运行 `ollama pull qwen2.5-coder:7b`。
- **LM Studio：** 加载上下文长度至少为 16384 个 token 的模型，然后选择 **Developer: Start Server**（开发者：启动服务器）。
- **llama.cpp：** `llama-server -m model.gguf --ctx-size 16384`

服务器运行后，Thinking power 会在 **On this computer**（在此计算机上）下显示它。点击 **Use it**（使用它）。免费、私密，任何内容都不会离开你的计算机。

**完全不使用密钥**

在 **No key needed**（无需密钥）下选择 **A chat window (copy and paste)**（聊天窗口，复制粘贴）。Runesmith 会显示每个请求。你将请求粘贴到任何你能使用的聊天模型中，再把回复粘贴回来。这适合只需要少量调用的角色，例如 Checker（检查者）、Improver（改进者），以及起草计划。每次调用都会等待你操作，因此不能无人值守地运行。

**角色。** **Worker**（工作者）修复代码。**Planner**（规划者）起草计划和首批文件并编写构建内容。**Checker**（检查者）提出验收检查，除非你另选模型，否则使用 Planner 的模型。**Improver**（改进者）改进 Runesmith 本身。

### 5. 规划和构建

打开 **Goals & plan**（目标与计划）（<kbd>4</kbd>）。写下一个目标，按需添加简要说明，然后点击 **Draft a plan**（起草计划）。接着在某个里程碑上使用 **Draft first files**（起草首批文件），或在 Build continuation（继续构建）卡片中使用 **Build next step**（构建下一步）。草稿会在 **Work & proposals → Drafts**（工作与提案 → 草稿）中等待你阅读，在你点击 **Write these files**（写入这些文件）之前，不会向你的文件写入任何内容。

随时通过 **Settings → Health**（设置 → 健康状态）或 `python -m runesmith doctor` 检查配置。要修复现有 Python 项目以及运行命令行演示，还需安装 pytest：`python -m pip install pytest`。Studio 无需 pytest 也能构建和检查项目。

> La referencia es el [README en inglés](../../README.md). Traducido desde el commit `83b0bc1` (24 de octubre de 2026).

## Inicio rápido en 60 segundos

Necesitas **Python 3.11 o superior** y un navegador web. No hay nada más que instalar: Runesmith usa solo la biblioteca estándar de Python.

### 1. Consíguelo

En esta página, haz clic en **Code → Download ZIP** (Código → Descargar ZIP) y descomprímelo, o clona el repositorio con Git.

### 2. Inicia el Studio

| Sistema | Cómo |
|---|---|
| **Windows** | Haz doble clic en `Runesmith.cmd`. Si falta Python, se abre la página de descarga; marca "Add python.exe to PATH" en el instalador. |
| **macOS** | En Terminal, en la carpeta de Runesmith: `sh Runesmith.command` |
| **Linux** | En una terminal, en la carpeta de Runesmith: `sh runesmith.sh` |

Tu navegador abre Runesmith Studio. Funciona solo en este equipo, a través de un enlace privado. Si el navegador no se abre, copia el enlace que aparece en la ventana del lanzador. Mantén esa ventana abierta mientras trabajas. Ciérrala, o pulsa <kbd>Ctrl</kbd>+<kbd>C</kbd>, para detenerlo.

Los lanzadores abren la carpeta que usaste la última vez, o una carpeta nueva `My first project` dentro de `~/Runesmith`. Para trabajar en una carpeta propia:

- **Windows:** arrastra la carpeta sobre `Runesmith.cmd`.
- **macOS y Linux:** `sh runesmith.sh path/to/folder`
- **Cualquier sistema, desde la carpeta de Runesmith:** `python -m runesmith up path/to/folder` (`python3` en macOS y Linux).
- **Instalado:** ejecuta `pip install .` una sola vez, dentro de un entorno virtual si tu sistema lo pide. Después ejecuta `runesmith` dentro de cualquier carpeta.

Para hacer doble clic en macOS o Linux, primero haz ejecutable el lanzador: `chmod +x Runesmith.command runesmith.sh`.

### 3. Ponle nombre a lo que construyes

El primer inicio muestra una breve introducción que puedes omitir. Después Runesmith pregunta **What will you create?** (¿Qué vas a crear?). Ponle un nombre. La descripción es opcional. Elige el tipo de trabajo: *Build something new* (Construir algo nuevo), *Improve my code* (Mejorar mi código), *Tend my documents* (Cuidar mis documentos), *Keep an eye on my numbers* (Vigilar mis números) o *Just explore* (Solo explorar). Puedes cambiarlo todo más tarde.

### 4. Dale un modelo (Thinking power, «potencia de razonamiento»)

Hasta que añadas un modelo, Runesmith puede mapear tu carpeta y vigilarla, pero no puede planificar ni construir. Abre **Thinking power** en el menú de la izquierda (o pulsa <kbd>6</kbd>) y haz clic en **Add thinking power** (Añadir potencia de razonamiento).

**Una clave gratuita de Google AI Studio o NVIDIA**

1. En **With a key** (Con una clave), elige **Google Gemini** (el nivel gratuito de Google AI Studio) o **NVIDIA** (muchos modelos con un endpoint gratuito, entre ellos Nemotron y Kimi).
2. Haz clic en **Get a key** (Obtener una clave). Se abre [aistudio.google.com/apikey](https://aistudio.google.com/apikey) o [build.nvidia.com/models](https://build.nvidia.com/models). Crea una clave y pégala en Runesmith.
3. Pega tu clave y Runesmith le pregunta al proveedor qué modelos ofrece hoy; luego rellena uno recomendado (para Gemini, el modelo flash más reciente) y ofrece algunos otros como botones. Conserva ese modelo, o escribe otro. **List models** (Listar modelos) vuelve a preguntar. Si alguna vez un proveedor responde que un modelo ya no está disponible y nombra su reemplazo, Runesmith lo muestra como un botón; nunca cambia de modelo en silencio.
4. Deja marcados los roles y haz clic en **Save and test** (Guardar y probar). Una llamada diminuta confirma que el modelo responde.

Añade ambos si quieres. En **Who does what** (Quién hace qué), el primer modelo de cada rol es el preferido y los demás son de respaldo.

Tu clave se guarda en un archivo dentro de la propia carpeta `.runesmith` de Runesmith, dentro de la carpeta de tu proyecto. No se vuelve a mostrar y solo se envía al proveedor al que pertenece. El archivo no está cifrado: depende de los permisos de archivo de tu cuenta. La carpeta `.runesmith` se ignora a sí misma para el control de versiones, así que no se incluye en un commit por accidente.

**Un modelo en tu propio equipo (Ollama, LM Studio, llama.cpp)**

- **Ollama:** instálalo desde [ollama.com](https://ollama.com), luego `ollama pull qwen2.5-coder:7b`.
- **LM Studio:** carga un modelo con una longitud de contexto de al menos 16384 tokens, luego **Developer: Start Server**.
- **llama.cpp:** `llama-server -m model.gguf --ctx-size 16384`

Con un servidor en marcha, Thinking power lo muestra en **On this computer** (En este equipo). Haz clic en **Use it** (Úsalo). Gratis, privado, y nada sale de tu equipo.

**Sin ninguna clave**

Elige **A chat window (copy and paste)** (Una ventana de chat: copiar y pegar) en **No key needed** (No se necesita clave). Runesmith muestra cada solicitud. Tú la pegas en cualquier modelo de chat al que tengas acceso y pegas la respuesta de vuelta. Sirve para los roles que necesitan solo unas pocas llamadas, como el Checker (Verificador), el Improver (Mejorador) y la redacción de un plan. Cada llamada espera por ti, así que no es un trabajo desatendido.

**Los roles.** El **Worker** (Trabajador) repara código. El **Planner** (Planificador) redacta planes y los primeros archivos, y escribe las construcciones. El **Checker** propone comprobaciones de aceptación y sigue el modelo del Planner a menos que elijas otro. El **Improver** mejora el propio Runesmith.

### 5. Planifica y construye

Abre **Goals & plan** (Objetivos y plan) (<kbd>4</kbd>). Escribe un objetivo, añade un resumen si quieres y haz clic en **Draft a plan** (Redactar un plan). Después usa **Draft first files** (Redactar los primeros archivos) en un hito, o **Build next step** (Construir el siguiente paso) en la tarjeta **Build continuation** (Continuación de la construcción). Los borradores esperan en **Work & proposals → Drafts** (Trabajo y propuestas → Borradores) para que los leas, y no se escribe nada en tus archivos hasta que hagas clic en **Write these files** (Escribir estos archivos).

Comprueba tu configuración en cualquier momento con **Settings → Health** (Ajustes → Salud), o con `python -m runesmith doctor`. Para reparar proyectos de Python existentes, y para ejecutar la demo de línea de comandos, instala también pytest: `python -m pip install pytest`. El Studio construye y comprueba proyectos sin él.
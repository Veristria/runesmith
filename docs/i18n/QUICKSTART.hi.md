# Runesmith — 60 सेकंड में शुरुआत (Quick start in 60 seconds)

> यह अनुवाद मुख्य अंग्रेज़ी README का अनुसरण करता है: [README.md](../../README.md)। यह कमिट `e47c574` से अनूदित है (2026-10-23)। अगर अंग्रेज़ी में कुछ बदला जाए, तो वही सबसे पहले अंग्रेज़ी README में बदलेगा।

आपको **Python 3.11 या नया** और एक वेब ब्राउज़र चाहिए। और कुछ इंस्टॉल करने की ज़रूरत नहीं है: Runesmith केवल Python की स्टैंडर्ड लाइब्रेरी का उपयोग करता है।

### 1. इसे पाएँ (Get it)

इस पेज पर **Code → Download ZIP** पर क्लिक करके उसे unzip करें, या Git से रिपॉज़िटरी clone करें।

### 2. Studio शुरू करें (Start the Studio)

| सिस्टम | कैसे |
|---|---|
| **Windows** | `Runesmith.cmd` पर डबल-क्लिक करें। अगर Python नहीं है, तो वह डाउनलोड पेज खोल देता है; installer में "Add python.exe to PATH" पर टिक करें। |
| **macOS** | Terminal में, Runesmith फ़ोल्डर में: `sh Runesmith.command` |
| **Linux** | टर्मिनल में, Runesmith फ़ोल्डर में: `sh runesmith.sh` |

आपका ब्राउज़र Runesmith Studio खोलता है। यह केवल इसी कंप्यूटर पर चलता है, एक निजी लिंक (private link) से। अगर ब्राउज़र न खुले, तो launcher विंडो में छपे लिंक को कॉपी करें। काम करते समय वह विंडो खुली रखें। रोकने के लिए उसे बंद करें, या <kbd>Ctrl</kbd>+<kbd>C</kbd> दबाएँ।

Launchers पिछली बार इस्तेमाल किए गए फ़ोल्डर को खोलते हैं, या `~/Runesmith` के नीचे एक नया `My first project` फ़ोल्डर बनाते हैं। अपनी पसंद के फ़ोल्डर में काम करने के लिए:

- **Windows:** फ़ोल्डर को `Runesmith.cmd` पर छोड़ दें (drag & drop)।
- **macOS और Linux:** `sh runesmith.sh path/to/folder`
- **कोई भी सिस्टम, Runesmith फ़ोल्डर से:** `python -m runesmith up path/to/folder` (macOS और Linux पर `python3`)।
- **इंस्टॉल करके:** Runesmith फ़ोल्डर में एक बार `pip install .` चलाएँ, ज़रूरत हो तो virtual environment में। फिर किसी भी फ़ोल्डर में `runesmith` चलाएँ।

macOS या Linux पर डबल-क्लिक से चलाने के लिए पहले launcher को executable बनाएँ: `chmod +x Runesmith.command runesmith.sh`।

### 3. बनाने वाली चीज़ को नाम दें (Name what you build)

पहली बार शुरू करने पर एक छोटी सी शुरुआत (opening) चलती है, जिसे आप छोड़ सकते हैं। फिर Runesmith पूछता है: **What will you create?** — आप क्या बनाएँगे? उसे एक नाम दें। विवरण (description) देना ज़रूरी नहीं है। काम की श्रेणी चुनें: *Build something new* (कुछ नया बनाना), *Improve my code* (मेरे कोड को सुधारना), *Tend my documents* (मेरे दस्तावेज़ों की देखभाल), *Keep an eye on my numbers* (मेरे आँकड़ों पर नज़र रखना) या *Just explore* (बस देखना-परखना)। ये सब बाद में बदले जा सकते हैं।

### 4. उसे एक मॉडल दें (Give it a model — Thinking power)

आप जब तक मॉडल नहीं जोड़ते, Runesmith आपका फ़ोल्डर map और निगरानी कर सकता है, पर वह योजना नहीं बना सकता और न बना सकता। बाएँ मेनू में **Thinking power** (सोचने की शक्ति) खोलें (या <kbd>6</kbd> दबाएँ) और **Add thinking power** पर क्लिक करें।

**Google AI Studio या NVIDIA से मुफ़्त key**

1. **With a key** के नीचे **Google Gemini** (Google AI Studio का मुफ़्त टियर) या **NVIDIA** (कई मॉडल एक मुफ़्त endpoint पर, उनमें Nemotron और Kimi भी) चुनें।
2. **Get a key** पर क्लिक करें। इससे [aistudio.google.com/apikey](https://aistudio.google.com/apikey) या [build.nvidia.com/models](https://build.nvidia.com/models) खुलता है। Key बनाकर Runesmith में paste करें।
3. Key paste करने पर Runesmith पूछता है कि आज वह provider कौन से मॉडल देता है, फिर एक सुझाया मॉडल भर देता है (Gemini के लिए सबसे नया flash मॉडल) और कुछ और बटनों के रूप में offer करता है। उसे रहने दें, या कोई और टाइप करें। **List models** दोबारा पूछता है। अगर कोई provider कभी कहे कि कोई मॉडल अब उपलब्ध नहीं है और उसका विकल्प बता दे, तो Runesmith उसे एक बटन के रूप में दिखाता है; वह चुपचाप बदलता नहीं।
4. Roles के टिक वैसे ही रहने दें और **Save and test** पर क्लिक करें। एक छोटी call से पक्का हो जाता है कि मॉडल उत्तर देता है।

दोनों जोड़ सकते हैं। **Who does what** (कौन क्या करे) में हर role का पहला मॉडल पसंदीदा होता है और बाकी विकल्प (fallback) हैं।

आपकी key आपके project फ़ोल्डर के अंदर Runesmith के अपने `.runesmith` फ़ोल्डर में एक फ़ाइल में सहेजी जाती है। वह दोबारा कभी नहीं दिखती, और केवल उसी provider को भेजी जाती है जिसकी है। वह फ़ाइल encrypted नहीं है: वह आपके अकाउंट की फ़ाइल permissions पर भरोसा करती है। `.runesmith` फ़ोल्डर version control में अपने आप ignore हो जाता है, इसलिए ग़लती से commit नहीं होता।

**अपने ही कंप्यूटर पर मॉडल (Ollama, LM Studio, llama.cpp)**

- **Ollama:** [ollama.com](https://ollama.com) से इंस्टॉल करें, फिर `ollama pull qwen2.5-coder:7b`।
- **LM Studio:** कम से कम 16384 tokens के context length वाला मॉडल load करें, फिर **Developer: Start Server**।
- **llama.cpp:** `llama-server -m model.gguf --ctx-size 16384`

Server चालू होने पर Thinking power उसे **On this computer** के नीचे दिखाता है। **Use it** पर क्लिक करें। मुफ़्त, निजी, और आपके कंप्यूटर से बाहर कुछ नहीं जाता।

**बिलकुल key के बिना**

**No key needed** के नीचे **A chat window (copy and paste)** चुनें। Runesmith हर request दिखाता है। आप उसे किसी भी चैट मॉडल में paste करें और उत्तर वापस paste कर दें। यह उन roles के लिए ठीक है जिन्हें बस कुछ ही calls चाहिए, जैसे Checker, Improver और एक योजना (plan) लिखवाना। हर call आपका इंतज़ार करती है, इसलिए यह बिना देखे चलने वाला काम नहीं है।

**Roles — कौन क्या करता है।** **Worker** कोड की मरम्मत करता है। **Planner** योजनाएँ और पहली फ़ाइलों को लिखता है और builds लिखवाता है। **Checker** acceptance checks सुझाता है और आप कुछ और न चुनें तो Planner का मॉडल ही चलाता है। **Improver** Runesmith को खुद सुधारता है।

### 5. योजना बनाएँ और बनाएँ (Plan and build)

**Goals & plan** (<kbd>4</kbd>) खोलें। एक लक्ष्य (goal) लिखें, चाहें तो संक्षिप्त जानकारी (brief) जोड़ें, और **Draft a plan** पर क्लिक करें। फिर किसी milestone पर **Draft first files** इस्तेमाल करें, या Build continuation कार्ड में **Build next step**। Drafts पढ़ने के लिए **Work & proposals → Drafts** में इंतज़ार करते हैं, और आप **Write these files** पर क्लिक करने तक आपकी फ़ाइलों में कुछ नहीं लिखा जाता।

अपनी सेटअप कभी भी जाँचें: **Settings → Health**, या `python -m runesmith doctor`। मौजूदा Python projects की मरम्मत के लिए, और command-line demo चलाने के लिए, pytest भी इंस्टॉल करें: `python -m pip install pytest`। Studio pytest के बिना भी projects बनाता और जाँचता है।

---

अंग्रेज़ी में आगे के विवरण के लिए [README.md](../../README.md) देखें।

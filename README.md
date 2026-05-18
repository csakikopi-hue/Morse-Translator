📡 Morse — Signal Translator

A **premium, minimalistic**, and highly intuitive web application designed to bridge the gap between traditional telegraphy and modern digital text. Featuring a **real-time translation** engine, **dynamic multi-language** localization, an active **audio synthesizer**, and an interactive **spacebar rhythm interpreter**.

---

## ✨ Features

### 🔄 Dual-Mode Conversion
* **Text** ➔ Morse Code: Instantly encodes standard text into standardized dots (`·`) and dashes (`–`).
* **Morse** Code ➔ Text: Decodes Morse signals back into legible text. Supports forward slashes (`/`) to seamlessly separate words.

### ⚡ Real-Time Processing
* No submit buttons or page reloads required. The optimized translation pipeline evaluates and parses your input on the fly as you type.

### 🔊 Audio Playback Engine
* Synthesizes perfectly timed, clean sine wave audio frequencies ($620\text{ Hz}$) using the native browser **Web Audio API.
* Features a dynamic CSS audio waveform visualizer that animates perfectly in sync with the auditory signals.

### ⌨️ Interactive Spacebar and Mouse Tap Interpreter
* Rhythm Detection: Switch to Morse mode and turn your spacebar into a virtual telegraph key!
* Smart Gaps: A short tap ($< 200\text{ ms}$) registers a **dot** (`·`).
  * A longer hold ($\ge 200\text{ ms}$) registers a **dash** (`–`).
  * Pausing for $750\text{ ms}$ automatically inserts a character gap space.
* Features a live oscillator that generates real-time audio feedback *while* you press down on the key.
* Click the **button . or -** in **Morse->Text** to type with the Mouse

### 🌍 Dynamic Localization & Character Mapping
* **On-the-Fly Translation:** Switch the entire interface language instantly between **English**, **German**, **Hungarian**, .**Spanish**, **French**, **Chienese**
* **Extended Character Sets:** Correctly handles regional character mappings (e.g., `Á` ➔ `.--.-` and `É` ➔ `..-..`).

### 🌙 Dynamic Luxury UI & Themes
* Designed with a modern, high-contrast palette, fluid micro-interactions, soft radial ambient glows, and responsive layouts.
* Implements seamless **Dark Mode** and **Light Mode** styling with manual toggle overrides and automatic system preference tracking.

### 💾 Utility & Production Tools
* **One-Click Clipboard Actions:** Quick buttons to instantly paste input text, copy input text, or copy generated results.
* **Result File Export:** Download translations directly as tailored `.txt` files with context-aware, localized naming conventions based on the active language.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3 (Modern CSS Variables, Flexbox/Grid, Keyframe Animations)
* **Scripting & Logic:** JavaScript (ES6+, LocalStorage, Web Audio API Pipeline)
* **Typography:** Google Fonts (*DM Sans, DM Mono, Playfair Display*)

---

## 🚀 Quick Start

Since this application is fully self-contained within a single client-side architecture, **no server setup or complex backend configuration is required**. You can launch it directly on any modern machine.

### Prerequisites
* A modern web browser (Google Chrome, Mozilla Firefox, Microsoft Edge, or Apple Safari) with Web Audio API support enabled.

<img width="1280" height="857" alt="Morse — Signal Translator - Google Chrome 2026  05  17  19_42_37" src="https://github.com/user-attachments/assets/daf175f5-3f45-4574-974b-aea71ea4371e" />
<img width="1280" height="854" alt="Morse — Signal Translator - Google Chrome 2026  05  17  19_42_47" src="https://github.com/user-attachments/assets/c16d6b4d-bb41-4262-9124-efb437d151f9" />
<img width="1259" height="860" alt="Google Gemini - Google Chrome 2026  05  18  15_40_03" src="https://github.com/user-attachments/assets/b26759bb-9694-4cd3-9330-34f3e25ed6aa" />
<img width="1264" height="857" alt="Google Gemini - Google Chrome 2026  05  18  15_40_10" src="https://github.com/user-attachments/assets/aeee0ba2-f61e-490f-af32-9867c3f1fab5" />



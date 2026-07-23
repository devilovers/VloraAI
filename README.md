<div align="center">

# Vlora AI

An intelligent Windows voice assistant tailored for Indonesian spoken commands, integrated with background global hotkey support.

<p>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white">
  <img src="https://img.shields.io/badge/Speech-Google_Speech-EA4335?style=for-the-badge&logo=google&logoColor=white">
  <img src="https://img.shields.io/badge/TTS-gTTS-FF9900?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-00C853?style=for-the-badge">
</p>

</div>

---

## Overview

Vlora AI is a personal voice assistant designed specifically to understand Indonesian phonetic speech patterns and local slang pronunciations. Built to run seamlessly on Windows, it allows users to trigger system actions, open web applications, and launch desktop software instantly using a global hotkey shortcut without leaving active windows or opening a terminal manually.

---

## Features

* **Indonesian Speech Recognition:** Native support for `id-ID` with custom phonetic matching for local accents.
* **Global Hotkey Activation:** Trigger the assistant anytime using `Ctrl + Alt + V`.
* **Silent Background Execution:** Automatically listens in the background via VBScript without popup terminal windows.
* **App & Site Launcher:** Fast command mapping for Spotify, VS Code, Discord, YouTube, Gemini, and more.
* **Natural Voice Feedback:** High-quality Indonesian Text-to-Speech response system.

---

## Technologies

| Technology | Description |
| ------------ | ---------------------------------------- |
| Python 3.11+ | Core programming language |
| SpeechRecognition | Speech-to-text integration using Google Speech API |
| gTTS & Pygame | Natural Indonesian voice feedback and audio playback |
| Keyboard | Low-level global hotkey listener for Windows |
| VBScript | Silent background launcher execution |

---

## Setup & Installation

Follow these steps to set up Vlora AI on your local machine from scratch.

### Prerequisites

* Windows OS
* Python 3.11 or higher installed
* Git installed

### 1. Clone Repository

Open Command Prompt (CMD) and run:

```bash
git clone https://github.com/devilovers/VloraAI.git
cd VloraAI
```

### 2. Install Dependencies

Install all required Python libraries:

```bash
pip install speechrecognition gtts pygame keyboard
```

---

## Usage Guide

### Running Vlora Manually

You can start the hotkey listener manually using Command Prompt:

```bash
python launcher.py
```

Press **`Ctrl` + `Alt` + `V`** anywhere on your system to activate Vlora, then speak your command (e.g., *"Halo Vlora, buka YouTube"*).

---

### Setting Up Automatic Silent Startup (Optional)

To make Vlora run automatically in the background when Windows boots up without opening any terminal windows:

1. Create a file named **`start_silent.vbs`** in your project folder with the following content:

   ```vbs
   Set WshShell = CreateObject("WScript.Shell")
   Set fso = CreateObject("Scripting.FileSystemObject")
   currentDir = fso.GetAbsolutePathName(".")
   WshShell.Run "cmd /c cd /d " & Chr(34) & currentDir & Chr(34) & " && python launcher.py", 0, False
   ```

2. Press **`Win` + `R`**, type `shell:startup`, and press **Enter**.
3. Copy your `start_silent.vbs` file and paste it as a **Shortcut** into the Startup folder.

---

## Author

<p>
<strong>Nur Islami Sabila</strong><br>
Informatics Engineering Student from Indonesia.
</p>

<blockquote>
Learning by building, growing by creating.
</blockquote>

<p align="left">
If you found this project helpful, consider giving it a ⭐ to support the repository.
</p>

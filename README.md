# 🤖 FRIDAY – AI Voice Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Voice Recognition](https://img.shields.io/badge/Speech-Recognition-green)
![OpenAI](https://img.shields.io/badge/AI-Integrated-black)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

📸 **Instagram:** [https://www.instagram.com/mohhitaggarwal](https://www.instagram.com/mohhitaggarwal)  
💼 **LinkedIn:** [https://www.linkedin.com/in/mohitaggarwalofficial](https://www.linkedin.com/in/mohitaggarwalofficial)

> **FRIDAY (Female Replacement Intelligent Digital Assistant Youth)**
> A Python-based personal AI voice assistant inspired by Alexa & Google Assistant.

FRIDAY can listen, speak, automate tasks, search the web, send WhatsApp messages, execute system commands, and even process AI-powered responses.

---

# 🚀 Project Overview

FRIDAY is a **voice-controlled automation assistant** built using Python.
It integrates:

* 🎤 Speech Recognition
* 🔊 Text-to-Speech
* 🌐 Web Automation
* 💻 System Commands
* 📱 WhatsApp Integration
* 🧠 AI Processing (OpenAI Ready)
* 🗄 SQLite Contact Database

It is designed as a **desktop virtual assistant** capable of performing real-world automation tasks.

---

# 🧠 Core Features

## 🎤 Voice Command Recognition

* Listens using `speech_recognition`
* Converts speech → text
* Responds using `pyttsx3`

---

## 🌐 Web & Search Automation

* Google Search
* YouTube Search
* Wikipedia Search
* Open common websites

---

## 💻 System Control

* Shutdown
* Restart
* Sleep
* Minimize all windows
* Launch apps (VS Code, Word, etc.)

---

## 📱 WhatsApp Automation

* Send messages
* Make calls
* Start video calls
* Fetch contacts from SQLite database

---

## 🎵 Mood-Based Music

* Sad songs
* Love songs
* Rage songs
* Party songs

---

## 🧮 Mathematical Calculations

* Performs basic arithmetic via voice command

---

## 🚕 Cab Booking Simulation

* Simulated booking flow using voice prompts

---

## 🧠 AI Command Processing

* Handles complex or unrecognized commands
* Uses OpenAI API (optional integration)

---

# 🖼️ Code Structure Preview

---

## 📦 requirements.txt

![Requirements File](https://raw.githubusercontent.com/MohitAggarwal1/readme_images/refs/heads/main/friday/Screenshot%202026-02-15%20150748.png)

Includes major dependencies:

* pyttsx3
* speech_recognition
* pyautogui
* openai
* sqlite3
* subprocess

---

## 🎤 takeCommand() – Voice Input Engine

![takeCommand Function](https://raw.githubusercontent.com/MohitAggarwal1/readme_images/refs/heads/main/friday/Screenshot%202026-02-15%20151050.png)

Handles:

* Microphone input
* Noise adjustment
* Speech recognition
* Error handling
* Returns processed query text

---

## 📱 whatsApp() – Messaging & Calling System

![WhatsApp Function](https://raw.githubusercontent.com/MohitAggarwal1/readme_images/refs/heads/main/friday/Screenshot%202026-02-15%20150924.png)

Features:

* Fetch contact from SQLite database
* Send WhatsApp message
* Initiate call
* Start video call
* Automated browser redirection

---

## 🧠 aiProcess() – AI Command Processor

![AI Process Function](https://raw.githubusercontent.com/MohitAggarwal1/readme_images/refs/heads/main/friday/Screenshot%202026-02-15%20151009.png)

Handles:

* Complex prompts
* OpenAI API integration
* Smart fallback response system
* Extensible for advanced AI tasks

---

# 🛠️ Tech Stack

* **Python 3.x**
* `pyttsx3` – Text-to-Speech
* `speech_recognition` – Voice Input
* `pyautogui` – System Automation
* `subprocess` – Shell Execution
* `sqlite3` – Contact Database
* `OpenAI API` – AI Processing
* `webbrowser` – URL Handling

---

# ⚙️ Setup Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/MohitAggarwal1/friday.git
cd friday
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Setup SQLite Database

Create a database named:

```
friday.db
```

Create table:

```sql
CREATE TABLE contacts (
    name TEXT,
    mobile_no TEXT
);
```

Add contacts for WhatsApp integration.

---

## 4️⃣ (Optional) Add OpenAI API Key

Inside `aiProcess()` function:

```python
openai.api_key = "your_api_key_here"
```

---

# ▶️ Usage

Run the assistant:

```bash
python friday.py
```

FRIDAY will:

1. Greet you based on time
2. Wait for your voice command
3. Execute the requested task

---

# 🗂️ Project Structure

```
friday-assistant/
│
├── friday.py
├── requirements.txt
├── friday.db
├── module.py
└── README.md
```

---

# 🎯 Example Voice Commands

* "Hello"
* "Search Python on Google"
* "Open YouTube"
* "Shutdown the system"
* "Send message to Harshit"
* "Call Divya"
* "Play love songs"
* "Calculate 25 plus 30"
* "Book a cab"

---

# 🔥 Highlights

* Modular function design
* Error handling included
* Database-driven contact system
* AI extensibility
* Real-world automation capabilities
* Beginner-friendly architecture
* Expandable to full AI desktop assistant

---

# 📌 Future Enhancements

* GUI interface (Tkinter / PyQt)
* Wake word detection
* Offline NLP processing
* Multi-language support
* Real-time AI streaming responses
* Email automation
* Smart home integration

---

# 📄 License

Licensed under **MIT License** — Free to use, modify, and distribute.

---

# 🙌 Why This Project Matters

FRIDAY demonstrates:

* Voice automation engineering
* Python system-level scripting
* AI API integration
* Database-driven logic
* Real-world assistant architecture

It’s not just a project — it’s a foundation for building your own AI ecosystem.

---

### ⭐ If you like this project, consider giving it a star!

---

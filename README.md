# FRIDAY - README

FRIDAY (Female Replacement Intelligent Digital Assistant Youth) is a personal virtual assistant designed to perform various tasks based on voice commands. Inspired by virtual assistants like Alexa and Google Assistant, FRIDAY automates tasks like web searches, file operations, messaging, and more, using Python libraries.

---

## Features

1. **Voice Commands**:
   - Accepts voice commands using speech recognition to execute tasks.
   - Responds with voice feedback through `pyttsx3`.

2. **Greeting**:
   - Wishes the user based on the time of day (morning, afternoon, evening).

3. **General Assistance**:
   - Provides responses to basic greetings and inquiries.
   - Searches on Wikipedia, Google, and YouTube.

4. **Automated Actions**:
   - Opens common websites (YouTube, Google, LinkedIn, etc.).
   - Launches desktop applications like VS Code, Microsoft Word, and more.

5. **System Control**:
   - Automates system actions like shutdown, restart, sleep, and window management.
   
6. **Music and Video Control**:
   - Opens specified YouTube playlists based on mood (e.g., sad, love, rage, party).

7. **Time and Date Information**:
   - Tells the current time and date upon request.

8. **WhatsApp Messaging and Calling**:
   - Uses WhatsApp to send messages, make calls, and initiate video calls based on contact names in a database.
   
9. **Cab Booking Simulation**:
   - Simulates a cab booking process based on user-provided pickup and drop-off locations.

10. **Mathematical Calculations**:
    - Performs basic calculations on command.

11. **AI-Powered Responses**:
    - Uses OpenAI to process complex commands not handled by other functions (currently commented out).

---

## Setup

### Prerequisites

- Python 3.x
- Required Libraries:
  - `pyttsx3`: Text-to-speech library
  - `speech_recognition`: For voice input
  - `pyautogui`: For controlling mouse and keyboard
  - `openai`: For AI-powered command processing
  - `subprocess`: For executing shell commands
  - `sqlite3`: For contact management in a local database (`friday.db`)

### Installation

1. **Clone the Repository**:
   
   git clone <repository-url>
   cd friday-assistant
   

2. **Install Dependencies**:
   
    pip install -r requirements.txt

3. **Database Setup**:
   - Create an SQLite database `friday.db`.
   - Add a `contacts` table with a `name` and `mobile_no` field.

4. **OpenAI API Key**:
   - Add your OpenAI API key in the `aiProcess` function for AI responses (optional).

---

## Usage

1. **Run the Script**:
   
   python friday.py
   

2. **Interact**:
   - FRIDAY will greet you and wait for commands.
   - Common commands include:
     - **Greeting**: "Hello", "Thank you", "Who are you?"
     - **Web Search**: "Search on YouTube/Google", "Wikipedia <topic>"
     - **System Commands**: "Shutdown", "Restart", "Minimize all windows"
     - **Music**: "Play sad/love/rage/party song"
     - **Cab Booking**: "Book a cab"
     - **WhatsApp**: "Send a message to <name>", "Call <name>"
     - **Calculations**: "Calculate 5 + 3"

---

## File Overview

- **Main Script**: Initializes the assistant, configures the voice engine, and sets up the command processing loop.
- **Functions**:
  - `speak()`: Text-to-speech.
  - `wishMe()`: Greeting.
  - `takeCommand()`: Listens for voice commands.
  - `search_google()`, `search_youtube()`: Web search.
  - `click()`, `shutDown()`, `restart()`, `Sleep()`: System control.
  - `remove_words()`: Filters unnecessary words from a command.
  - `findContact()`: Searches contact info in `friday.db`.
  - `whatsApp()`: Sends WhatsApp messages or calls.
  - `book_cab()`, `friday_book_cab()`: Simulates cab booking.
  - `aiProcess()`: AI command processing (optional).

# importing module

from module import *


# voice and engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

con =  sqlite3.connect('friday.db')
cur = con.cursor()


# all functions

# function to speak

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function to wish

def wishMe():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        speak("Good Morning Boss!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss!")

    else:
        speak("Good Evening Boss!")
    speak("Boss How may i help you")

# function to take command

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query

# function to write in file

def search_google(query):
    kit.search(query)

# function to write in file

def search_youtube(video):
    kit.playonyt(video)

# function to operate click by pyautogui

def click():
    pyautogui.click()

#  function to shutdown the system

def desktop():
    pyautogui.keyDown('win')
    pyautogui.press('d')
    pyautogui.keyUp('win')

def shutDown():
    speak(f'Ok boss   ')
    desktop()
    speak('Initializing shutdown protocol ')
    click()

    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')

    sleep(3)
    pyautogui.press('enter')

#  function to restart the system

def restart():
    speak("Ok boss    ")
    desktop()
    speak("Restarting your computer")
    click()

    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')

    sleep(3)
    pyautogui.press('r')
    pyautogui.press('enter')

#  function to lock the system

def Sleep():
    speak('Ok boss')
    desktop()
    speak("Initializing sleep mode")

    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')

    sleep(3)
    pyautogui.press('s')
    pyautogui.press('s')
    pyautogui.press('s')
    pyautogui.press('enter')

# function to remove unwanted words
    
def remove_words(input_string, words_to_remove):
    words = input_string.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    result_string = ' '.join(filtered_words)

    return result_string

# function to find contact from database
 
def findContact(query):
    words_to_remove = [ 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cur.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cur.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query

    except:
        speak('not exist in contacts')

        return 0, 0

#  function to send message and call using whatsapp

def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        friday_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        friday_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        friday_message = "staring video call with "+name
    encoded_message = quote(message)
    print(encoded_message)

    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    full_command = f'start "" "{whatsapp_url}"'

    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(friday_message)

# Simulating a cab service

def book_cab(pickup_location, dropoff_location):
    speak(f"Booking a cab from {pickup_location} to {dropoff_location}...")
    time.sleep(2)  
    speak("Cab booked successfully! Your driver will arrive shortly.")
    return True

# FRIDAY's function to handle cab booking

def friday_book_cab():
    speak("Boss Please provide the pickup location.")
    pickup_location = takeCommand()

    if pickup_location is None:
        return

    speak("and what's the dropoff location.")
    dropoff_location = takeCommand()

    if dropoff_location is None:
        return

    if book_cab(pickup_location, dropoff_location):
        speak("I've successfully booked a cab for you.")

    else:
        speak("Sorry, there was an issue booking the cab.")

#   function to search using AI

def aiProcess(command):
    client = openai(api_key="<Your Key Here>",)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named FRIDAY skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
        ])

    return completion.choices[0].message.content


# speak functions

if __name__ ==  '__main__':
    wishMe()

    while True:
        query = takeCommand().lower()

# general 

        if 'hello' in query or 'friday' in query:
            speak("hello Boss")

        elif "thankyou" in query or "thanks" in query or "thank you" in query:
            speak("No need boss. It's my pleasure")

        elif "hu r u" in query or "who are you" in query:
            speak("I am Female Replacement Intelligent Digital Assistant Youth or. you can call me FRIDAY, and I am here to assist you with various tasks!")

# to search on wikipedia

        elif "wikipedia" in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")

            result = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia, ")
            print(result)
            speak(result) 

# to search any website

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening Youtube")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "open chat" in query:
            webbrowser.open("https://www.chatgpt.com")
            speak("Opening Chat GPT")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com")
            speak("Opening Whatsapp")

        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("Opening G-Mail")

        elif 'open maps' in query or 'show my location' in query:
            webbrowser.open("https://www.google.com/maps/@28.6182658,77.0449321,15z?entry=ttu&g_ep=EgoyMDI0MDkxMS4wIKXMDSoASAFQAw%3D%3D")
            speak("Opening Maps")

        elif 'open canva' in query:
            webbrowser.open("https://www.canva.com")
            speak("Opening Canva")

        elif "open github" in query:
            webbrowser.open("https://www.github.com")
            speak("Opening Github")

        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com")
            speak("Opening Linkedin")    

        elif "open my portfolio" in query:
            webbrowser.open("file:///C://Users//manmo//OneDrive//Desktop//Coding%20Projects//completed//Portfolio//index.html")
            speak("Opening Your Portfolio")

        elif "play sad song" in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLQeQA17Q3CYfMhJREvlmzaeEHqUS7R2-y")
            speak("Opening your Playlist")

        elif "play love song" in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLQeQA17Q3CYdZQLQ--T3oimLDugwHqQ9H")
            speak("Opening your Playlist")

        elif "play rage song" in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLQeQA17Q3CYek-jTt84cRIaRiSTecEjZ_")
            speak("Opening your Playlist")

        elif "play party song" in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PLQeQA17Q3CYf0fi4Tnbd0S667BrhQOAuc")            
            speak("Opening your Playlist")

# to find date and time

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss, the time is {strTime}")

        elif "date" in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak(f"Boss, today is {date} of {month} {year}")

# to open any program from pc

        elif "open code" in query:
            codePath = "C:\\Users\\manmo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening VS Code")

        elif "open projects" in query:
            codePath = "C:\\Users\\manmo\\OneDrive\\Desktop\\Coding Projects"
            os.startfile(codePath)
            speak("Opening your projects")

        elif "open word" in query:
            codePath = "C:\\Users\\manmo\\OneDrive\\Desktop\\Microsoft Office Word 2007.lnk"
            os.startfile(codePath)
            speak("Opening MS Word")

# keys tasks

        elif 'close current window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
            speak("Current window is closed.")

        elif 'minimise all window' in query:
            desktop()
            speak("Minimized all windows")

        elif 'full screen' in query:    
            pyautogui.keyDown('f11')
            pyautogui.keyUp('f11')
            speak("Yes Boss")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
           
        elif 'shutdown' in query or 'shut down' in query or 'close my PC' in query:
            shutDown()

        elif 'restart' in query or 'reboot' in query:
            restart()

        elif 'sleep' in query or 'sleep mode' in query:
            Sleep()    

        elif 'exit' in query:
            speak("goodbye boss. Have a nice day")
            break    

# search on youtube or google

        elif "search on youtube" in query:
            speak("Boss, What do you want to search?")

            video = takeCommand().lower()
            search_youtube(video)

        elif "search on google" in query:
            speak("Boss, What do you want to search?")

            query = takeCommand().lower()
            search_google(query)

# basic calculations like addition substraction and division

        elif "calculate" in query:
            speak("Boss, What do you want to calculate?")

            query = takeCommand().lower()
            query = query.replace("calculate ", "")
            result = eval(query)
            speak("The answer is " + str(result))

# whatsapp automation to send message or calls

        elif "send message" in query or "send a message" in query or "phone call" in query or "video call" in query:
            flag = ""
            contact_no, name = findContact(query)

            if(contact_no !=0):

                if "send a message" in query or "send message" in query:
                    flag = 'message'
                    speak("what message to send Boss")
                    query = takeCommand()
                
                elif "phone call" in query:
                    flag = 'call'

                else:
                    flag = 'video call'   
                whatsApp(contact_no, query, flag, name)

            else:
                speak("Contact not found")            

# to book a cab using voice command

        elif "book a cab" in query:
            friday_book_cab()

# to search something from AI

        # else:
        #     output = aiProcess()
        #     speak(output)


# pip install -r requirements.txt ---(to install all the required packages)
# python friday.py ---(to run the python script)
from datetime import datetime
from Body.Speak import Speak
from Body.Listen import MicExecution
from Brain.AIBrain import ReplyBrain
import webbrowser
import time
import pyjokes
import pywhatkit as kit
import pyautogui
import PyPDF2
import psutil
import os
# pip install pywhatkit

def pdf_reader():
    book = open("hello.pdf", 'rb')
    pdfReader = PyPDF2.PdfReader(book)  
    pages = len(pdfReader.pages) 
    Speak(f"Total number of pages in this book: {pages}")
    while True:
        try:
            pg = int(input("Please enter the page number (1 to {}): ".format(pages)))
            if 1 <= pg <= pages:
                break
            else:
                print("Invalid page number. Please enter a number between 1 and {}.".format(pages))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    page = pdfReader.pages[pg - 1] 
    text = page.extract_text()
    Speak(text)
    book.close()


def MainExe():
    while True:
        Data = MicExecution()
        Data = str(Data)
        Data = Data.lower()
        if len(Data)<3:
            pass
        elif "open youtube" in Data:
            Speak("opening YouTube sir...")
            webbrowser.open("https://youtube.com")
        elif "open instagram" in Data:
            Speak("opening Instagram sir...")
            webbrowser.open("https://www.instagram.com/")
        elif "open whatsapp" in Data:
            Speak("opening Whatsapp sir...")
            webbrowser.open("https://web.whatsapp.com/")
        elif "open stackoverflow" in Data:
            Speak("opening stackoverflow sir...")
            webbrowser.open("https://www.stackoverflow.com/")
        elif "open google" in Data:
            Speak("sir, what should I search on google...")
            query = MicExecution().lower()
            Speak(f"Roger sir, opening google and searching {query}")
            webbrowser.open(f"{query}")
        elif "open spotify" in Data:
            Speak("sir, what should I play on spotify...")
            query = MicExecution().lower()
            Speak(f"Roger sir, opening spotify and playing {query}")
            webbrowser.open(f"https://open.spotify.com/search/{query}")
        elif "send message" in Data:
            contact_list = {
                "rishabh": "+918218964361",
                "oreo": "+918171196035",
            }
            Speak("To whom you want to message sir.....")
            recipient_name = MicExecution().lower()
            Speak("Sir, please tell me your message")
            message = MicExecution().lower()
            # current_time = datetime.now()
            if recipient_name in contact_list:
                recipient_number = contact_list[recipient_name]
                # current_time = datetime.now()
                # kit.sendwhatmsg(recipient_number, message, current_time.hour, current_time.minute+1)
                kit.sendwhatmsg_instantly(recipient_number, message)
            else:
                print(f"No contact found for the name {recipient_name}.")
        elif "play song" in Data:
            Speak("sir, which song you want to play...")
            query = MicExecution().lower()
            Speak(f"Roger sir, playing {query} song on youtube")
            kit.playonyt(query)
        elif "search on youtube" in Data:
            Speak("sir, what should I search on youtube...")
            query = MicExecution().lower()
            Speak(f"Roger sir, searching {query} on youtube")
            kit.playonyt(query)
        elif "tell me a joke" in Data:
            joke = pyjokes.get_joke()
            Speak(joke)
        elif "switch window" in Data:
            Speak("Switching window sir...")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        elif "read pdf" in Data:
            pdf_reader()
        elif 'play offline song'in Data:
            music_dir = "C:\\Users\\hp\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif "how much power left" in Data or "how much power we have" in Data or "battery status" in Data:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            Speak(f"sir our system have {percentage} percent battery left")
        elif 'jarvis quit' in Data or 'exit' in Data or 'close' in Data or 'bye' in Data:
            Speak("Thanks you for using Jarvis Sir")
            exit()
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)


def authenticate_user():
    Speak("Please enter the passcode to access confidential data of Rishabh sir")
    attempts = 3

    while attempts > 0:
        temp = MicExecution()
        temp = str(temp).lower()

        if temp == "hello jarvis":
            Speak("Access granted. Welcome back Rishabh sir. How may I assist you?")
            MainExe()
            break
        else:
            attempts -= 1
            if attempts != 0:
                Speak(f"Access denied. {attempts} {'attempts' if attempts != 1 else 'attempt'} remaining. Please try again.")

    Speak("Sorry, access denied. Too many unsuccessful attempts. Exiting.")
    Speak("Enter passcode after 10 seconds....")
    time.sleep(10)
    authenticate_user()




def wish():
    hour = int(datetime.now().hour)
    if(hour>=8 and hour<=12):
        Speak("good morning sir...")
    elif hour>12 and hour<18:
        Speak("good afternoon sir...")
    else:
        Speak("good evening sir...")
    Speak("I am Jarvis, at your service.")
    authenticate_user()
    # MainExe()




wish()









# from Brain.AIBrain import ReplyBrain
# from Body.Listen import MicExecution
# print(">> Starting The Jarvis: Wait for some seconds.")
# from Body.Speak import Speak
# from Features.Clap import Tester
# print(">> Starting The Jarvis: Wait For Few Seconds More")

# def MainExecution():
#     Speak("Hello Sir")
#     Speak("I'm Jarvis, I'm Ready To Assist You Sir.")
#     while True:
#         Data = MicExecution()
#         Data = str(Data)
#         Reply = ReplyBrain(Data)
#         Speak(Reply)

# def ClapDetect():
#     query = Tester()
#     if "True-Mic" in query:
#         print("")
#         print(">> Clap Detected!! >>")
#         print("")
#         MainExecution()
#     else:
#         pass


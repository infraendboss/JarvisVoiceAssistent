import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess                   #het werken met verschillende processen (OS)
import pyttsx3                      #text to speech  library
#from gtts import gTTS              #in aanbouw
import tkinter                      #gebruiks interface maken     
import json                         #jAVASCRIPT module
import random                       #random class, random bepalingen
import operator                     #+,-,**. (voor de operatoren)
import speech_recognition as sr     #herkennen van speech 
from datetime import datetime
import wikipedia                    #voor het opzoeken van wiki stukke 
import webbrowser                   #het openen van webbrowsers
import os                           #het werkend maken van de os in python
import smtplib                      #smtp protocol om mails te sturen
import ctypes                       #het gebruik van van de c library
import time                         #het gebruik maken van tijd
import requests                     #voor de http bibliotheek
import shutil                       #het uitztten van het systeem
from bs4 import BeautifulSoup       #het gebruik van HTML files
import win32com.client as wincl     #text to speech api
from urllib.request import urlopen  #voor het openen van urls
import pyaudio                      #de python driver autio 
import locale                       #lokale tijd instellingen
import pyjokes                      #cabretier
import wolframalpha                 #opnoemen van de tijd
from ecapture import ecapture as ec #camera

def takeCommand():
	r = sr.Recognizer()

with open('assistentconfig.json') as bestand:
    config = json.load(bestand)
gmailpassword = config['mailPassword']
mail = config['mail']
newsapi = config['newsapi']

def speak(text):
    tts = gTTS(text=text, lang="nl")
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    tts.save(filename)
    playsound.playsound(filename)

def sendEmail(to, content):                             #gebruik de email library
	server = smtplib.SMTP('smtp.gmail.com', 587)        #gebruik poort 587 icm smtp mail
	server.ehlo()                                       #smtp protocol client
	server.starttls()                                   #tls protovol client
	
	# Enable low security in gmail
	server.login(mail, gmailpassword)
	server.sendmail(mail, to, content)
	server.close()



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio, language ='nl-in')	 
            print(said)

        except Exception as e:
            print("Exception: " + str(e))

    return said

text = get_audio()

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()


     
    while True:
         
        text = get_audio().lower()

        if "hallo" in text:
            hour = int(datetime.now().hour)  #tussen 0:00 en 12:00 goedemorgen
            if hour>= 0 and hour<12:
                speak("Goede morgen deze morgen !")
            
            
            elif hour>= 12 and hour<18:               #tussen 12:00-18:00 goedemiddag
                speak("Goedemiddag deze middag") 

            else:
                speak("Goedeavond deze avond!")           #de rest is goedenavond

            speak("Hoe zal ik je noemen")             #creeen van een gebruikersnaam
            uname = get_audio()
            speak("Welkom meneer")
            speak(uname)
            columns = shutil.get_terminal_size().columns    #zet de naam weer in overzichtelijke weergave
            
            print("##########################################################".center(columns))  ####
            print("Welkom Mr.", uname.center(columns))     #gebruikersnaam
            print("##########################################################".center(columns))  ###
            
            speak("Hoe kan ik je helpen")



        elif "je naam" in text:
            speak("Mijn naam is Youri ")
        elif "why you came to world" in text:
            speak("Thanks to Youri his python skills")
        elif 'open YouTube' in text:                 #openen van youtube door user
            speak("lekker filmpjes kijken\n")         #wordt gezegd door jarvis
            webbrowser.open("youtube.com")            #openen door webbrowser libbrary

        elif 'nieuws' in text: 
            try: 
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=nl&apiKey=' + newsapi)
                data = json.load(jsonObj)
                i = 1
                    
                speak('hier is wat interessant nieuws uit Nederland')
                print('''=============== TIMES OF Nederland ============'''+ '\n')
                    
                for item in data['articles']:
                        
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                    
                print(str(e))

        elif 'sluit scherm' in text:
            speak("vergrendel de laptop")
            ctypes.windll.user32.LockWorkStation()

        elif 'uitzetten' in text:
            speak("ik schakel de laptop uit")
            os.system('shutdown -s')

        elif 'stackoverflow' in text:
            speak("Lekker coderen met de codeerbeer")
            webbrowser.open("stackoverflow.com")   

        elif 'tijd' in text:                                                 #openen van de tijd door user
            strTime = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")     #library wordt opgehaald
            speak(f"Youri de tijd is {strTime}")                                 #jarvis zegt de tijd

        elif 'open youtube' in text:                 #openen van youtube door user
            speak("lekker Youtuben\n")         #wordt gezegd door jarvis
            webbrowser.open("youtube.com")            #openen door webbrowser libbrary

        elif 'speel muziek' in text or "Speel een nummer" in text:    #openen van muziek door user
            speak("lekker muziekjes luisteren")   
            os.startfile('C:\\Users\\Youri\\Music\\muziek.mp3')                          #jarvis bevestigd 
                
        elif 'achtergrond' in text:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                        0, 
                                                        "C:\\Users\\Youri\\Pictures\\epicfoto.jfif",
                                                        0)
            speak("ik heb je achtergrond veranderd")

        elif "waar is" in text: #werkt nu wel
            query = text.replace("waar is", "")
            speak(f"Gebruiker vraagt naar locatie {query}")
            webbrowser.open("https://www.google.nl/maps/place/" + query + "")

        elif "camera" in text or "foto" in text:
            #(ec.capture(0, "Jarvis Camera ", "img.jpg")
            (ec.capture(0,False,"img.jpg"))
            print("Foto is gemaakt")

        elif "maak een notitie" in text:
            speak("wat moet ik noteren")
            note = get_audio()
            file = open('jarvis.txt', 'w')
            speak("Moet ik de datum en tijd bijvoegen")
            snfm = get_audio()
            if 'ja' in snfm or 'okay' in snfm:
                strTime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "notitie inzien" in text:
            speak("notitie laten zien")
            file = open("jarvis.txt", "r")
            print(file.read())
            #speak(str(file.read(6))

        elif 'verstuur mail' in text:                          #openen van mail door user
            try:
                speak("wat moet ik zeggen")                     #jarvis vraagt om text in mail
                content = get_audio()                         #vraagt voor commando en vult dit in in terminal
                speak("naar wie moet ik het versturen")                    #jarvis vraagt om geadresseerde
                to = input()                                    #je kan zelf het mail adres intypen door middel van input
                sendEmail(to, content)                          #versturen van de mail middels librarys
                speak("de email is verstuurd!")                  #jarvis bevestigd
            except Exception as e:                              #email kan niet verstuurd worden
                print(e)
                speak("ik kan de mail niet versturen")       #jarvis bevestigd


import subprocess                   #het werken met verschillende processen (OS)
import pyttsx3                      #text to speech  library
import tkinter                      #gebruiks interface maken     
import json                         #jAVASCRIPT module
import random                       #random class, random bepalingen
import operator                     #+,-,**. (voor de operatoren)
import speech_recognition as sr     #herkennen van speech 
import datetime                     #opnemen van de lokale tijd/data
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

engine = pyttsx3.init('sapi5')              #de pyttsx3 is de text to speech libtary, de sapi 5 is de Microsoft spreech
voices = engine.getProperty('voices')       #het ophalen van de stemgeluiden
engine.setProperty('voice', voices[0].id)   #1 is vrouwelijk, 0 is mannelijk

with open('assistentconfig.json') as bestand:
    config = json.load(bestand)
gmailpassword = config['mailPassword']
mail = config['mail']
newsapi = config['newsapi']



def speak(audio):                           #het instellen van de audio en spreken tekst
	engine.say(audio)                       
	engine.runAndWait()

def wishMe():                                 #functie om te begroeten
	hour = int(datetime.datetime.now().hour)  #tussen 0:00 en 12:00 goedemorgen
	if hour>= 0 and hour<12:
		speak("Good morning !")

	elif hour>= 12 and hour<18:               #tussen 12:00-18:00 goedemiddag
		speak("Good afternoon !") 

	else:
		speak("Good Evening Sir !")           #de rest is goedenavond


	assname =("Jarvis 1 point o")             #gebasseerd op Iron man
	speak("I am your Assistant")
	speak(assname)
	

def usrname():
	speak("What should i call you sir")             #creeen van een gebruikersnaam
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns    #zet de naam weer in overzichtelijke weergave
	
	print("#####################".center(columns))  ####
	print("Welcome Mr.", uname.center(columns))     #gebruikersnaam
	print("#####################".center(columns))  ###
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:                 #gebruik de build in mic voor stemmen
		
		print("Luisteren...")                       #aan het luisteren
		r.pause_threshold = 1                       #pauze van een seconde, anders crasht het programma
		audio = r.listen(source)

	try:
		print("Herkennen...")                     
		query = r.recognize_google(audio, language ='nl-in')        #gebruik de nederlandse google stem
		print(f"Gebruiker: {query}\n")

	except Exception as e:
		print(e) 
		print("Ik snap het niet") 
		return "None"
	
	return query

def sendEmail(to, content):                             #gebruik de email library
	server = smtplib.SMTP('smtp.gmail.com', 587)        #gebruik poort 587 icm smtp mail
	server.ehlo()                                       #smtp protocol client
	server.starttls()                                   #tls protovol client
	
	# Enable low security in gmail
	server.login(mail, gmailpassword)
	server.sendmail(mail, to, content)
	server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    usrname()
     
    while True:
         
        query = takeCommand().lower()
         
        # Al de commandos gezegd door user zulle  worden
        # opgeslagen  in 'query' en zullen
        # converted worden door lower case for makkelijk 
        # herkenning van command
        if 'wikipedia' in query:                                   #inladen van wikipedia
            speak('Searching Wikipedia...')                        #er wordt gezogd in wikipedia
            query = query.replace("wikipedia", "")                 
            results = wikipedia.summary(query, sentences = 3)      #eerste drie zinnen
            speak("According to Wikipedia")
            print(results)
            speak(results)          
 
        elif 'open youtube' in query:                 #openen van youtube door user
            speak("Here you go to Youtube\n")         #wordt gezegd door jarvis
            webbrowser.open("youtube.com")            #openen door webbrowser libbrary
 
        elif 'open google' in query:                 #openen van youtube door user                  
            speak("Here you go to Google\n")         #wordt gezegd door jarvis
            webbrowser.open("google.com")           #openen door webbroswer in lobrary
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")   
			
        elif 'speel muziek' in query or "speel een nummer" in query:    #openen van muziek door user
            speak("Here you go with music")                             #jarvis bevestigd 
            # music_dir = "C:\\youridevos\\Song"
            music_dir = "C:\\Users\\youridevos\\Music"                  #de dir waar muziek in staar
            songs = os.listdir(music_dir)                               #opent de muziekspeler            
            print(songs)        
            random = os.startfile(os.path.join(music_dir, songs[0]))    #speelt random songs af (begint bij de eerste = 0)
 
        elif 'de tijd' in query:                                        #openen van de tijd door user
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   #library wordt opgehaald
            speak(f"Sir, the time is {strTime}")                        #jarvis zegt de tijd
 
        elif 'open chrome' in query:                                                        #openen van chrome door user
            codePath = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"        #opent het code path
            os.startfile(codePath)                                                          #start chrome op
   
        elif 'verstuur mail' in query:                          #openen van mail door user
            try:
                speak("What should I say?")                     #jarvis vraagt om text in mail
                content = takeCommand()                         #vraagt voor commando en vult dit in in terminal
                speak("whome should i send")                    #jarvis vraagt om geadresseerde
                to = input()                                    #je kan zelf het mail adres intypen door middel van input
                sendEmail(to, content)                          #versturen van de mail middels librarys
                speak("Email has been sent !")                  #jarvis bevestigd
            except Exception as e:                              #email kan niet verstuurd worden
                print(e)
                speak("I am not able to send this email")       #jarvis bevestigd
 
        elif 'hoe gaat het' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'goed' in query or "het gaat goed" in query:
            speak("It's good to know that your fine")
 
        elif "verander mijn naam in" in query:
            query = query.replace("verander mijn naam in", "")
            assname = query
 
        elif "verander naam assistent" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "wat is jouw naam" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "wie heeft jou gemaakt" in query or "who created you" in query: 
            speak("I have been created by Youri.")
             
        elif 'grap' in query:
            speak(pyjokes.get_joke())
             

        elif 'zoeken' in query or 'play' in query:
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query) 
 
        elif "wie ben ik" in query:
            speak("If you talk then definately your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Youri his python skills")
 
        #elif 'PowerPoint presentatie' in query or "Powerpoint":
            #speak("opening Power Point presentation")
            #power = r"C:\\Users\\youridevos\\Desktop\\Voice Assistant.pptx"
            #os.startfile(power)
        
        elif 'Powerpoint' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\youridevos\\Desktop"
            os.startfile(power)
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Youri")
 
        elif 'reason for you' in query:
            speak("I was created as a  project by Mister Youri ")

                
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")
 
        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
 
        elif 'nieuws' in query:
             
            try: 
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=nl&apiKey=' + newsapi)
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of Nederland')
                print('''=============== TIMES OF Nederland ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
                

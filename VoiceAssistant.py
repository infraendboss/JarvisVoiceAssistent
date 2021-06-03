#Voor extra informatie kan de README file gelezen worden betreft deze epische Voice Assistent

import os                           #interactie met het besturingssysteem
import time                         #koppeling naar huidige tijd
import playsound                    #afspelen van geluid    
import speech_recognition as sr     #gebruik van de microfoon
from gtts import gTTS               #Google Text To speech
import subprocess                   #het werken met verschillende processen (OS)
import json                         #jAVASCRIPT module voor api en wachtwoorden
import random                       #random class, random bepalingen
import operator                     #+,-,**. (voor de operatoren)
from datetime import datetime       #datum en tijd notatie
import wikipedia                    #voor het opzoeken van wiki stukke 
import webbrowser                   #het openen van webbrowsers
import smtplib                      #smtp protocol om mails te sturen
import ctypes                       #het gebruik van van de c library
import requests                     #voor de http bibliotheek
import shutil                       #het uitztten van het systeem
from bs4 import BeautifulSoup       #het gebruik van HTML files
from urllib.request import urlopen  #voor het openen van urls
import pyaudio                      #de python driver autio 
import locale                       #lokale tijd instellingen
from ecapture import ecapture as ec #camera
from ip_address import bridge_ip_address    
from phue import Bridge             #aansturen van lampen
from requests.structures import CaseInsensitiveDict


def takeCommand():
	r = sr.Recognizer()                         #aansturen van de microfoon 

with open('assistentconfig.json') as bestand:   #openen config bestand
    config = json.load(bestand)
gmailpassword = config["mail"]['mailPassword']  #variabelen aanmaken vanuit json
mail = config['mail']["email"]
newsapi = config["nieuws"]['newsapi']
weerapi = config["weer"]['weerapi']

def speak(text):
    tts = gTTS(text=text, lang="nl")                        #bepaling taal voor gtts
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")   #slaat bestanden op met datum tijd
    filename = "voice"+date_string+".mp3"                   #filename wordt gecreeeerd
    tts.save(filename)                                      #file wordt opgeslagen
    playsound.playsound(filename)

def sendEmail(to, content):                             #gebruik de email library
	server = smtplib.SMTP('smtp.gmail.com', 587)        #gebruik poort 587 icm smtp mail
	server.ehlo()                                       #smtp protocol client
	server.starttls()                                   #tls protovol client
	
	# Enable low security in gmail
	server.login(mail, gmailpassword)                   #logt in op mail
	server.sendmail(mail, to, content)                  #verstuurd mail
	server.close()                                      #connectie wordt verbroken

def access_lights(bridge_ip_address):                   #lampen aansturen
    b = Bridge(bridge_ip_address)                       #zoekt ip address uit bestand
    light_names_list = b.get_light_objects('name')      #haalt namen van lampen
    return light_names_list                             #stuurt namen terug

def danger_mode():                                      #functie lampen aanzetten
    lights = access_lights(bridge_ip_address)           #zoekt ip addres bridge
    time.sleep(1)                                       #lampen doen 1 seconde 
    for light in lights:
        lights[light].on = True                         #zet lampen aan
        lights[light].hue = 180                         #lampen wit
        lights[light].saturation = 100                  #helderheid
    time.sleep(1)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 7000                        #lampen geel
        lights[light].saturation = 100                  

def uit():                                              #zet de lampen uit
    lights = access_lights(bridge_ip_address)
    for light in lights:
        lights[light].on = False                        #uit

def get_audio():                    #haalt audio op
    r = sr.Recognizer()             #r variabele microfoon
    with sr.Microphone() as source: # gebruik de standaardmicrofoon als audiobron
        audio = r.listen(source)    # luister naar de eerste zin en extraheer deze in audiogegevens
        said = ""                   #maakt variabele said

        try:
            said = r.recognize_google(audio, language ='nl-in') #library taal nederlands	 
            print(said)                                         #print gesproken tekst

        except Exception as e:                                  #wanneer er niks gezegd is
            print("Ik heb u niet gehoord" + str(e))             #print ik heb u niet gehoord

    return said

text = get_audio()                                              #variabele text 

if __name__ == '__main__':                          #zorgt ervoor dat clear screeen op elk type pc werkt
    clear = lambda: os.system('cls')                #haalt os op, cls wordt clear
     
    # This Function will clean any
    # command before execution of this python file
    clear()



     
    while True:
         
        text = get_audio().lower()          #de text wordt omgezet in lowercase 

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
            
            print("#######################################".center(columns))  ####
            print("Welkom Mr.", uname.center(columns))     #gebruikersnaam
            print("#######################################".center(columns))  ###
            
            speak("Hoe kan ik je helpen")



        elif "je naam" in text:
            speak("Mijn naam is Youri ")
        elif "Hoe ben je gemaakt" in text:
            speak("Door Youri zijn Python skills")
        elif 'open YouTube' in text:                  #openen van youtube door user
            speak("lekker filmpjes kijken\n")         #wordt gezegd door jarvis
            webbrowser.open("youtube.com")            #openen door webbrowser libbrary

        elif 'nieuws' in text:              
            try:                    
                jsonObj = urlopen('https://newsapi.org/v2/top-headlines?country=nl&apiKey=' + newsapi)  #haalt nieuwsapi op
                data = json.load(jsonObj)   #zet json text in variabele
                i = 1                       #start nummering nieuws artikelen
                    
                speak('hier is wat interessant nieuws uit Nederland')
                print('''=============== TIMES OF Nederland ============'''+ '\n')
                    
                for item in data['articles']:   
                        
                    print(str(i) + '. ' + item['title'] + '\n') #print headline arikel
                    print(item['description'] + '\n')           #print beschrijving
                    speak(str(i) + '. ' + item['title'] + '\n') #zegt headline artikel
                    i += 1
            except Exception:                                   #als er geen nieuws meer is
                print('dit was het nieuws')

        elif 'sluit scherm' in text:
            speak("vergrendel de laptop")
            ctypes.windll.user32.LockWorkStation()              #ctypes library vergendeld laptop

        elif 'uitzetten' in text:
            speak("ik schakel de laptop uit")
            os.system('shutdown -s')                            #os.system sluit laptop af

        elif 'stackoverflow' in text:
            speak("Lekker coderen met de codeerbeer")
            webbrowser.open("stackoverflow.com")                

        elif 'tijd' in text:                                            #openen van de tijd door user
            strTime = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")     #library wordt opgehaald
            speak(f"Youri de tijd is {strTime}")                        #jarvis zegt de tijd

        elif 'open youtube' in text:                 #openen van youtube door user
            speak("lekker Youtuben\n")               #wordt gezegd door jarvis
            webbrowser.open("youtube.com")           #openen door webbrowser libbrary

        elif 'speel muziek' in text or "Speel een nummer" in text:    #openen van muziek door user
            speak("lekker muziekjes luisteren")   
            os.startfile('C:\\Users\\Youri\\Music\\muziek.mp3')       #jarvis bevestigd 
                
        elif 'achtergrond' in text:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                        0, 
                                                        "C:\\Users\\youri\\Pictures\\epicfoto.jpg",
                                                        0)
            speak("ik heb je achtergrond veranderd")

        elif "waar is" in text: #werkt nu wel
            query = text.replace("waar is", "")                                 #verplaatst "waar is" in bestand
            speak(f"Gebruiker vraagt naar locatie {query}")                     #overgebleven plaatsmaa, om zom
            webbrowser.open("https://www.google.nl/maps/place/" + query + "")   #zoekt op base url icm query

        elif "camera" in text or "foto" in text:
            (ec.capture(0,False,"img.jpg"))         #maakt foto onder naam img.jpg
            speak("Foto is gemaakt")

        elif "maak een notitie" in text:
            speak("wat moet ik noteren?")
            note = get_audio()                  #spraak in variabele note
            file = open('jarvis.txt', 'w')      #creeerd een file jarvis.txt
            speak("Moet ik de datum en tijd bijvoegen")
            snfm = get_audio()                  #vraagt naar datum en tijd
            if 'ja' in snfm or 'okay' in snfm or 'goed' in snfm:  #akkoord in spraak    
                strTime = datetime.now().strftime("%d-%m")        #haalt datum op
                file.write(strTime)                               #zet datum in notitie
                file.write(" :- ")
                file.write(note)                                  #zet notitie in notitie
            else:
                file.write(note)
            speak('notitie is gemaakt')                            

        elif "notitie inzien" in text:
            speak("notitie laten zien")
            file = open("jarvis.txt", "r")                        #haalt notitie op
            speak(file.read())                                    #spreekt file text uiy
            

        elif 'verstuur mail' in text:                          #openen van mail door user
            try:
                speak("wat moet ik zeggen")                     #jarvis vraagt om text in mail
                content = get_audio()                           #vraagt voor commando en vult dit in in terminal
                speak("naar wie moet ik het versturen")         #jarvis vraagt om geadresseerde
                to = input()                                    #je kan zelf het mail adres intypen door middel van input
                sendEmail(to, content)                          #versturen van de mail middels librarys
                speak("de email is verstuurd!")                 #jarvis bevestigd
            except Exception as e:                              #email kan niet verstuurd worden
                print(e)
                speak("ik kan de mail niet versturen")       #jarvis bevestigd

    

        elif "weer" in text:
            # werkt met Google Open weather website
            base_url = "https://api.openweathermap.org/data/2.5/weather?"   #basis url
            speak(" Wat is de naam van de stad?")       
            city_name = get_audio()                                         #output stad naam in variabele
            print("Stad naam : " + city_name)                                
            complete_url = base_url + "appid=" + weerapi + "&q=" + city_name +"&units=metric"   #vormt de complete url
            response = requests.get(complete_url)                           #vraagt response api
            x = response.json()

            if x["cod"] != "404":                                           #als code geen error geeft
  
                # sla de waarde van "main" op
                # key variabele y in
                y = x["main"]
            
                # sla de corresponderende waarde op
                # naar de "temp" -toets van y
                current_temperature = y["temp"]
            
                # sla de corresponderende waarde op
                # op de "lucht druk van y
                current_pressure = y["pressure"]
            
                # sla de corresponderende waarde op
                # op de regenverwachting van y
                current_humidiy = y["humidity"]
            
                # sla de corresponderende waarde op
                # op de weer van y
                z = x["weather"]
            
                # sla de corresponderende waarde op
                # naar de "beschrijving" key op
                # de 0e index van z
                weather_description = z[0]["description"]
            
                #print de volgende waardes
                speak(" Temperatuur = " +
                                str(current_temperature) + 'graden'
                    "\n De luchtdruk is  = " +
                                str(current_pressure) + 'hectoPascal'
                    "\n Regenverwachting is  = " +
                                str(current_humidiy) + 'procent'
                    "\n Weersbeschrijving = " +
                                str(weather_description))
            
            else:                                   #als 404 als output komt
                print(" Stad niet gevonden ")

        elif "servers" in text or "server" in text:
            ip_list = ['192.168.1.239', '192.168.1.244', '192.168.1.1', '192.168.1.211']    #zet de ip in list
            for ip in ip_list:
                response = os.popen(f"ping {ip}").read()                                    #vaagt reactir van ips
                if "Approximate round trip times in milli-seconds" in response:             #als de waarde in reactie zit
                    speak(f"UP {ip} deze server is bereikbaar")
                    print(f"UP {ip} deze server is bereikbaar")
                else:
                    speak(f"DOWN {ip} de server is niet bereikbaar")
                    print(f"DOWN {ip} deze server is niet bereikbaar")

        elif 'virtueel' in text or 'machine' in text:  
                headers = CaseInsensitiveDict()
                headers["Authorization"] = "Basic c3R1ZGVudDpCbG9lbXBvdDEh"     #haalt de authentication op, name passwor
                urlID = "http://127.0.0.1:8697/api/vms"                         #variabele url van de vm
                resp = requests.get(urlID, headers=headers)                     #haalt reactie van variabelen
                jsonDataID = json.loads(resp.text)
                try:
                    for id in jsonDataID:
                        id = id['id']                                               #haalt het id van de vm op
                        urlStatus = f"http://127.0.0.1:8697/api/vms/{id}/power"  
                        resp2 = requests.get(urlStatus, headers=headers)            #naalt de waarde powerstate op
                        jsonDataStatus = json.loads(resp2.text)
                        print(f"ID: {id} STATUS: {jsonDataStatus['power_state']}")  #koppelt de waardes 
                        speak(f"STATUS: {jsonDataStatus['power_state']}")
                except Exception:
                    print("ERROR")  

        elif 'lampen aan' in text or 'disco' in text:
            if __name__ == '__main__':                  
                danger_mode()                           #haalt waardes op functie dangermode lampen
                speak('ik zet de lampen aan')

        elif 'lampen uit' in text: 
            if __name__ == '__main__':
                uit()                                   #haalt de waardes op functie uit 
            else:
                speak('ik kan de lampen niet uitzetten')
# Project Jarvis

Dit programma is geschreven voor de projectchallenge betreft de Applicatie-laag door Youri.
Python is een geschikte taal voor scriptschrijvers en ontwikkelaars. Zodanig is in deze taal de Voice Assistent geschreven.
Spraakherkenning is het proces waarbij audio in tekst wordt omgezet. Dit wordt vaak gebruikt in stemassistenten zoals Alex en Siri. Python biedt een API genaamd SpeechRecognition waarmee audio in tekst wordt gezet om te kunnen converteren voor verdere verwerking.

## Vereisten

### Systeemvereisten

Windows 10 versie
21H1

Python 3.9+

Microsoft Visual studio

### Modules

**De volgende modules en (pip)installaties zijn benodigd, vooralsnog het script werkt.**

Om het project werkend te laten krijgen, moeten allereerst de volgende modules worden geinstalleerd middels pip.

*Subproces:* - Deze module wordt gebruikt voor het verkrijgen van systeemsubprocesdetails die worden gebruikt in verschillende opdrachten, zoals afsluiten, slapen, enz. Deze module is ingebouwd met Python.

*Wolframalpha:* - Het wordt gebruikt om antwoorden op expertniveau te berekenen met behulp van Wolfram's algoritmen, kennisbank en AI-technologie. Typ het onderstaande commando in de terminal om deze module te installeren.

```md
pip3 install wolframaplha
```

*gTTS* - (Google Text-to-Speech), een Python-bibliotheek en CLI-tool om te communiceren met de tekst-naar-spraak-API van Google Translate. Schrijf gesproken mp3-gegevens naar een bestand, een bestandachtig object (bytestring) voor verdere audiomanipulatie, of stdout. Of genereer eenvoudig vooraf Google Translate TTS-verzoek-URL's om naar een extern programma te sturen.

```md
pip3 install gtts
```

*Tkinter:* - Deze module wordt gebruikt voor het bouwen van GUI en wordt geleverd met Python. Deze module is ingebouwd met Python.

*Wikipedia:* - Zoals we allemaal weten, is Wikipedia een geweldige bron van kennis, net als GeeksforGeeks, we hebben de Wikipedia-module gebruikt om informatie uit Wikipedia te halen of om Wikipedia-zoekopdrachten uit te voeren. Typ het onderstaande commando in de terminal om deze module te installeren.

```md
pip3 install wikipedia
```

*Spraakherkenning:* - Aangezien we een toepassing van stemassistent bouwen, is een van de belangrijkste dingen hierin dat uw assistent uw stem herkent (betekent wat u wilt zeggen / vragen). Typ het onderstaande commando in de terminal om deze module te installeren.

```md
pip3 installeer SpeechRecognition
```

*Webbrowser:* - Om op internet te zoeken. Deze module is ingebouwd met Python.

*Ecapture:* - Om afbeeldingen van uw camera vast te leggen. Typ het onderstaande commando in de terminal om deze module te installeren.

```md
pip3 installeer ecapture
```

*Pyjokes:* - Pyjokes wordt gebruikt voor het verzamelen van Python-grappen via internet. Typ het onderstaande commando in de terminal om deze module te installeren.
pip pyjokes installeren

*Datetime:* - Datum en tijd wordt gebruikt om datum en tijd weer te geven. Deze module is ingebouwd met Python.

*Twilio:* - Twilio wordt gebruikt voor het maken van oproepen en berichten. Typ het onderstaande commando in de terminal om deze module te installeren.

```md
pip3 install twilio
```

*Requests:* - Requests worden gebruikt voor het doen van GET- en POST-verzoeken. Typ het onderstaande commando in de terminal om deze module te installeren.

```md
pip3 install requests
```

*BeautifulSoup:* - Beautiful Soup is een bibliotheek die het gemakkelijk maakt om informatie van webpagina's te schrapen. Typ het onderstaande commando in de terminal om deze module te installeren.

```md
pip install beautifulsoup4
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```md
Luisteren ... 
Herkennen ... 
Gebruiker zei: Youri
##################### 
Welkom meneer Youri 
##################### 
Luisteren ... 
Herkennen ... 
Gebruiker zei: Youri op Wikipedia
Joeri, Yoeri en Yuri zijn Nederlandse jongensnamen die afkomstig zijn van de Slavische naam Юрий die 'Bewerker van de aarde' betekent.
Luisteren ... 
Herkennen ... 
Gebruiker zei: open YouTube
Luisteren ... 
Herkennen ...
Kan je stem niet herkennen. 
Luisteren ... 
Herkennen ... 
Gebruiker zei: exit

en herhaal
```

## Aanvulling van code

Om de code aan te vullen, kan het volgende statement worden toegevoegd:

```md
elif ... in text:
    commando invoeren
```

## Bronnen

* [gTTS](https://gtts.readthedocs.io/en/latest/) - Google Text-to-Speech
* [News Api](https://newsapi.org/) - Nederlands nieuws
* [Wolframalpha](https://www.wolframalpha.com/) - Computer expert-level answers
* [GeeksforGeeks](https://www.geeksforgeeks.org/voice-assistant-using-python/) - Jarvis Assistent
* [Weather Api](https://openweathermap.org/) - Weer API


## Versiebeheer

Versiebeheer wordt bijgehouden in GitHub. Voor alle versies kan de [GitHub](https://github.com/infraendboss/JarvisVoiceAssistent) geraadpleegd worden.

## Authors

* **Youri de Vos** - [GitHub](https://gist.github.com/infraendboss)

## Acknowledgments

* Iron Man the movie
* Bjorn Hamels
* Richard Stam

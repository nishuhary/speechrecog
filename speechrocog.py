from logging import info
import speech_recognition as sr
#This is to recognise the speech by the user
from gtts import gTTS
#This is to import Google TextToSpeech module
import datetime
import wikipedia
#To import date and time
import wikipediaapi as wiki
wiki_wiki = wiki.Wikipedia('en')
#Importing Wikipedia 
import os
#Importing os to get audio input

def voice_greetings():
    if(now<todaynoon):
        myobj =gTTS(text="Good Morning!", lang='en', slow=False)
        myobj.save("greetings.wav")
        os.system("greetings.wav")
    
    elif(now>todaynoon and now<todayevening):
        myobj =gTTS(text="Good Afternoon!", lang='en', slow=False)
        myobj.save("afternoon.wav")
        os.system("afternoon.wav")

    elif(now>todayevening):
        myobj =gTTS(text="Good Evening!", lang='en', slow=False)
        myobj.save("evening.wav")
        os.system("evening.wav")

def voice_bye():
    objbye =gTTS(text="See you later!", lang='en', slow=False)
    objbye.save("bye.wav")
    os.system("bye.wav")

def search_keyword():
    if 'search' in userword:
        l = userword.split()
        l.pop(0)
        word = (" ".join(l))
        info_search(word) # to get output_summary of user's choice

def info_search(word):
    page_wiki = wiki_wiki.page(word)
    info = page_wiki.summary
    stop = info.find('.')
    spos = info.find('(')
    #Starting postion of string
    lpos = info.find(';')
    #Last position of string
    output_summary = info[0:spos] + info[lpos+1:stop+1]
    print(output_summary)
    summaryinfovoice =gTTS(text=output_summary, lang='en', slow=False)
    summaryinfovoice.save("output_summary.wav")
    os.system("output_summary.wav")

#This is to recognise the user's audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    userword=r.recognize_google(audio)
    print(userword)
except sr.UnknownValueError:
    userword=None
    print("Google Speech Recognition could not understand audio")
    unkerror =gTTS(text="Sorry i cant understand you", lang='en', slow=False)
    unkerror.save("errornovalue.wav")
    os.system("errornovalue.wav")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

#Time variables
now = datetime.datetime.now()
todaynoon=now.replace(hour=12, minute=0, second=0)
todayevening=now.replace(hour=18, minute=0, second=0)

#Greetings
if (userword in ["hello","haii","hola"]):
   voice_greetings()

if (userword in ["bye","see you","im going","bye bye","goodbye"]):
    voice_bye()

search_keyword()
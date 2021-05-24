#pip install pyttsx3
#pip install speechRecognition
#pip install wikipedia
#pip install PyAudio
# (if pyaudio doesnt install , then goto 'https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio'
# and download the .whl file based on the python version (maybe first one is the one to download) 
# and install that file by going to that directory and 'pip install filename.whl' )
import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
 
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
 
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")  
 
    else:
        speak("Good Evening!")  
 
    speak("I am Jarvis Sir. Please tell me how may I help you")      
 
def takeCommand():
    #It takes microphone input from the user and returns string output
 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"User said: {query}\n")
 
    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
 
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
 
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
 
        # Logic for executing tasks based on query
        #wikipedia one maynot work so just ignore, if find the solution msg me
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            query = query.replace("open youtube", "")
            ytsearchL=query.split(" ")
            ytsearch='+'.join(ytsearchL)
            webbrowser.open("youtube.com/results?search_query={}".format(ytsearch))
            # https://www.youtube.com/results?search_query=elon+musk
 
        elif 'open google' in query:
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
 
 
        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
 
        elif 'open code' in query:
            # bhai just change the path accordingly
            codePath = "C:\\Users\\khush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to Danish Jain' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "danishislove@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend khushil bhai. I am not able to send this email")

        elif 'exit' in query:
            exit(0)        

        elif 'vah bete vah' in query:
            speak("Ttam tto badde heavy driver ho")     

        elif 'dosti' in query:
            speak("School ki dosti 10th class tak, , , ,college ki dosti final year tak, , , , lover ki dosti shaaadi tak, , , but hamari dosti thees faravari tak,  , , , kyuki thees faravari nah khabhi ayegi , , , , aur nah hi humari dosti khabhi khutam hogi.")

        elif 'teri zubaan bahut chalti hai surya' in query:
            speak("haath zyada chalta hai")    

        elif 'mere power' in query:
            speak("Mujhe yaad rakhne ki zarurat nahi")

        elif 'mujh se haath mila le' in query:
            speak("Gaddar se dosti nahi karta")       

        elif 'maharaja jaega' in query:
            speak("apni soch")      

        elif 'itna guroor theek nahin' in query:
            speak("sarrr  purrr kaffan baandhne walle moth se nahi darteh")
            speak(" ab nikal yaha se")

        elif 'ok ok cool' in query:
            exit(0)              

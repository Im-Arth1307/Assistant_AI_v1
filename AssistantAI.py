import win32com.client  #For windows-specific functionalities.
import speech_recognition as sr
import os   #Provides a way to interact with the operating system
import webbrowser
import openai
import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")      #Speech Application Programming Interface

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1   #Sets the pause threshold to 1 second, indicating the maximum amount of silence before a phrase is considered complete.
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language = "en-in")       #Understanding the audio 
            print(f"User said : {query}")
            return query    #'query' is what was said by the user
        except Exception as e:
            return "Some Error Ocurred. Sorry."

while 1:    #Infinite loop to keep the script running continuously.
    speaker.Speak("Hello this is AI")
    while True:     #Inner loop continuously listens for user commands.
        print("Listening....")
        query = takeCommand().lower()
        sites = [["youtube", "https://youtube.com"] , ["wikipedia" , "https://wikipedia.com"] , ["google", "https://google.com"]]   #List of lists
        
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]}")
                webbrowser.open(site[1])
                
        if "open music" in query:
            musicPath = r"Enter the path for a downloaded mp3 file."      #Prefix the string with 'r' to treat it as a raw string, which will ignore escape sequences.
            os.startfile(musicPath)

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"The time is {strfTime}")

        if "open brave browser" in query:
            brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            os.startfile(brave_path)

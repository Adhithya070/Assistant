import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import openai

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('88AU3Q-Q46GJ73W74')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

openai.api_key = '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'

def speak(audio):
    print('\nAssistant : ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if 0 <= currentH < 12:
        speak('Good Morning!')
    elif 12 <= currentH < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

greetMe()

speak('I am JARVIS, your digital assistant!')
speak('How may I help you?')

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query

def chatGPT(query):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=query,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    while True:
        query = myCommand()
        query = query.lower()

        if "chat" in query:
            speak('Please give your query! :')
            conversation = []
            user_input = myCommand()
            conversation.append('User: ' + user_input)
            assistant_response = chatGPT('\n'.join(conversation))
            conversation.append(assistant_response)
            if ("code" in user_input):
                speak("Here is your code :")
                print(assistant_response)
            else:
                speak(assistant_response)


        elif 'open youtube' in query:
            speak('Opening YouTube!')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('Opening Google!')
            webbrowser.open('www.google.co.in')
        elif 'open gmail' in query:
            speak('Opening Gmail!')
            webbrowser.open('www.gmail.com')
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('It was nice chatting with you. Have a great day!')
            sys.exit()
        elif 'hello' in query:
            speak('Hello Sir')
        elif 'bye' in query:
            speak('It was nice chatting with you. Have a great day!')
            sys.exit()
        else:
            query = query
            speak('Processing...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Here you go...')
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Here you go...')
                    speak(results)
            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sir!')

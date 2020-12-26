#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


# In[2]:


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def talk(text):
    engine.say('I am your alexa')
    engine.say('What can I do for you')
    engine.runAndWait()


# In[3]:


def take_command():
    try:
        with sr.Microphone()as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                    command = command.replace('alexa','')
                    print(command)
    except:
        pass
    return command


# In[ ]:


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt('playing')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is'+time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is','')
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry,I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again.')

        
while True:
    run_alexa()


# In[ ]:





# In[ ]:





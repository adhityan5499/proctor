#need to add [save if common member exists]

import speech_recognition as sr
import pyaudio
import wave
import time
import threading
import os

def convert(i):
    if i >= 0:
        #sound = 'record' + str(i) +'.wav'
        sound = 'rai000' + str(i+1) +'.wav'
        r = sr.Recognizer()
        
        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
            print("Converting Audio To Text and saving to file..... ") 
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio, language="en-IN") ##### API call to google for speech recognition
            if str is bytes: 
                result = u"{}".format(value).encode("utf-8")
            else: 
                result = "{}".format(value)
            with open("test.txt","a") as f:
                f.write(result)
                f.write(" ")
                f.close()
                
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("{0}".format(e))
        except KeyboardInterrupt:
            pass


#user input of exam duration
duration=int(input('Enter the duration of exam\n'))
f = open("test.txt","r+")
f. truncate(0)
f. close()

for i in range(duration//4): # Number of total seconds to record/ Number of seconds per recording
    convert(i) 

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

file = open("test.txt") ## Student speech file
data = file.read()
file.close()
tokens = word_tokenize(data)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
word_tokens = [word for word in stripped if word.isalpha()]
# filter out stop words
stop_words = set(stopwords.words('english'))   
#word_tokens = word_tokenize(data) ######### tokenizing sentence

filtered_sentence = [w for w in word_tokens if not w in stop_words]  
print('Recorded: ')
print(filtered_sentence,end='\n')

####### creating a final file
f = open("final.txt","r+")
f. truncate(0)
f. close()
f=open('final.txt','w')
for ele in filtered_sentence:
    f.write(ele+' ')
f.close()
    
##### checking whether proctor needs to be alerted or not
file = open("question_paper.txt") ## Question file
data = file.read()
file.close()
tokens = word_tokenize(data)
# convert to lower case
tokens = [w.lower() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
word_tokens = [word for word in stripped if word.isalpha()]
# filter out stop words
stop_words = set(stopwords.words('english'))   
#word_tokens = word_tokenize(data) ######### tokenizing sentence

filtered_questions = [w for w in word_tokens if not w in stop_words]  

filtered_questions.append('first')
print(filtered_questions)

def common_member(a, b):     
    a_set = set(a) 
    b_set = set(b) 
      
    # check length  
    if len(a_set.intersection(b_set)) > 0: 
        return(a_set.intersection(b_set))   
    else: 
        return([]) 

comm = common_member(filtered_questions, filtered_sentence)
print('Number of common elements:', len(comm))
print(comm)
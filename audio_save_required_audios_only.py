
import speech_recognition as sr
import pyaudio
import wave
import time
import threading
import os

def common_member(a, b):  
    b_list = list(str(b).split(" "))
    #print(f'Type of text is {type(b)} ')
    b_list = list(map(str.lower,b_list))
    b_set = set(b_list)
    a_set = a
    print('Current recording\n')
    print(b_set,end='\n')
    # check length  
    if len(a_set.intersection(b_set)) > 0: 
        return(a_set.intersection(b_set))   
    else: 
        return([]) 

def read_audio(stream, filename):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 4 # Number of seconds to record at once
    filename = filename
    frames = []  # Initialize array to store frames
    
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    # Stop and close the stream
    stream.stop_stream()
    stream.close()

def convert(i):
    if i >= 0:
        sound = 'record' + str(i) +'.wav'
        #sound = 'rai000' + str(i+1) +'.wav'
        r = sr.Recognizer()
        
        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
            print("Converting Audio To Text and saving to file..... ") 
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio) ##### API call to google for speech recognition
            if str is bytes: 
                result = u"{}".format(value).encode("utf-8")
            else: 
                result = "{}".format(value)
            if(len(common_member(filtered_questions,result))==0):
                if os.path.exists(sound):
                    print('deleted ')
                    print(sound,end='\n')
                    os.remove(sound)
                else:
                  print("The file does not exist\n")
            else:
                with open("report.txt","a") as f:
                    f.write(sound)
                    f.write(" - ")
                    f.write(result)
                    f.write("\n")
                    f.close()

                
        except sr.UnknownValueError:
            print("UnknownValueError\n")
        except sr.RequestError as e:
            print("{0}".format(e))
        except KeyboardInterrupt:
            pass

p = pyaudio.PyAudio()  # Create an interface to PortAudio
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100

def save_audios(i):
    stream = p.open(format=sample_format,channels=channels,rate=fs,
                frames_per_buffer=chunk,input=True)
    filename = 'record'+str(i)+'.wav'
    read_audio(stream, filename)

#delete all existing .wav files
def delete_existing_audios():
    dir_name = "C:/Users/adhityan/Desktop/proctor/"
    report = os.listdir(dir_name)

    for item in report:
        if item.endswith(".wav"):
            os.remove(os.path.join(dir_name, item))

delete_existing_audios()
#user input of exam duration
import sys
duration=int(sys.argv[1])
f = open("report.txt","r+")
f. truncate(0)
f. close()

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
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

filtered_questions.append('shape')
filtered_questions = set(filtered_questions)
print(filtered_questions)

for i in range(duration//4): # Number of total seconds to record/ Number of seconds per recording
    print(i ,end=" ")
    t1 = threading.Thread(target=save_audios, args=[i]) 
    x = i-1
    t2 = threading.Thread(target=convert, args=[x]) # send one earlier than being recorded
    t1.start() 
    t2.start() 
    t1.join() 
    t2.join() 
    if i==(duration//4) - 1:
        flag = True
if flag:
    convert(i)
    p.terminate()


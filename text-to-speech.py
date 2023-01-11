from gtts import gTTS
from random import randint
import os

while True:
    # inputdan tekst alyar
    text = input(">>> ")
    
    # inputdan alan tekstyny google translate bilen okayar
    audio = gTTS(text=text, lang='en')
    
    # okan sesinin adyny doredyar
    name = "audio"+str(randint(100000, 999999))+".mp3"
    
    # sesi alan ady bilen yatda saklayar
    audio.save(name)
    
    # yatdan saklan sesini okayar
    os.system(name)
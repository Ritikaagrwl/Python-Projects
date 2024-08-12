# healthy programmer - my solutiom 

from time import time
from pygame import mixer
from datetime import datetime

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
        
def log_file(msg):
    with open("ritika.txt","a") as f:
        f.write(f"{msg} - {datetime.now()}\n")

if __name__ == "__main__":
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water = 5 #2400
    eyes = 10 #1800
    exercise = 7 #2700
    
    while True:
    
        if time() - init_water > water:
            print("Water drinking time. Enter Drank to stop the music")
            musiconloop("water.mp3","Drank")
            init_water = time()
            log_file("Drank water at")
        
        if time() - init_eyes > eyes:
            print("Eyes exercise time. Enter EyDone to stop the music")
            musiconloop("eyes.mp3","EyDone")
            init_eyes = time()
            log_file("Eyes exercise done at")
            
        if time() - init_exercise > exercise:
            print("Physical exercise time. Enter ExDone to stop the music")
            musiconloop("physical.mp3","ExDone")
            init_exercise = time()
            log_file("Physical exercise done at")
        
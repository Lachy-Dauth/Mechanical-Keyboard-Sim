from pynput.keyboard import Key,Listener
import random
from pygame import mixer

mixer.init()
    
def playSound(sound):
    mixer.music.load(f"./Sounds/{sound}.mp3")
    mixer.music.set_volume(2)
    mixer.music.play()

count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count+=1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    for key in keys:
        k=str(key).replace("'","")
        if k.find("backspace") > 0:
            playSound("delete")
        elif k.find("enter") > 0:
            playSound("enter")
        elif k.find("shift") > 0:
            playSound("space")
        elif k.find("space") > 0:
            playSound("4")
        elif k.find("caps_lock") >0 :
            playSound(random.randint(1,6))
        elif k.find("Key"):
            playSound(random.randint(1,6))


def on_release(key):
    global exit
    if key == Key.esc:
        exit += 1
        if exit == 2 :
            return False
    else:
        exit = 0

exit = 0
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
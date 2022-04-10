from pynput.keyboard import Key,Listener
import random
from pygame import mixer

mixer.init()
click = 1
    
def playSound(sound):
    if click == 1:
        mixer.music.load(f"./Sounds/{sound}.mp3")
        mixer.music.set_volume(1)
        mixer.music.play()

def on_press(key):
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
    global click
    if key == Key.esc:
        exit += 1
        if exit == 5:
            return False
        if exit == 2:
            click *= -1
    else:
        exit = 0

exit = 0
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
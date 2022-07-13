from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        print('{0} at {1}'.format(
            'Pressed' ,
            (x, y)))

def on_scroll(x, y, dx, dy):
    return False

# Collect events until released
with Listener(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

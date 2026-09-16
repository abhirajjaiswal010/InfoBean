from pynput import keyboard

def on_press(key):
    print("Pressed:", key)

def on_release(key):
    print("Released:", key)

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

listener.start()
listener.join()
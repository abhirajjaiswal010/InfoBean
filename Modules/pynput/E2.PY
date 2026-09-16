from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.space:
        print("Space pressed")

    if key == keyboard.Key.enter:
        print("Enter pressed")

listener = keyboard.Listener(on_press=on_press)

listener.start()
listener.join()      






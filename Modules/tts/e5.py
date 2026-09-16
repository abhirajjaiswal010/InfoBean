import pyttsx3

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

messages = [
    "First message",
    "Second message",
    "Third message"
]

for message in messages:
    engine.say(message)

engine.runAndWait()
engine.stop()
# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

# l = ["Rahul", "Nishant", "Harry"]
# Your program should pronouce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry
# Note: If you are not using windows, try to figure out how to do the same thing using some other package

import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# List of names
names = ["Rahul", "Nishant", "Harry"]

# Loop through the names and pronounce them
for name in names:
    text = f"Shoutout to {name}"
    print(text)
    engine.say(text)
    engine.runAndWait()

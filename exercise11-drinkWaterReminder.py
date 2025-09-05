# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system


import time
from plyer import notification

# Set reminder interval (in seconds) → 1 hour = 3600 sec, 2 hours = 7200 sec
interval = 3600   # change to 7200 for 2 hours

while True:
    # Send desktop notification
    notification.notify(
        title="💧 Water Reminder",
        message="Time to drink a glass of water!",
        timeout=10  # notification stays for 10 seconds
    )

    # Wait before reminding again
    time.sleep(interval)

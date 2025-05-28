import RPi.GPIO as GPIO
import os

# Define GPIO pins for buttons
BUTTON_PINS = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5]  # Adjust these pins as needed
WALLPAPERS = [
    "/home/pi/Pictures/wallpaper1.jpg",
    "/home/pi/Pictures/wallpaper2.jpg",
    "/home/pi/Pictures/wallpaper3.jpg",
    "/home/pi/Pictures/wallpaper4.jpg",
    "/home/pi/Pictures/wallpaper5.jpg",
    "/home/pi/Pictures/wallpaper6.jpg",
    "/home/pi/Pictures/wallpaper7.jpg",
    "/home/pi/Pictures/wallpaper8.jpg",
    "/home/pi/Pictures/wallpaper9.jpg",
    "/home/pi/Pictures/wallpaper10.jpg"
]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def change_wallpaper(channel):
    index = BUTTON_PINS.index(channel)
    wallpaper = WALLPAPERS[index]
    os.system(f"pcmanfm --set-wallpaper {wallpaper}")
    print(f"Wallpaper changed to: {wallpaper}")

# Register event detection
for pin in BUTTON_PINS:
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=change_wallpaper, bouncetime=300)

try:
    print("Waiting for button presses to change wallpaper...")
    while True:
        pass  # Keep the script running

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()

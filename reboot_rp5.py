import RPi.GPIO as GPIO
import time

mosfet_pin = 17  # any GPIO pin number

GPIO.setmode(GPIO.BCM)
GPIO.setup(mosfet_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(mosfet_pin, GPIO.HIGH)  # turn ON load
        time.sleep(.5)
        print("rp5 reboot start...")
        GPIO.output(mosfet_pin, GPIO.LOW)   # turn OFF load
        print("reboot pwr off")
        time.sleep(120)
except KeyboardInterrupt:
    GPIO.cleanup()

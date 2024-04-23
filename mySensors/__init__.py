import adafruit_dht
import RPi.GPIO as GPIO
from picamera2 import Picamera2

DHT_PIN=4

GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT_PIN, GPIO.IN)

mydht = adafruit_dht.DHT11(DHT_PIN)
mycamera = Picamera2()
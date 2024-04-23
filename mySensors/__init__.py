import board
import adafruit_dht
from picamera2 import Picamera2

mydht = adafruit_dht.DHT11(board.D4)
mycamera = Picamera2()
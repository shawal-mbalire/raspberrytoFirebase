from myFirebase import database, storage
from mySensors import camera, dht

hum, temp = dht.measure()
print(database.updateHumidity(hum=hum))
print(database.updateTemperature(temp=temp))

photoSrc = camera.capture()
print(storage.uploadFile(src=photoSrc,type="captured")) # or inferenced


# "image_url": f"https://storage.googleapis.com/green-coffee-beans-75fe4.appspot.com/captured2024-04-23-12_39_15.jpeg",
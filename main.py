from myFirebase import database, storage

print(database.updateHumidity(61))
print(database.updateTemperature(24))
print(storage.uploadFile(src="download.jpeg",type="captured")) # or inferenced
from firebase import database, storage

print(database.ref.get())
print(storage.uploadFile(src="download.jpeg",name="download.jpeg"))